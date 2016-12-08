

import pytest

from fanfic.utils import atoi


@pytest.mark.parametrize('raw,parsed', [
    ('1,234', 1234),
])
def test_atoi(raw, parsed):
    assert atoi(raw) == parsed
