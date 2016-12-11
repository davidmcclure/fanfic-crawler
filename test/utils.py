

import os


def get_fixture(itemtype, id):

    """
    Read fixture text.
    """

    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures/{}/{}.html'.format(itemtype, id),
    )

    with open(path) as fh:
        return fh.read()
