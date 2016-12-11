

from datetime import datetime as dt

from sqlalchemy import Column, Integer, String

from cached_property import cached_property
from lxml import html

from fanfic.database import session
from fanfic.utils import extract_int, clean_string, atoi, parse_date
from fanfic.parse_dict import ParseDict

from .base import Base
from .mixins import ScrapyItem
from .metadata import Metadata


class MetadataHTML(Base, ScrapyItem):

    __tablename__ = 'metadata_html'

    book_id = Column(Integer, primary_key=True)

    html = Column(String, nullable=False)

    @classmethod
    def ingest(cls):

        """
        Parse HTML, load rows into Metadata.
        """

        for html in cls.query.all():
            session.add(html.parse())

        session.commit()

    @cached_property
    def tree(self):

        """
        Wrap the HTML as a Scrapy selector.

        Returns: Selector
        """

        return html.fragment_fromstring(self.html)

    def title(self):

        """
        Query the title.
        """

        return self.tree.xpath('b/text()')[0]

    def user_id(self):

        """
        Query the title.
        """

        href = self.tree.xpath('a/@href')[0]

        return extract_int(href)

    def username(self):

        """
        Query the username.
        """

        return self.tree.xpath('a/text()')[0]

    def summary(self):

        """
        Query the summary.
        """

        return self.tree.xpath('div/text()')[0]

    def xutimes(self):

        """
        Query data-xutime timestamps.
        """

        return self.tree.xpath('//*[@data-xutime]/@data-xutime')

    def published(self):

        """
        Query the published timestamp.
        """

        xutimes = self.xutimes()

        offset = 0 if len(xutimes) == 1 else 1

        return dt.fromtimestamp(int(xutimes[offset]))

    def updated(self):

        """
        Query the published timestamp.
        """

        xutimes = self.xutimes()

        return (
            dt.fromtimestamp(int(xutimes[0]))
            if len(xutimes) == 2 else None
        )

    def details_string(self):

        """
        Query the raw metadata string.
        """

        parts = self.tree.xpath('span[position()=last()]//text()')

        return ''.join(parts)

    def details(self):

        """
        Parse fields out of the details string.
        """

        parts = self.details_string().split('-')

        fields = ParseDict([
            [clean_string(p) for p in part.split(':')]
            for part in parts if ':' in part
        ])

        language = parts[1]

        genres = parts[2]

        characters = parts[3]

        return dict(
            follows=fields.parse('Follows', atoi),
            favorites=fields.parse('Favs', atoi),
            rating=fields.get('Rated'),
            language=clean_string(language),
            genres=clean_string(genres),
            characters=clean_string(characters),
        )

    def parse(self):

        """
        Map into the Metadata model.

        Returns: Metadata
        """

        details = self.details()

        return Metadata(
            book_id=self.book_id,
            title=self.title(),
            user_id=self.user_id(),
            username=self.username(),
            summary=self.summary(),
            published=self.published(),
            updated=self.updated(),
            **details
        )
