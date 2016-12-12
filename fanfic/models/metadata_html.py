

from datetime import datetime as dt

from cached_property import cached_property
from sqlalchemy import Column, String, ForeignKey
from lxml import html

from fanfic.services import session
from fanfic.parsers import MetadataDetailsParser
from fanfic.utils import extract_int

from .base import Base
from .mixins import ScrapyItem
from .metadata import Metadata


class MetadataHTML(Base, ScrapyItem):

    __tablename__ = 'metadata_html'

    book_id = Column(
        ForeignKey('book_id.book_id'),
        primary_key=True,
        autoincrement=False,
    )

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

        # If there are 2 xutimes, published is the second. Otherwise, it is the
        # first and only xutime.

        offset = 0 if len(xutimes) == 1 else 1

        return dt.fromtimestamp(int(xutimes[offset]))

    def updated(self):

        """
        Query the updated timestamp.
        """

        xutimes = self.xutimes()

        # If there are 2 xutimes, updated is the first. Otherwise, there is no
        # updated date, just published.

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

        details = MetadataDetailsParser(self.details_string())

        return dict(
            follows=details.follows(),
            favorites=details.favorites(),
            rating=details.rating(),
            language=details.language(),
            genres=details.genres(),
            characters=details.characters(),
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
