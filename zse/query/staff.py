from zse.common import db
from zse.model.staff import Staff


def get_staff_by_cid(cid):
    q = db.session.query(Staff)
    q = q.where(Staff.vatsim_cid == cid)
    return q.first()
