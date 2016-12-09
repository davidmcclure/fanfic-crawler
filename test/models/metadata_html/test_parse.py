

import pytest

from fanfic.models import MetadataHTML, Metadata
from fanfic.utils import read_yaml


pytestmark = pytest.mark.usefixtures('db')


cases = read_yaml(__file__, 'fixtures.yml')


@pytest.mark.parametrize('book_id,case', cases.items())
def test_parse(book_id, case):

    html_row = MetadataHTML(book_id=book_id, html=case['html'])

    row = html_row.parse()

    for key, val in case['fields'].items():
        assert getattr(row, key) == val
