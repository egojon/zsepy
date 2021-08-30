from zse.common import db
from zse.model.controller import ControllerPositions
from zse.model.training import (TrainingSession, TrainingSessionObjective, ControllerTrainingStage, TrainingStage,
                                TrainingStageRequirement, ControllerTrainingStageRequirement)
from typing import List


def get_training_stages() -> List[TrainingStage]:
    q = db.session.query(TrainingStage)
    return q.all()


def get_controller_training_stages() -> List[ControllerTrainingStage]:
    q = db.session.query(ControllerTrainingStage)
    return q.all()


def get_controller_training_stages_by_cid(cid: int) -> List[ControllerTrainingStage]:
    q = db.session.query(ControllerTrainingStage)
    q = q.where(ControllerTrainingStage.vatsim_cid == cid)
    return q.all()


def insert_controller_training_stage(cid: int, stage: TrainingStage):
    cts = ControllerTrainingStage()
    cts.vatsim_cid = cid
    cts.training_stage_key = stage.training_stage_key

    creqs = []
    req: TrainingStageRequirement
    for req in stage.requirements:
        creq = ControllerTrainingStageRequirement()
        creq.vatsim_cid = cid
        creq.training_stage_requirement_id = req.training_stage_requirement_id
        creqs.append(creq)

    cts.requirements = creqs
    db.session.add(cts)
    db.session.add_all(creqs)
    db.session.commit()
    return cts


def get_training_objectives_for_cid(cid: int):
    q = db.session.query(ControllerTrainingObjective)
    q = q.where(ControllerTrainingObjective.student_cid == cid)
    return q.all()


def insert_training_session(session_data: dict, objectives_data: List[dict]):
    training_session: TrainingSession = db.build(session_data, TrainingSession)
    objectives: List[TrainingSessionObjective] = [db.build(obj, TrainingSessionObjective) for obj in objectives_data]
    db.session.add(training_session)
    db.session.commit()
    for obj in objectives:
        obj.training_session_id = training_session.training_session_id
    db.session.add_all(objectives)
    db.session.commit()


def get_training_sessions_by_student_cid(cid: int) -> List[TrainingSession]:
    q = db.session.query(TrainingSession)
    q = q.where(TrainingSession.student_cid == cid)
    return q.all()


def get_training_sessions_by_instructor_cid(cid: int) -> List[TrainingSession]:
    q = db.session.query(TrainingSession)
    q = q.where(TrainingSession.instructor_id)
    return q.all()


def set_positions_for_cid(cid: int, positions: dict):
    q = db.session.query(ControllerPositions)
    q = q.where(ControllerPositions.vatsim_cid == cid)
    record: ControllerPositions = q.first()
    record.delivery = positions.get('delivery')
    record.ground = positions.get('ground')
    record.tower = positions.get('tower')
    record.approach = positions.get('approach')
    record.center = positions.get('center')
    db.session.commit()


def get_training_stage_requirement(training_stage_requirement_id) -> TrainingStageRequirement:
    q = db.session.query(TrainingStageRequirement)
    q = q.where(TrainingStageRequirement.training_stage_requirement_id == training_stage_requirement_id)
    return q.first()


def save_training_stage_requirement(data: dict):
    if 'training_stage_requirement_id' in data:
        requirement = get_training_stage_requirement(data.get('training_stage_requirement_id'))
    else:
        # Create new record
        requirement = TrainingStageRequirement()
        requirement.training_stage_key = data.get('training_stage_key')
        requirement.requirement_type = data.get('requirement_type')
    requirement.name = data.get('name')
    requirement.reference_id = data.get('reference_id')
    requirement.reference_value = data.get('reference_value')
