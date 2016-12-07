

from sqlalchemy import Column, Integer, String

from .base import Base


class Metadata(Base):

    __tablename__ = 'metadata'

    book_id = Column(Integer, primary_key=True)

    # TODO
