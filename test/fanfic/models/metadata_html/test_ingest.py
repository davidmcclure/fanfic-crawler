

import pytest

from datetime import datetime as dt

from fanfic.models import MetadataHTML, Metadata
from fanfic.database import session

from test.utils import get_fixture


pytestmark = pytest.mark.usefixtures('db')


@pytest.mark.parametrize('book_id,fields', [

    (12241223, dict(
        book_id=12241223,
        title='Scar Tissue',
        user_id=8476478,
        username='Slytherin\'s King',
        summary="A few years ago, Draco's life changed for the worst. Still, he could live with it, he could adapt. But when another werewolf comes in Hogwarts to teach the students, it starts to get dangerous. Their absences and behavior towards each other raise some eyebrows and Draco is afraid that a curious mind might even end up seeing right through him. (AU -Werewolf!Draco - Dramione)",
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
        summary="The time turner around Harrys neck shattered sending his soul back in time; where his body could not go. When Harry finds himself in a ten year old body; in his aunts garden he vows to do things right this time and save everyone he lost. First he needs to make his friends into the new Marauders and convince the sorting hat to unite him with his own alternative to Sirius Black.",
        rating='Fiction T',
        language='English',
        genres='Adventure/Friendship',
        characters='Harry P., Ron W., Hermione G., Draco M.',
        follows=1777,
        favorites=1068,
        published=dt.fromtimestamp(1462477100),
        updated=dt.fromtimestamp(1481386185),
    )),

    (83174, dict(
        book_id=83174,
        title='Violet\'s Story',
        user_id=20430,
        username='Moondust',
        summary="Hey everyone! This my first fic and I would like to know how you all like it, so please read and review. Thanks!",
        rating='Fiction K+',
        language='English',
        genres=None,
        characters=None,
        follows=None,
        favorites=2,
        published=dt.fromtimestamp(970297200),
        updated=None,
    )),

])
def test_ingest(book_id, fields):

    html = get_fixture('metadata', book_id)

    html_row = MetadataHTML(book_id=book_id, html=html)

    session.add(html_row)

    MetadataHTML.ingest()

    row = Metadata.query.filter_by(book_id=book_id).one()

    for key, val in fields.items():
        assert getattr(row, key) == val
