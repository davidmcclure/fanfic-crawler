

from nltk.tokenize import RegexpTokenizer
from collections import OrderedDict

from fanfic.utils import clean_string, atoi


GENRES = set([
    'Adventure',
    'Angst',
    'Crime',
    'Drama',
    'Family',
    'Fantasy',
    'Friendship',
    'General',
    'Horror',
    'Humor',
    'Hurt',
    'Comfort',
    'Mystery',
    'Parody',
    'Poetry',
    'Romance',
    'Sci-Fi',
    'Spiritual',
    'Supernatural',
    'Suspense',
    'Tragedy',
    'Western',
])


def is_genre(text: str) -> bool:

    """
    Check if a string contains any of the genre words.
    """

    tokens = RegexpTokenizer('[a-zA-Z]+').tokenize(text)

    return bool(set(tokens).intersection(GENRES))


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
        Try to find a genres list.
        """

        keys = list(self.keys())

        if keys[4] == 'Chapters':
            return list(self.keys())[2]

        elif keys[3] == 'Chapters' and is_genre(keys[2]):
            return keys[2]

    def characters(self) -> str:

        """
        Try to find a characters list.
        """

        keys = list(self.keys())

        if keys[4] == 'Chapters':
            return list(self.keys())[3]

        elif keys[3] == 'Chapters' and not is_genre(keys[2]):
            return keys[2]
