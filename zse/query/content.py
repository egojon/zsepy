from zse.common import db
from zse.model.content import Document, DocumentCategory, ExternalLink


def get_document_list():
    # TODO: Support more than just public documents -- This requires auth implementation
    q = db.session.query(Document, DocumentCategory)
    q = q.join(DocumentCategory, Document.document_category_id == DocumentCategory.document_category_id)
    q = q.where(DocumentCategory.is_public.is_(True))
    return q.all()


def get_document_by_id(document_id: int):
    # TODO: Support more than just public documents -- This requires auth implementation
    q = db.session.query(Document, DocumentCategory)
    q = q.join(DocumentCategory, Document.document_category_id == DocumentCategory.document_category_id)
    q = q.where(DocumentCategory.is_public.is_(True))
    q = q.where(Document.document_id == document_id)
    return q.first


def get_external_links():
    q = db.session.query(ExternalLink)
    return q.all()
