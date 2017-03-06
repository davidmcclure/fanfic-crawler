

from datetime import datetime as dt

from cached_property import cached_property
from sqlalchemy import Column, Integer, String, ForeignKey
from lxml import html

from fanfic.services import session
from fanfic.utils import clean_string, extract_int

from .base import Base
from .mixins import ScrapyItem
from .review import Review


class ReviewHTML(Base, ScrapyItem):

    __tablename__ = 'review_html'

    book_id = Column(
        ForeignKey('book_id.book_id'),
        primary_key=True,
        autoincrement=False,
    )

    review_id = Column(Integer, primary_key=True, autoincrement=False)

    html = Column(String, nullable=False)

    @classmethod
    def ingest(cls):
        """Parse HTML, load rows into Review.
        """
        for html in cls.query.all():
            session.add(html.parse())

        session.commit()

    @cached_property
    def tree(self):
        """Wrap the HTML as a Scrapy selector.

        Returns: Selector
        """
        return html.fragment_fromstring(self.html)

    def review(self):
        """Query the review.
        """
        return self.tree.xpath('td/div/text()')[0]

    def published(self):
        """Query the publication date.
        """
        xutime = self.tree.xpath('//*[@data-xutime]/@data-xutime')[0]

        return dt.fromtimestamp(int(xutime))

    def user_id(self):
        """Try to get a registered username, fall back on guest name.
        """
        user = self.tree.xpath('td/a/@href')

        # Take the user id, if present.
        if len(user):
            return extract_int(user[0])

    def username(self):
        """Try to get a registered username, fall back on guest name.
        """
        user = self.tree.xpath('td/a/text()')

        # Take the user link, if present.
        if len(user):
            return user[0]

        # Otherwise take the guest name.
        else:
            guest = self.tree.xpath('td/text()')[0]
            return clean_string(guest)

    def chapter_number(self):
        """Get the chapter number.
        """
        small = self.tree.xpath('td/small/text()')[0]

        return extract_int(small.split('.')[0])

    def parse(self):
        """Map into the Metadata model.

        Returns: Metadata
        """
        return Review(
            book_id=self.book_id,
            review_id=self.review_id,
            user_id=self.user_id(),
            username=self.username(),
            chapter_number=self.chapter_number(),
            review=self.review(),
            published=self.published(),
        )
