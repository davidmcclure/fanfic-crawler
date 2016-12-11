

from sqlalchemy import Column, Integer, String
from cached_property import cached_property
from lxml import etree, html

from fanfic.utils import extract_int

from .base import Base
from .mixins import ScrapyItem


class MetadataHTML(Base, ScrapyItem):

    __tablename__ = 'metadata_html'

    book_id = Column(Integer, primary_key=True)

    html = Column(String, nullable=False)

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

    def metadata_string(self):

        """
        Query the raw metadata string.
        """

        parts = self.tree.xpath('span[position()=last()]//text()')

        return ''.join(parts)
