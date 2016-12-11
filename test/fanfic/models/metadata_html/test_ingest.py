

import pytest

from datetime import datetime as dt

from fanfic.models import MetadataHTML, Metadata
from fanfic.database import session

from test.utils import get_fixture


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

])
def test_ingest(book_id, fields):

    html = get_fixture('metadata', book_id)

    html_row = MetadataHTML(book_id=book_id, html=html)

    session.add(html_row)

    MetadataHTML.ingest()

    row = Metadata.query.filter_by(book_id=book_id).one()

    for key, val in fields.items():
        assert getattr(row, key) == val
