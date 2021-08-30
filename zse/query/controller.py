from zse.common import cache, db
from zse.common.constants import ControllerLOAStatus, ControllerRating, ControllerLogMessage
from zse.model.controller import Controller, ControllerLOA, ControllerLog, ControllerPositions, ControllerDocumentRead
from zse.model.staff import Staff
import datetime
from sqlalchemy import and_, or_
from typing import List


def get_controller_by_cid(cid: int):
    q = db.session.query(Controller, ControllerLOA, ControllerPositions)
    q = q.join(ControllerLOA, and_(Controller.vatsim_cid == ControllerLOA.vatsim_cid,
                                   ControllerLOA.status == ControllerLOAStatus.ACTIVE), isouter=True)
    q = q.join(ControllerPositions, Controller.vatsim_cid == ControllerPositions.vatsim_cid, isouter=True)
    q = q.where(Controller.vatsim_cid == cid)
    return q.first()


def get_active_controllers():
    q = db.session.query(Controller)
    q = q.where(Controller.is_active)
    return q.all()


def get_roster_controllers():
    q = db.session.query(Controller)
    q = q.where(or_(Controller.is_home, Controller.is_visitor))
    return q.all()


def get_controllers():
    q = db.session.query(Controller)
    return q.all()


def log(cid, admin_cid, message: ControllerLogMessage, data=()):
    record = ControllerLog()
    record.controller_cid = cid
    record.admin_cid = admin_cid
    record.message = message.value % tuple(data)
    db.session.add(record)
    db.session.commit()


@cache.cached
def get_documents_read_by_cid(cid: int) -> List[ControllerDocumentRead]:
    q = db.session.query(ControllerDocumentRead)
    q = q.where(ControllerDocumentRead.vatsim_cid == cid)
    return q.all()


def get_document_read_by_ids(cid: int, document_id: int):
    q = db.session.query(ControllerDocumentRead)
    q = q.where(ControllerDocumentRead.vatsim_cid == cid)
    q = q.where(ControllerDocumentRead.document_id == document_id)
    return q.first()


def set_document_read(cid: int, document_id: int):
    record = get_document_read_by_ids(cid, document_id)
    if record is None:
        record = ControllerDocumentRead()
        record.vatsim_cid = cid
        record.document_id = document_id
        record.first_read = datetime.datetime.now()
        db.session.add(record)
    record.last_read = datetime.datetime.now()
    record.is_latest_version_read = True
    db.session.commit()
