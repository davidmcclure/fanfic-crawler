

import os
import yaml


def read_yaml(from_path, file_name):
    """Open a YAML file relative to the passed path.

    Args:
        from_path (str)
        file_name (str)

    Returns: dict
    """
    path = os.path.join(os.path.dirname(from_path), file_name)

    with open(path, 'r') as fh:
        return yaml.load(fh)


def read_metadata_fixture(book_id: int):
    """Read a metadata fixture.
    """
    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures/metadata/{}.html'.format(book_id),
    )

    with open(path) as fh:
        return fh.read()


def read_review_fixture(book_id: int, review_id: int):
    pass
