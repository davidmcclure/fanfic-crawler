

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


def atoi(value: str) -> int:

    """
    Replace commas, parse int.
    """

    return int(value.replace(',', ''))


def parse_metadata(raw: str) -> dict:

    """
    Parse the metadata string.
    """

    parts = raw.split('-')

    metadata = dict([
        [clean_string(p) for p in part.split(':')]
        for part in parts if ':' in part
    ])

    language = clean_string(parts[1])

    genres = clean_string(parts[2])

    characters = clean_string(parts[3])

    return dict(
        rating      = metadata['Rated'],
        favorites   = atoi(metadata['Favs']),
        follows     = atoi(metadata['Follows']),
        language    = language,
        genres      = genres,
        characters  = characters,
    )
