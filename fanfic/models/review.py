

from sqlalchemy import Column, Integer, String, Date

from .base import Base


class Review(Base):

    __tablename__ = 'review'

    book_id = Column(Integer, primary_key=True)

    user_id = Column(Integer, nullable=True)

    username = Column(String, nullable=True)

    chapter_number = Column(Integer, nullable=True)

    review = Column(String, nullable=True)

    published = Column(Date, nullable=True)
