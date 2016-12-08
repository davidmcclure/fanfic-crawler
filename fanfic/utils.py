

import re


def href_to_id(href: str) -> int:

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


# def parse_metadata(raw: str) -> dict:

    # """
    # Parse the metadata string.
    # """

    # parts = raw.split('-')

    # metadata = dict([
        # map(strip, part.split(':'))
        # for part in parts
        # if ':' in part
    # ])

    # characters = parts[3]

    # genres = parts[2]

    # return metadata
