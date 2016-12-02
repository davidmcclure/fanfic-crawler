

from sqlalchemy import Column, Integer, String

from .base import Base


class Chapter(Base):

    __tablename__ = 'chapter'

    book_id = Column(Integer, primary_key=True)

    chapter_number = Column(Integer, nullable=False)

    content = Column(String, nullable=False)