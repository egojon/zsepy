from zse.common import db
from sqlalchemy import Column, String, Text


class EmailTemplate(db.Base):
    __tablename__ = 'email_template'
    template_id = Column(String(240), primary_key=True, nullable=False)
    template_name = Column(String(240), nullable=False)
    additional_cc_list = Column(Text, nullable=False, default='')
    content_plaintext = Column(Text, nullable=False)
    content_html = Column(Text, nullable=False)
