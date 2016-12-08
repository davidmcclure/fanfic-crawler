

from sqlalchemy import Column, Integer, String

from .base import Base


class Metadata(Base):

    __tablename__ = 'metadata'

    book_id = Column(Integer, primary_key=True)

    title = Column(String, nullable=True)

    user_id = Column(Integer, nullable=True)

    username = Column(String, nullable=True)

    summary = Column(String, nullable=True)

    rated = Column(String, nullable=True)

    genres = Column(String, nullable=True)

    characters = Column(String, nullable=True)

    favs = Column(Integer, nullable=True)

    follows = Column(Integer, nullable=True)

    # TODO: Parse date?
    published = Column(String, nullable=True)
