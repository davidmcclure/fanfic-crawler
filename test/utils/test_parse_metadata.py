

import pytest

# from fanfic.utils import parse_metadata


@pytest.mark.skip
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
        )

    ),

])
def test_test(raw, parsed):
    assert parse_metadata(raw) == parsed
