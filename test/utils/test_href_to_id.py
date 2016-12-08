

import pytest

from fanfic.utils import href_to_id


@pytest.mark.parametrize('href,id', [
    ('/u/3306612/the-Imaginizer', 3306612),
])
def test_href_to_id(href, id):
    assert href_to_id(href) == id
