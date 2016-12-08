

from sqlalchemy import Column, Integer, String, Date

from .base import Base


class ReviewHTML(Base):

    __tablename__ = 'review_html'

    id = Column(Integer, primary_key=True)

    book_id = Column(Integer, nullable=False)

    html = Column(String, nullable=False)
