

from datetime import datetime as dt
from collections import OrderedDict

from cached_property import cached_property
from sqlalchemy import Column, Integer, String
from lxml import html

from fanfic.database import session
from fanfic.utils import extract_int, clean_string, atoi
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

        details = DetailsString(self.details_string())

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


class DetailsString(OrderedDict):

    def __init__(self, raw):

        """
        Parse the raw details string.
        """

        parts = raw.split('-')

        for part in parts:

            if ':' in part:
                key, val = part.split(':')
                self[clean_string(key)] = clean_string(val)

            else:
                self[clean_string(part)] = None

    def parse_key(self, key, parse=None, default=None):

        """
        Look up a key. If a parse function is provided, apply it. If the key
        is missing, return the default.
        """

        val = self.get(key)

        if val:
            return parse(val) if parse else val

        else:
            return default

    def follows(self) -> int:

        """
        Cast 'Follows' to an integer.
        """

        return self.parse_key('Follows', atoi)

    def favorites(self) -> int:

        """
        Cast 'Favs' to an integer.
        """

        return self.parse_key('Favs', atoi)

    def rating(self) -> str:

        """
        Provide 'Rated' as-is.
        """

        return self.get('Rated')

    def language(self) -> str:

        """
        Language is always the second element.
        """

        return list(self.keys())[1]

    def genres(self) -> str:

        """
        TODO
        """

        return list(self.keys())[2]

    def characters(self) -> str:

        """
        TODO
        """

        return list(self.keys())[3]
