

import pytest

from datetime import date

from fanfic.utils import parse_date


@pytest.mark.parametrize('raw,parsed', [

    ('Mar 21, 2015', date(2015, 3, 21)),

    # When no year, assume current.
    ('Jun 2', date(date.today().year, 6, 2)),

    # When invalid, assume today.
    ('30m ago', date.today()),

])
def test_parse_date(raw, parsed):
    assert parse_date(raw) == parsed
