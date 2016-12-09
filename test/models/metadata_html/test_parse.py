

import pytest
import os
import yaml

from fanfic.models import MetadataHTML, Metadata
from fanfic.database import session


pytestmark = pytest.mark.usefixtures('db')


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


cases = read_yaml(__file__, 'ingest.yml')


@pytest.mark.parametrize('book_id,case', cases.items())
def test_parse(book_id, case):

    html_row = MetadataHTML(book_id=book_id, html=case['html'])

    row = html_row.parse()

    for key, val in case['fields'].items():
        assert getattr(row, key) == val
