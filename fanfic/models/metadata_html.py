

from sqlalchemy import Column, Integer, String

from .base import Base


class MetadataHTML(Base):

    __tablename__ = 'metadata_html'

    book_id = Column(Integer, primary_key=True)

    html = Column(String, nullable=False)
