from zse.common import db
from zse.model.navigation import PreferredRoute


def get_preferred_routes():
    q = db.session.query(PreferredRoute)
    return q.all()
