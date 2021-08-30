from zse.common import db
from zse.query import content, controller, info, navigation, staff, training


def add(record):
    db.session.add(record)


def save():
    db.session.commit()
