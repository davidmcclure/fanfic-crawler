

import pytest

from datetime import date

from fanfic.utils import parse_metadata


@pytest.mark.parametrize('raw,parsed', [

    (

        '''
        Rated: Fiction T - English - Friendship/Adventure - Hermione G., Sirius
        B., Remus L., Marauders - Chapters: 95 - Words: 359,385 - Reviews:
        1,233 - Favs: 620 - Follows: 1,002 - Updated: 22m ago - Published: Mar
        21, 2015 - id: 11129273
        ''',

        dict(
            rating='Fiction T',
            language='English',
            genres='Friendship/Adventure',
            characters='Hermione G., Sirius B., Remus L., Marauders',
            favorites=620,
            follows=1002,
            published=date(2015, 3, 21),
        )

    ),

    (

        '''
        Rated: Fiction K - English - Romance - Hermione G., Ron W. - Chapters:
        20 - Words: 67,939 - Reviews: 608 - Favs: 62 - Follows: 13 - Updated:
        Mar 30, 2001 - Published: Jan 2, 2001 - id: 162160
        ''',

        dict(
            rating='Fiction K',
            language='English',
            genres='Romance',
            characters='Hermione G., Ron W.',
            favorites=62,
            follows=13,
            published=date(2001, 1, 2),
        )

    ),

    (

        '''
        Rated: Fiction T - English - Angst/Romance - Hermione G., Draco M.,
        Lucius M., Narcissa M. - Chapters: 12 - Words: 69,397 - Reviews: 12 -
        Favs: 19 - Follows: 34 - Updated: Dec 4 - Published: Nov 20 - id:
        12241223
        ''',

        dict(
            rating='Fiction T',
            language='English',
            genres='Angst/Romance',
            characters='Hermione G., Draco M., Lucius M., Narcissa M.',
            favorites=19,
            follows=34,
            published=date(2016, 11, 20),
        )

    ),

])
def test_parse_metadata(raw, parsed):
    assert parse_metadata(raw) == parsed
