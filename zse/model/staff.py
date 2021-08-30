from zse.common import db
from zse.common.constants import StaffPosition
from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey, String
from sqlalchemy.orm import relationship


class Staff(db.Base):
    __tablename__ = 'staff'
    vatsim_cid = Column(Integer, ForeignKey("controller.vatsim_cid"), primary_key=True, autoincrement=False)
    staff_position = Column(String(80))
    is_admin = Column(Boolean, default=False, nullable=False)
    is_mentor = Column(Boolean, default=False, nullable=False)
    is_instructor = Column(Boolean, default=False, nullable=False)
    is_training_administrator = Column(Boolean, default=False, nullable=False)
    is_facility_engineer = Column(Boolean, default=False, nullable=False)
    is_event_coordinator = Column(Boolean, default=False, nullable=False)

    controller = relationship("Controller", back_populates="staff")
