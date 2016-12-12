

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from .base import Base


class BookId(Base):

    __tablename__ = 'book_id'

    book_id = Column(Integer, primary_key=True, autoincrement=False)

    chapters = relationship('Chapter')

    metadata_html = relationship('MetadataHTML')

    reviews = relationship('ReviewHTML')

    @classmethod
    def ids(cls):

        """
        Provide book ids as a list.
        """

        return [r.book_id for r in cls.query.all()]

    @classmethod
    def without_chapters(cls):

        """
        Get book ids without any downloaded chapters.
        """

        query = (
            cls.query
            .filter(cls.chapters == None)  # noqa: E711
            .all()
        )

        return [row.book_id for row in query]

    @classmethod
    def without_metadata_html(cls):

        """
        Get book ids without downloaded metadata.
        """

        query = (
            cls.query
            .filter(cls.metadata_html == None)  # noqa: E711
            .all()
        )

        return [row.book_id for row in query]

    @classmethod
    def without_reviews(cls):

        """
        Get book ids without any downloaded reviews.
        """

        query = (
            cls.query
            .filter(cls.reviews == None)  # noqa: E711
            .all()
        )

        return [row.book_id for row in query]
