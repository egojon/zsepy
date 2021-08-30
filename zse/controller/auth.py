from zse.common import auth
from zse.common.constants import Permission
from zse.common.flask import app
from flask import jsonify


@app.get('/auth/test/private')
@auth.guard([Permission.ADM])
def test_private():
    return jsonify({
        'thereisacow': 1337
    })


@app.get('/auth/test/key/<cid>')
def test_key(cid):
    data = {
        'jwt': auth.make_jwt(cid)
    }
    return jsonify(data)
