from datetime import datetime

from database import Base
from sqlalchemy import Column, DateTime, Integer, String


class ShortenedURL(Base):
    __tablename__ = "shortened_url"

    id = Column(Integer, primary_key=True)
    url = Column(String(256))
    url_path = Column(String(10))
    created_date = Column(DateTime, default=datetime.now)
