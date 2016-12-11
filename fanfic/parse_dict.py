

class ParseDict(dict):

    def parse(self, key, parse=None, default=None):

        """
        Look up a key. If a parse function is provided, apply it. If the key
        is missing, return the default.
        """

        val = super().get(key)

        if val:
            return parse(val) if parse else val

        else:
            return default
