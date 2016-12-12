

import os


def read_metadata_fixture(book_id: int):

    """
    Read a metadata fixture.
    """

    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures/metadata/{}.html'.format(book_id),
    )

    with open(path) as fh:
        return fh.read()
