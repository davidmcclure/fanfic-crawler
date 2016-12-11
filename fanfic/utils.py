

import re

from textblob import TextBlob


def extract_int(href: str) -> int:

    """
    Extract a numeric id from an href.
    """

    return int(re.search('[0-9]+', href).group())


def clean_string(value: str) -> str:

    """
    - Strip whitespace.
    - Replace whitespace strings with 1 space.
    """

    return re.sub('\s+', ' ', value.strip())


def atoi(value: str) -> int:

    """
    Replace commas, parse int.
    """

    return int(value.replace(',', ''))


def pos_tags(text: str) -> list:

    """
    Return a list of POS tags from a text.
    """

    blob = TextBlob(text)

    return [pos for _, pos in blob.tags]
