

from sqlalchemy import Column, Integer, String

from .base import Base
from .mixins import ScrapedItem


class MetadataHTML(Base, ScrapedItem):

    __tablename__ = 'metadata_html'

    book_id = Column(Integer, primary_key=True)

    html = Column(String, nullable=False)
