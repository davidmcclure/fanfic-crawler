

from sqlalchemy import Column, Integer, String

from .base import Base
from .mixins import ScrapedItem


class ReviewHTML(Base, ScrapedItem):

    __tablename__ = 'review_html'

    id = Column(Integer, primary_key=True)

    book_id = Column(Integer, nullable=False)

    html = Column(String, nullable=False)
