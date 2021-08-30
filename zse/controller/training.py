from zse import query
from zse.common import auth
from zse.common.constants import TrainingType, ControllerLogMessage, CertificationType
from zse.common.flask import app, error
from zse.model.training import TrainingStageRequirement, ControllerTrainingStageRequirement
from zse.util import training as training_util
from flask import jsonify, request


@app.get('/training/objective/student/<cid>')
@auth.guard([auth.Permission.INS, auth.Permission.MTR])
def get_student_objectives(cid: int):
    data = [{
        'student_cid': obj.student_cid,
        'objective_id': obj.objective_id,
        'is_policy_read': obj.is_policy_read,
        'is_focus_area': obj.is_focus_area,
        'is_completed': obj.is_completed
    } for obj in query.training.get_training_objectives_for_cid(cid)]
    return jsonify(data)


@app.get('/training/objective/me')
def get_my_objectives():
    data = [{
        'student_cid': obj.student_cid,
        'objective_id': obj.objective_id,
        'is_policy_read': obj.is_policy_read,
        'is_focus_area': obj.is_focus_area,
        'is_completed': obj.is_completed
    } for obj in query.training.get_training_objectives_for_cid(auth.get_user_id())]
    return jsonify(data)


@app.post('/training/debrief')
@auth.guard([auth.Permission.INS, auth.Permission.MTR])
def create_debrief():
    training_session_data = {
        'student_cid': request.json.get('student_cid'),
        'instructor_cid': auth.get_user_id(),
        'training_type': TrainingType.get(request.json.get('training_type')),
        'training_stage_key': request.json.get('training_stage_key'),
        'score': request.json.get('score'),
        'comments': request.json.get('comments'),
        'notes': request.json.get('notes'),
        'duration': request.json.get('duration'),
        'movements': request.json.get('movements'),
        'is_private': request.json.get('is_private'),
        'is_ots_ready': request.json.get('is_ots_ready'),
        'is_pass': request.json.get('is_pass'),
        'session_date': request.json.get('session_date')
    }
    objectives_data = [{
        'objective_id': objective.get('objective_id'),
        'is_lecture': objective.get('is_lecture'),
        'is_observed': objective.get('is_observed'),
        'is_focus_area': objective.get('is_focus_area'),
        'score': objective.get('score')
    } for objective in request.json.get('training_objectives', [])]
    query.training.insert_training_session(training_session_data, objectives_data)
    query.controller.log(request.json.get('student_cid'), auth.get_user_id(),
                         ControllerLogMessage.TRAINING_DEBRIEF_CREATE)
    return jsonify(message='Success')


@app.put('/training/certification/<cid>')
@auth.guard(auth.Permission.INS)
def training_set_certified_positions(cid: int):
    instructor_cid = auth.get_user_id()
    positions = {
        'delivery': CertificationType.get(request.json.get('delivery')),
        'ground': CertificationType.get(request.json.get('ground')),
        'tower': CertificationType.get(request.json.get('tower')),
        'approach': CertificationType.get(request.json.get('approach')),
        'center': CertificationType.get(request.json.get('center')),
    }
    controller = query.controller.get_controller_by_cid(cid)
    rejected = training_util.check_position_certifications(controller.Controller, positions)
    if rejected:
        error('Invalid position certifications: %r' % rejected, 400)
    positions_updated = training_util.get_positions_updated(controller.ControllerPositions, positions)
    query.training.set_positions_for_cid(cid, positions)
    for pos in positions_updated:
        cert = positions.get(pos)
        query.controller.log(cid, instructor_cid,
                             ControllerLogMessage.TRAINING_POSITION_CERTIFIED,
                             (pos, cert.name if cert is not None else None))
    return jsonify(message='Success')


@app.get('/training/stages')
def get_training_stages():
    requirement: TrainingStageRequirement
    data = [{
        'training_stage_key': stage.training_stage_key,
        'name': stage.name,
        'required_rating': stage.required_rating,
        'is_visitor_path': stage.is_visitor_path,
        'is_home_path': stage.is_home_path,
        'requirements': [
            {
                'training_stage_requirement_id': requirement.training_stage_requirement_id,
                'name': requirement.name,
                'requirement_type': requirement.requirement_type,
                'reference_id': requirement.reference_id,
                'reference_value': requirement.reference_value
            } for requirement in stage.requirements
        ]
    } for stage in query.training.get_training_stages()]
    return jsonify(data)


@app.get('/training/stages/<cid>')
@auth.guard([auth.Permission.MTR, auth.Permission.INS, auth.Permission.TA])
def get_training_stages_by_cid(cid: int):
    requirement: ControllerTrainingStageRequirement
    data = [{
        'training_stage_key': stage.training_stage.training_stage_key,
        'name': stage.training_stage.name,
        'required_rating': stage.training_stage.required_rating,
        'is_visitor_path': stage.training_stage.is_visitor_path,
        'is_home_path': stage.training_stage.is_home_path,
        'is_completed': stage.is_completed,
        'completed_date': stage.completed_date,
        'requirements': [
            {
                'training_stage_requirement_id': requirement.training_stage_requirement.training_stage_requirement_id,
                'name': requirement.training_stage_requirement.name,
                'requirement_type': requirement.training_stage_requirement.requirement_type,
                'reference_id': requirement.training_stage_requirement.reference_id,
                'reference_value': requirement.training_stage_requirement.reference_value,
                'is_completed': requirement.is_completed,
                'completed_date': requirement.completed_date
            } for requirement in stage.requirements
        ]
    } for stage in query.training.get_controller_training_stages_by_cid(cid)]
    return jsonify(data)
