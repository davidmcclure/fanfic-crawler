

from collections import OrderedDict

from fanfic.utils import clean_string, atoi


class MetadataDetailsParser(OrderedDict):

    def __init__(self, details):

        """
        Parse the raw details string.
        """

        parts = details.split('-')

        for part in parts:

            if ':' in part:
                key, val = part.split(':')
                self[clean_string(key)] = clean_string(val)

            else:
                self[clean_string(part)] = None

    def parse_key(self, key, parse=None, default=None):

        """
        Look up a key. If a parse function is provided, apply it. If the key
        is missing, return the default.
        """

        val = self.get(key)

        if val:
            return parse(val) if parse else val

        else:
            return default

    def follows(self) -> int:

        """
        Cast 'Follows' to an integer.
        """

        return self.parse_key('Follows', atoi)

    def favorites(self) -> int:

        """
        Cast 'Favs' to an integer.
        """

        return self.parse_key('Favs', atoi)

    def rating(self) -> str:

        """
        Provide 'Rated' as-is.
        """

        return self.get('Rated')

    def language(self) -> str:

        """
        Language is always the second element.
        """

        return list(self.keys())[1]

    def genres(self) -> str:

        """
        TODO
        """

        return list(self.keys())[2]

    def characters(self) -> str:

        """
        TODO
        """

        return list(self.keys())[3]
