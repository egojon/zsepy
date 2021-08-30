from zse import query
from zse.common import auth
from zse.common.flask import app
from flask import jsonify


@app.get('/documents')
def documents():
    data = [{
        'document_id': doc.Document.document_id,
        'document_category_id': doc.DocumentCategory.document_category_id,
        'document_category_name': doc.DocumentCategory.name,
        'name': doc.Document.name,
        'google_document_id': doc.Document.google_document_id
    } for doc in query.content.get_document_list()]
    return jsonify(data)


@app.put('/document/read/<document_id>')
def put_document_read(document_id):
    cid = auth.get_user_id()
    # Verify document exists
    document = query.content.get_document_by_id(document_id)
    if document is not None:
        query.controller.set_document_read(cid, document_id)
    return jsonify(message='Success')


@app.get('/external_links')
def external_links():
    data = [{
        'type': link.type,
        'name': link.name,
        'link': link.link
    } for link in query.content.get_external_links()]
    return jsonify(data)
