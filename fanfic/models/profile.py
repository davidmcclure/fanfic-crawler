

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from .base import Base


# TODO: Set required metadata fields.
class Profile(Base):

    __tablename__ = 'profile'

    book_id = Column(
        ForeignKey('book_id.book_id'),
        primary_key=True,
        autoincrement=False,
    )

    title = Column(String, nullable=True)

    user_id = Column(Integer, nullable=True)

    username = Column(String, nullable=True)

    summary = Column(String, nullable=True)

    rating = Column(String, nullable=True)

    language = Column(String, nullable=True)

    genres = Column(String, nullable=True)

    characters = Column(String, nullable=True)

    favorites = Column(Integer, nullable=True)

    follows = Column(Integer, nullable=True)

    published = Column(DateTime, nullable=True)

    updated = Column(DateTime, nullable=True)
