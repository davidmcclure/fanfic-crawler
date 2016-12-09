

from sqlalchemy import Column, Integer, String
from scrapy.selector import Selector

from fanfic.utils import extract_int, parse_metadata
from fanfic.database import session

from .base import Base
from .metadata import Metadata


class MetadataHTML(Base):

    __tablename__ = 'metadata_html'

    # TODO: Use book id as PK?
    id = Column(Integer, primary_key=True)

    book_id = Column(Integer, nullable=False)

    html = Column(String, nullable=False)

    @classmethod
    def ingest(cls):

        """
        Load parsed metadata rows.
        """

        # TODO: Bulk-insert?

        for html_row in cls.query.all():
            session.add(html_row.parse())

        session.commit()

    def parse(self):

        """
        Extract metadata fields.

        Returns: Metadata
        """

        tree = Selector(text=self.html)

        title = (
            tree.xpath('//div[@id="profile_top"]/b/text()')
            .extract_first()
        )

        user_id = extract_int(
            tree.xpath('//div[@id="profile_top"]/a/@href')
            .extract_first()
        )

        username = (
            tree.xpath('//div[@id="profile_top"]/a/text()')
            .extract_first()
        )

        summary = (
            tree.xpath('//div[@id="profile_top"]/div/text()')
            .extract_first()
        )

        raw_metadata = ''.join(
            tree.xpath('''
                //div[@id="profile_top"]/
                span[position()=last()]//text()
            ''')
            .extract()
        )

        metadata = parse_metadata(raw_metadata)

        return Metadata(
            book_id=self.book_id,
            title=title,
            user_id=user_id,
            username=username,
            summary=summary,
            **metadata
        )
