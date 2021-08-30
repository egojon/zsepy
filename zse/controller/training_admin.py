from zse import query
from zse.common import auth
from zse.common.constants import TrainingType, TrainingObjectiveType, ControllerLogMessage, CertificationType, \
    ControllerRating
from zse.common.flask import app, error
from zse.util import training as training_util
from flask import jsonify, request


@app.post('/admin/training/stage/requirement')
@auth.guard(auth.Permission.TA)
def create_training_stage_requirement():
    requirement = {
        'training_stage_key': request.json.get('training_stage_key'),
        'name': request.json.get('name'),
        'requirement_type': request.json.get('requirement_type'),
        'reference_id': request.json.get('reference_id'),
        'reference_value': request.json.get('reference_value')
    }
    # TODO - Validate input
    query.training.save_training_stage_requirement(requirement)
    return jsonify(message='Success')


@app.put('/admin/training/stage/requirement')
@auth.guard(auth.Permission.TA)
def update_training_stage_requirement():
    requirement = {
        'training_stage_requirement_id': request.json.get('training_stage_requirement_id'),
        'training_stage_key': request.json.get('training_stage_key'),
        'name': request.json.get('name'),
        'requirement_type': request.json.get('requirement_type'),
        'reference_id': request.json.get('reference_id'),
        'reference_value': request.json.get('reference_value')
    }
    # TODO - Validate input
    query.training.save_training_stage_requirement(requirement)
    return jsonify(message='Success')
