from zse.common import db
from zse.common.constants import ExternalLinkType
from sqlalchemy import Column, String, Integer, Boolean, Enum, Date, DateTime, Text


class Document(db.Base):
    __tablename__ = 'document'
    document_id = Column(Integer, primary_key=True)
    document_category_id = Column(Integer)
    name = Column(String(120))
    google_document_id = Column(String(240))
    created_by_cid = Column(Integer)
    created_date = Column(DateTime)
    updated_by_cid = Column(Integer)
    updated_date = Column(DateTime)


class DocumentCategory(db.Base):
    __tablename__ = 'document_category'
    document_category_id = Column(Integer, primary_key=True)
    name = Column(String(120))
    is_public = Column(Boolean, default=False)
    show_instructor = Column(Boolean, default=False)
    show_mentor = Column(Boolean, default=False)
    show_staff = Column(Boolean, default=False)


class ExternalLink(db.Base):
    __tablename__ = 'external_link'
    external_link_id = Column(Integer, primary_key=True)
    type = Column(String(80), nullable=False)
    name = Column(String(240), nullable=False)
    link = Column(Text, nullable=False)
