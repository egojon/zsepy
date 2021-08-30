from zse import query
from zse.common.constants import ControllerRating, CertificationType, TrainingStageRequirementType, TrainingType
from zse.model.controller import Controller, ControllerPositions, ControllerDocumentRead
from zse.model.training import ControllerTrainingStageRequirement, TrainingStageRequirement
import datetime
from typing import Dict, List


def get_positions_updated(record: ControllerPositions, positions: dict):
    ret = []
    for pos, value in positions.items():
        current = getattr(record, pos)
        if current != value:
            ret.append(pos)
    return ret


def check_position_certifications(controller: Controller, positions: dict):
    allowed = get_allowed_positions_by_rating(controller.rating)
    rejected = []
    for k, v in positions.items():
        if v is not None and v not in allowed.get(k):
            rejected.append(k)
    return rejected


def get_allowed_positions_by_rating(rating: ControllerRating):
    allowed = {
        'delivery': [],
        'ground': [],
        'tower': [],
        'approach': [],
        'center': [],
    }
    if rating == ControllerRating.OBS:
        allowed = {
            'delivery': [CertificationType.TRAIN],
            'ground': [CertificationType.TRAIN],
            'tower': [],
            'approach': [],
            'center': [],
        }
    elif rating == ControllerRating.S1:
        allowed = {
            'delivery': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'ground': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'tower': [CertificationType.TRAIN, CertificationType.SOLO, CertificationType.OTS],
            'approach': [],
            'center': [],
        }
    elif rating == ControllerRating.S2:
        allowed = {
            'delivery': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'ground': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'tower': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'approach': [CertificationType.TRAIN, CertificationType.SOLO, CertificationType.OTS],
            'center': [],
        }
    elif rating == ControllerRating.S3:
        allowed = {
            'delivery': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'ground': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'tower': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'approach': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'center': [CertificationType.TRAIN, CertificationType.SOLO, CertificationType.OTS],
        }
    elif rating in [ControllerRating.C1, ControllerRating.C3,
                    ControllerRating.I1, ControllerRating.I3,
                    ControllerRating.SUP, ControllerRating.ADM]:
        allowed = {
            'delivery': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'ground': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'tower': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'approach': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
            'center': [CertificationType.TRAIN, CertificationType.MINOR, CertificationType.FULL],
        }
    return allowed


def check_training_stage_requirement_complete(ctsr: ControllerTrainingStageRequirement):
    requirement: TrainingStageRequirement = ctsr.training_stage_requirement
    check = False
    # Switch to call breakout checkers
    if requirement.requirement_type == TrainingStageRequirementType.TRAINING_SESSIONS:
        check = _check_training_sessions_requirement(ctsr, requirement)
    elif requirement.requirement_type == TrainingStageRequirementType.DOCUMENT_READ:
        check = _check_document_read_requirement(ctsr, requirement)
    elif requirement.requirement_type == TrainingStageRequirementType.CONTROLLING_HOURS:
        pass
    elif requirement.requirement_type == TrainingStageRequirementType.VATUSA_EXAM:
        pass
    elif requirement.requirement_type == TrainingStageRequirementType.VATUSA_CBT:
        pass
    elif requirement.requirement_type == TrainingStageRequirementType.CALENDAR_DAYS:
        pass

    # After all checkers are complete
    if check:
        ctsr.is_completed = True
        ctsr.completed_date = datetime.datetime.now()


def _check_training_sessions_requirement(
        ctsr: ControllerTrainingStageRequirement, requirement: TrainingStageRequirement) -> bool:
    training_sessions = query.training.get_training_sessions_by_student_cid(ctsr.vatsim_cid)
    filtered_sessions = [session for session in training_sessions
                         if session.training_stage_key == requirement.training_stage_key
                         and session.training_type not in [TrainingType.NOTE, TrainingType.WORKSHEET]]
    return len(filtered_sessions) >= int(requirement.reference_value)


def _check_document_read_requirement(
        ctsr: ControllerTrainingStageRequirement, requirement: TrainingStageRequirement) -> bool:
    documents_read = query.controller.get_documents_read_by_cid(ctsr.vatsim_cid)
    documents_read_dict = {dr.document_id: dr for dr in documents_read}
    dr: ControllerDocumentRead = documents_read_dict.get(requirement.reference_id)
    return dr.is_latest_version_read if dr is not None else False


