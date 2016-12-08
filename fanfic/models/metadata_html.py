

from sqlalchemy import Column, Integer, String

from .base import Base


class MetadataHTML(Base):

    __tablename__ = 'metadata_html'

    id = Column(Integer, primary_key=True)

    book_id = Column(Integer, nullable=False)

    html = Column(String, nullable=False)
