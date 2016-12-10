

import re
import yaml
import os

from dateutil.parser import parse as dateutil_parse
from datetime import date


def read_yaml(from_path, file_name):

    """
    Open a YAML file relative to the passed path.

    Args:
        from_path (str)
        file_name (str)

    Returns: dict
    """

    path = os.path.join(os.path.dirname(from_path), file_name)

    with open(path, 'r') as fh:
        return yaml.load(fh)


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
