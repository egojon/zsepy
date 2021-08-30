from zse.common import db
from sqlalchemy import Column, String, Integer, Boolean, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class TrainingStage(db.Base):
    __tablename__ = 'training_stage'
    training_stage_key = Column(String(80), primary_key=True)
    name = Column(String(120))
    required_rating = Column(String(80), nullable=False)
    is_visitor_path = Column(Boolean, default=False, nullable=False)
    is_home_path = Column(Boolean, default=False, nullable=False)

    requirements = relationship("TrainingStageRequirement", lazy="joined")


class TrainingStageRequirement(db.Base):
    __tablename__ = 'training_stage_requirement'
    training_stage_requirement_id = Column(Integer, primary_key=True)
    training_stage_key = Column(String(80), ForeignKey(TrainingStage.training_stage_key), nullable=False)
    name = Column(String(240), nullable=False)
    requirement_type = Column(String(80), nullable=False)
    reference_id = Column(Integer)
    reference_value = Column(String(240))


class TrainingStageObjective(db.Base):
    __tablename__ = 'training_stage_objective'
    training_stage_objective_id = Column(Integer, primary_key=True)
    training_stage_key = Column(String(80), ForeignKey(TrainingStage.training_stage_key), nullable=False)
    session_number = Column(Integer, nullable=False)
    name = Column(String(240), nullable=False)
    description = Column(Text)
    policy_reference = Column(String(100))
    policy_link = Column(Text)
    display_order = Column(Integer, nullable=False)


class ControllerTrainingStage(db.Base):
    __tablename__ = 'controller_training_stage'
    vatsim_cid = Column(Integer, primary_key=True, autoincrement=False)
    training_stage_key = Column(String(80), ForeignKey(TrainingStage.training_stage_key),
                                primary_key=True, autoincrement=False)
    is_allowed_to_train = Column(Boolean, default=False, nullable=False)
    requirements_completed_date = Column(DateTime, default=None)
    is_completed = Column(Boolean, default=False, nullable=False)
    completed_date = Column(DateTime, default=None)

    training_stage = relationship("TrainingStage")
    requirements = relationship("ControllerTrainingStageRequirement", back_populates="controller_training_stage",
                                lazy="joined")


class ControllerTrainingStageRequirement(db.Base):
    __tablename__ = 'controller_training_stage_requirement'
    vatsim_cid = Column(Integer, ForeignKey(ControllerTrainingStage.vatsim_cid), primary_key=True, autoincrement=False)
    training_stage_requirement_id = Column(Integer, ForeignKey(TrainingStageRequirement.training_stage_requirement_id),
                                           primary_key=True, autoincrement=False)
    is_completed = Column(Boolean, default=False, nullable=False)
    completed_date = Column(DateTime, default=None)

    controller_training_stage = relationship("ControllerTrainingStage", back_populates="requirements", lazy="joined")
    training_stage_requirement = relationship("TrainingStageRequirement", lazy="joined")


class TrainingSession(db.Base):
    __tablename__ = 'training_session'
    training_session_id = Column(Integer, primary_key=True)
    student_cid = Column(Integer, nullable=False)
    instructor_cid = Column(Integer, nullable=False)
    training_type = Column(String(80), nullable=False)
    training_stage_key = Column(String(80), ForeignKey(TrainingStage.training_stage_key))
    score = Column(Integer)
    comments = Column(String(240))
    notes = Column(Text)
    duration = Column(Integer)  # Minutes
    movements = Column(Integer, default=0, nullable=False)
    is_private = Column(Boolean, default=False, nullable=False)
    is_ots_ready = Column(Boolean, default=False, nullable=False)
    is_pass = Column(Boolean, default=None)
    session_date = Column(Date)


class TrainingSessionObjective(db.Base):
    __tablename__ = 'training_session_objective'
    training_session_objective_id = Column(Integer, primary_key=True)
    training_session_id = Column(Integer, nullable=False)
    training_stage_objective_id = Column(Integer, ForeignKey(TrainingStageObjective.training_stage_objective_id),
                                         nullable=False)
    is_lecture = Column(Boolean)
    is_observed = Column(Boolean)
    is_focus_area = Column(Boolean)
    is_complete = Column(Boolean)
    score = Column(Integer)


class TrainingRequest(db.Base):
    __tablename__ = 'training_request'
    training_request_id = Column(Integer, primary_key=True)
    student_cid = Column(Integer, ForeignKey("controller.vatsim_cid"), nullable=False)
    training_stage_key = Column(String(80), ForeignKey(TrainingStage.training_stage_key), nullable=False)
    window_start_date = Column(DateTime, nullable=False)
    window_end_date = Column(DateTime, nullable=False)
    is_accepted = Column(Boolean, default=False, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)
    is_cancelled = Column(Boolean, default=False, nullable=False)
    instructor_cid = Column(Integer, ForeignKey("controller.vatsim_cid"))
    training_session_id = Column(Integer, ForeignKey(TrainingSession.training_session_id))
    scheduled_start_date = Column(DateTime)
    scheduled_end_date = Column(DateTime)
