

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship

from .base import Base


class Review(Base):

    __tablename__ = 'review'

    review_id = Column(Integer, primary_key=True)

    book_id = Column(Integer, nullable=False)

    user_id = Column(Integer, nullable=True)

    username = Column(String, nullable=True)

    chapter_number = Column(Integer, nullable=True)

    review = Column(String, nullable=True)

    published = Column(DateTime, nullable=True)
