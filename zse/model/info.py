from zse.common import db
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text


class News(db.Base):
    __tablename__ = 'news'
    news_id = Column(Integer, primary_key=True)
    poster_cid = Column(Integer)
    message = Column(String(240), nullable=False)
    link = Column(Text)
    post_date = Column(DateTime)
    deleted = Column(Boolean)


class NOTAM(db.Base):
    __tablename__ = 'notam'
    notam_id = Column(Integer, primary_key=True)
    poster_cid = Column(Integer)
    message = Column(String(240), nullable=False)
    link = Column(Text)
    post_date = Column(DateTime)
    active = Column(Boolean)
