

from datetime import datetime as dt

from cached_property import cached_property
from sqlalchemy import Column, Integer, String
from lxml import html

from fanfic.database import session
from fanfic.utils import clean_string, extract_int

from .base import Base
from .mixins import ScrapyItem


class ReviewHTML(Base, ScrapyItem):

    __tablename__ = 'review_html'

    id = Column(Integer, primary_key=True)

    book_id = Column(Integer, nullable=False)

    html = Column(String, nullable=False)

    @classmethod
    def ingest(cls):

        """
        Parse HTML, load rows into Review.
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

    def review(self):

        """
        Query the review.
        """

        return self.tree.xpath('td/div/text()')[0]

    def published(self):

        """
        Query the publication date.
        """

        xutime = self.tree.xpath('//*[@data-xutime]/@data-xutime')[0]

        return dt.fromtimestamp(int(xutime))

    def user_id(self):

        """
        Try to get a registered username, fall back on guest name.
        """

        user = self.tree.xpath('td/a/@href')

        # Take the user id, if present.
        if len(user):
            return extract_int(user[0])

    def username(self):

        """
        Try to get a registered username, fall back on guest name.
        """

        user = self.tree.xpath('td/a/text()')

        # Take the user link, if present.
        if len(user):
            return user[0]

        # Otherwise take the guest name.
        else:
            guest = self.tree.xpath('td/text()')[0]
            return clean_string(guest)
