

from sqlalchemy import Column, Integer

from .base import Base


class BookId(Base):

    __tablename__ = 'book_id'

    book_id = Column(Integer, primary_key=True, autoincrement=False)

    @classmethod
    def ids(cls):

        """
        Provide book ids as a list.
        """

        return [r.book_id for r in cls.query.all()]

    def without_chapters(cls) -> list:

        """
        Get book IDs without downloaded chapters.
        """

        pass
