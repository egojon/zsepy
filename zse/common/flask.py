from flask import Flask, request, make_response, jsonify, abort
from flask_cors import CORS
from zse.common import db
import enum
import json

app = Flask(__name__)
CORS(app)


def error(msg, status_code):
    abort(make_response(jsonify(error=msg), status_code))


@app.before_request
def _before_request():
    db.start_session()
    return


@app.after_request
def _after_request(response):
    db.end_session()
    return response


class JSONEncoderImproved(json.JSONEncoder):
    '''
    Used to help jsonify numpy arrays or lists that contain numpy data types.
    '''
    def default(self, obj):
        if isinstance(obj, enum.Enum):
            return obj.name
        else:
            return super().default(obj)


app.json_encoder = JSONEncoderImproved
