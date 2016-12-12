

import re


def extract_int(href: str) -> int:

    """
    Extract a numeric id from an href.
    """

    # TODO: Should this always take the first match?

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


def flatten_dict(d, root=True):

    """
    Flatten a dict into a list of tuples.

    Args:
        nested (dict)

    Yields: ((key1, key2, ...), val)
    """

    for k, v in d.items():

        if isinstance(v, dict):
            for item in flatten_dict(v, False):

                # At root level, break away the key path from the value.
                if root:
                    yield ((k,) + item[:-1], item[-1])

                # Otherwise build up the key chain.
                else:
                    yield (k,) + item

        else:
            yield (k, v)
