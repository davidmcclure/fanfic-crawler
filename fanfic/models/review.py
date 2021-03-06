

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

from .base import Base


class Review(Base):

    __tablename__ = 'review'

    book_id = Column(
        ForeignKey('book_id.book_id'),
        primary_key=True,
        autoincrement=False,
    )

    review_id = Column(Integer, primary_key=True, autoincrement=False)

    user_id = Column(Integer, nullable=True)

    username = Column(String, nullable=True)

    chapter_number = Column(Integer, nullable=True)

    review = Column(String, nullable=True)

    published = Column(DateTime, nullable=True)
