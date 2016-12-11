

from sqlalchemy import Column, Integer, String

from .base import Base
from .mixins import ScrapyItem


class Chapter(Base, ScrapyItem):

    __tablename__ = 'chapter'

    book_id = Column(Integer, primary_key=True)

    chapter_number = Column(Integer, primary_key=True)

    chapter = Column(String, nullable=False)
