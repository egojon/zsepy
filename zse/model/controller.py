from zse.common import db
from zse.common.constants import ControllerRating, ControllerLOAStatus, CertificationType
from sqlalchemy import Column, String, Integer, Boolean, Enum, Date, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


class Controller(db.Base):
    __tablename__ = 'controller'
    vatsim_cid = Column(Integer, primary_key=True, autoincrement=False)
    initials = Column(String(4), nullable=True, unique=True)
    rating = Column(String(80), nullable=False)
    first_name = Column(String(120))
    last_name = Column(String(120))
    display_name = Column(String(240))
    email_address = Column(String(240))
    member_since = Column(Date, default=None)
    facility = Column(String(20))
    is_home = Column(Boolean, default=False)
    is_visitor = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    loa = relationship("ControllerLOA", back_populates="controller", lazy="joined", uselist=False)
    positions = relationship("ControllerPositions", back_populates="controller", lazy="joined", uselist=False)
    discord = relationship("ControllerDiscord", back_populates="controller", lazy="joined", uselist=False)
    inactivity = relationship("ControllerInactivity", back_populates="controller", lazy="joined", uselist=False)
    staff = relationship("Staff", back_populates="controller", lazy="joined", uselist=False)


class ControllerLog(db.Base):
    __tablename__ = 'controller_log'
    log_id = Column(Integer, primary_key=True)
    controller_cid = Column(Integer, ForeignKey(Controller.vatsim_cid), nullable=False)
    admin_cid = Column(Integer)
    log_date = Column(DateTime)
    message = Column(Text)


class ControllerLOA(db.Base):
    __tablename__ = 'controller_loa'
    vatsim_cid = Column(Integer, ForeignKey(Controller.vatsim_cid), primary_key=True, autoincrement=False)
    reason = Column(String(240))
    request_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String(80), default=ControllerLOAStatus.PENDING)

    controller = relationship("Controller", back_populates="loa")


class ControllerPositions(db.Base):
    __tablename__ = 'controller_positions'
    vatsim_cid = Column(Integer, ForeignKey(Controller.vatsim_cid), primary_key=True, autoincrement=False)
    delivery = Column(String(80), default=None)
    ground = Column(String(80), default=None)
    tower = Column(String(80), default=None)
    approach = Column(String(80), default=None)
    center = Column(String(80), default=None)

    controller = relationship("Controller", back_populates="positions")


class ControllerDiscord(db.Base):
    __tablename__ = 'controller_discord'
    vatsim_cid = Column(Integer, ForeignKey(Controller.vatsim_cid), primary_key=True, autoincrement=False)
    discord_id = Column(String(40), nullable=False, unique=True)
    notifications = Column(Boolean, default=True)
    on_voice_channel = Column(Boolean, default=False)

    controller = relationship("Controller", back_populates="discord")


class ControllerInactivity(db.Base):
    __tablename__ = 'controller_inactivity'
    vatsim_cid = Column(Integer, ForeignKey(Controller.vatsim_cid), primary_key=True, autoincrement=False)
    is_inactivity_exempt = Column(Boolean, default=False)
    inactivity_strikes = Column(Integer, default=0)
    inactivity_start = Column(DateTime)

    controller = relationship("Controller", back_populates="inactivity")


class ControllerProfile(db.Base):
    __tablename__ = 'controller_profile'
    vatsim_cid = Column(Integer, primary_key=True, autoincrement=False)
    timezone = Column(String(120))


class ControllerDocumentRead(db.Base):
    __tablename__ = 'controller_document_read'
    vatsim_cid = Column(Integer, primary_key=True)
    document_id = Column(Integer, primary_key=True)
    first_read = Column(DateTime)
    last_read = Column(DateTime)
    is_latest_version_read = Column(Boolean, default=False, nullable=False)

