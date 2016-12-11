

from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from .base import Base


class Metadata(Base):

    __tablename__ = 'metadata'

    book_id = Column(
        Integer,
        ForeignKey('metadata_html.book_id'),
        primary_key=True,
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

    published = Column(Date, nullable=True)

    updated = Column(Date, nullable=True)
