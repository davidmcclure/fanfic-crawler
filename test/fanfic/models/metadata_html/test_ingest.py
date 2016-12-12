

import pytest

from datetime import datetime as dt

from fanfic.models import MetadataHTML, Metadata
from fanfic.singletons import session

from test.utils import read_yaml


cases = read_yaml(__file__, 'ingest.yml')


@pytest.fixture(scope='module', autouse=True)
def ingest(db_module):

    """
    Write HTML fixtures into the database.
    """

    for book_id, html in cases.items():
        row = MetadataHTML(book_id=book_id, html=html)
        session.add(row)

    MetadataHTML.ingest()


@pytest.mark.parametrize('book_id,fields', [

    (12241223, dict(
        book_id=12241223,
        title='Scar Tissue',
        user_id=8476478,
        username='Slytherin\'s King',
        summary="A few years ago, Draco's life changed for the worst. Still, he could live with it, he could adapt. But when another werewolf comes in Hogwarts to teach the students, it starts to get dangerous. Their absences and behavior towards each other raise some eyebrows and Draco is afraid that a curious mind might even end up seeing right through him. (AU -Werewolf!Draco - Dramione)",  # noqa: E501
        rating='Fiction T',
        language='English',
        genres='Angst/Romance',
        characters='Hermione G., Draco M., Lucius M., Narcissa M.',
        follows=37,
        favorites=22,
        published=dt.fromtimestamp(1479684054),
        updated=dt.fromtimestamp(1481476219),
    )),

    (11931564, dict(
        book_id=11931564,
        title='The Red Dragon',
        user_id=5439553,
        username='Yes I am using a typewriter',
        summary="The time turner around Harrys neck shattered sending his soul back in time; where his body could not go. When Harry finds himself in a ten year old body; in his aunts garden he vows to do things right this time and save everyone he lost. First he needs to make his friends into the new Marauders and convince the sorting hat to unite him with his own alternative to Sirius Black.",  # noqa: E501
        rating='Fiction T',
        language='English',
        genres='Adventure/Friendship',
        characters='Harry P., Ron W., Hermione G., Draco M.',
        follows=1777,
        favorites=1068,
        published=dt.fromtimestamp(1462477100),
        updated=dt.fromtimestamp(1481386185),
    )),

    # No genres, no characters.
    (83174, dict(
        book_id=83174,
        title='Violet\'s Story',
        user_id=20430,
        username='Moondust',
        summary="Hey everyone! This my first fic and I would like to know how you all like it, so please read and review. Thanks!",  # noqa: E501
        rating='Fiction K+',
        language='English',
        genres=None,
        characters=None,
        follows=None,
        favorites=2,
        published=dt.fromtimestamp(970297200),
        updated=None,
    )),

    # Genres, no characters.
    (248475, dict(
        book_id=248475,
        title='Apple Pie and Enchiladas',
        user_id=8669,
        username='gaelicchick',
        summary="Dark forces and flying drumsticks, talking birds, talking mirrors, bigotry, love, and a quest to save the last remnant of a vanishing people. Fifth year, Sirius and Remus cameos and a tiny hint of R/Hermione*FINAL CHAPTER*",  # noqa: E501
        rating='Fiction T',
        language='English',
        genres='Drama',
        characters=None,
        follows=1,
        favorites=13,
        published=dt.fromtimestamp(986713200),
        updated=dt.fromtimestamp(1012858887),
    )),

    # Characters, no genres.
    (12026134, dict(
        book_id=12026134,
        title='Harry Potter and the ? (Goblet of Fire)',
        user_id=2720740,
        username='bookhater95',
        summary="Though the worst has been revealed, now that Harry has Sirius on his side they're all confident Harry's next year must go smoothly...right? Part of my Reading the ? book's series. Status: In Progress",  # noqa: E501
        rating='Fiction T',
        language='English',
        genres=None,
        characters='Sirius B., Remus L., James P., Lily Evans P.',
        follows=306,
        favorites=225,
        published=dt.fromtimestamp(1467313627),
        updated=dt.fromtimestamp(1481476222),
    )),

])
def test_ingest(book_id, fields):

    row = Metadata.query.filter_by(book_id=book_id).one()

    for key, val in fields.items():
        assert getattr(row, key) == val
