from zse.common.constants import TrainingStage
from zse.model.training import TrainingStage as TrainingStageModel, ControllerTrainingStageRequirement, \
    ControllerTrainingStage
from zse import query, util
import datetime


def run():
    training_stage_keys = [TrainingStage.MINOR_GROUND, TrainingStage.MAJOR_GROUND,
                           TrainingStage.MINOR_TOWER, TrainingStage.MAJOR_TOWER,
                           TrainingStage.MINOR_APPROACH, TrainingStage.MAJOR_APPROACH,
                           TrainingStage.CENTER]
    training_stages = query.training.get_training_stages()
    training_stages = {ts.training_stage_key: ts for ts in training_stages}
    controllers = query.controller.get_active_controllers()
    controllers_training_stages = query.training.get_controller_training_stages()
    for controller in controllers:
        controller_training_stages = {cts.training_stage_key: cts for cts in controllers_training_stages
                                      if cts.vatsim_cid == controller.vatsim_cid}
        for ts_key in training_stage_keys:
            training_stage: TrainingStageModel = training_stages.get(ts_key.name)
            if controller.rating.value < training_stage.required_rating.value:
                # Rating not high enough - Skip training stage
                continue
            if controller.is_visitor and not training_stage.is_visitor_path:
                # Not for visitors - Skip training stage
                continue
            if not controller.is_visitor and not training_stage.is_home_path:
                # Not for home - Skip training stage
                continue
            controller_training_stage: ControllerTrainingStage = controller_training_stages.get(ts_key.name)
            if controller_training_stage is None:
                controller_training_stage = query.training.insert_controller_training_stage(
                    controller.vatsim_cid, training_stage)
            if not controller_training_stage.is_allowed_to_train:
                # Check if requirements are completed
                is_any_requirement_pending = False
                req: ControllerTrainingStageRequirement
                for req in controller_training_stage.requirements:
                    if req.is_completed:
                        # req is already completed - continue
                        continue
                    # Check if requirement is completed
                    util.training.check_training_stage_requirement_complete(req)
                    if not req.is_completed:
                        is_any_requirement_pending = True
                        break
                if not is_any_requirement_pending:
                    controller_training_stage.is_allowed_to_train = True
                    controller_training_stage.requirements_completed_date = datetime.datetime.now()
    query.save()


if __name__ == '__main__':
    run()
