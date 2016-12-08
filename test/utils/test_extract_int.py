

import pytest

from fanfic.utils import extract_int


@pytest.mark.parametrize('href,id', [

    ('/u/3306612/the-Imaginizer', 3306612),

    ('Chapter 16', 16),

])
def test_extract_int(href, id):
    assert extract_int(href) == id
