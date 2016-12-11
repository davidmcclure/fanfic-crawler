

from datetime import datetime as dt

from sqlalchemy import Column, DateTime


class ScrapedItem:

    scraped_at = Column(DateTime, default=dt.utcnow, nullable=False)
