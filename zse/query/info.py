from zse.common import db
from zse.model.controller import Controller
from zse.model.info import News, NOTAM
from zse.model.staff import Staff
from sqlalchemy import and_


def get_recent_news(num_records):
    q = db.session.query(News)
    q = q.where(News.deleted.is_(False))
    q = q.order_by(News.post_date.desc())
    q = q.limit(num_records)
    return q.all()


def get_notams():
    q = db.session.query(NOTAM)
    q = q.where(NOTAM.active.is_(True))
    return q.all()


def get_staff():
    q = db.session.query(Controller, Staff)
    q = q.join(Staff, Controller.vatsim_cid == Staff.vatsim_cid)
    return q.all()
