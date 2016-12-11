

import re

from dateutil.parser import parse as dateutil_parse
from datetime import date


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


def parse_date(value: str):

    """
    Try to parse a date string. On failure, return today.
    """

    try:
        return dateutil_parse(value).date()

    except ValueError:
        return date.today()
