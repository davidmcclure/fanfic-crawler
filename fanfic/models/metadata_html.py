

from sqlalchemy import Column, Integer, String
from cached_property import cached_property
from lxml import etree, html

from fanfic.utils import extract_int, clean_string, atoi, parse_date

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

        fields = dict([
            [clean_string(p) for p in part.split(':')]
            for part in parts if ':' in part
        ])

        language = parts[1]

        genres = parts[2]

        characters = parts[3]

        return dict(

            follows     = atoi(fields['Follows']),
            favorites   = atoi(fields['Favs']),
            published   = parse_date(fields['Published']),
            rating      = fields['Rated'],

            language    = clean_string(language),
            genres      = clean_string(genres),
            characters  = clean_string(characters),

        )
