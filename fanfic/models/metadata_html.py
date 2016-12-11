

from sqlalchemy import Column, Integer, String

from .base import Base
from .mixins import ScrapyItem


class MetadataHTML(Base, ScrapyItem):

    __tablename__ = 'metadata_html'

    book_id = Column(Integer, primary_key=True)

    html = Column(String, nullable=False)
