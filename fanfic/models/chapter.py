

from sqlalchemy import Column, Integer, String

from .base import Base
from .mixins import ScrapyItem


class Chapter(Base, ScrapyItem):

    __tablename__ = 'chapter'

    book_id = Column(Integer, primary_key=True, autoincrement=False)

    chapter_number = Column(Integer, primary_key=True, autoincrement=False)

    chapter = Column(String, nullable=False)
