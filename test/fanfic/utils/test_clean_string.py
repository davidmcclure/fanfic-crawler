

import pytest

from fanfic.utils import clean_string


@pytest.mark.parametrize('raw,clean', [

    # Strip surrounding whitespace
    (' test ', 'test'),

    # Strip linebreaks
    ('test1\ntest2', 'test1 test2'),

    # Replace 2+ whitespace chars with 1.
    ('test1  test2', 'test1 test2'),

])
def test_clean_string(raw, clean):
    assert clean_string(raw) == clean
