from zse.model.controller import Controller
from zse.types.vatusa import VATUSAUserInfo, VATUSAVisitingFacilityInfo
from zse import query
from zse import util
from typing import Dict, List


def run():
    controllers: List[Controller] = query.controller.get_controllers()
    controllers: Dict[int, Controller] = {controller.vatsim_cid: controller for controller in controllers}
    vatusa_roster: List[VATUSAUserInfo] = util.vatusa.get_facility_roster()
    vatusa_roster: Dict[int, VATUSAUserInfo] = {info.cid: info for info in vatusa_roster}

    vatusa_roster_loop(controllers, vatusa_roster)
    local_roster_loop(controllers, vatusa_roster)
    query.save()  # Don't want to save in the loop for performance reasons


def vatusa_roster_loop(controllers: Dict[int, Controller], vatusa_roster: Dict[int, VATUSAUserInfo]):
    for cid, vatusa_info in vatusa_roster.items():
        if cid not in controllers:
            # This case should only happen for new controllers coming to ZSE for the first time
            controller = util.controller.add_controller(cid, vatusa_info=vatusa_info)
            controllers[cid] = controller  # Inject controller into the dict
        controller = controllers.get(cid)
        if vatusa_info.flag_homecontroller:
            # Home Controller
            if not controller.is_home:
                util.controller.setup_home_controller(controller)
        else:
            # Visitor
            if not controller.is_visitor:
                # Visitor has been removed from our roster
                util.vatusa.remove_visitor_from_roster(controller.vatsim_cid)
        # Both Home and Visitor
        util.controller.update_controller_info_from_vatusa(controller, vatusa_info)


def local_roster_loop(controllers: Dict[int, Controller], vatusa_roster: Dict[int, VATUSAUserInfo]):
    for cid, controller in controllers.items():
        vatusa_info = vatusa_roster.get(cid)
        if controller.is_home:
            # Home Controller
            if vatusa_info is None:
                # Doesn't exist on the VATUSA roster -- remove them
                util.controller.remove_controller(controller)
                # TODO - Notify ATM, DATM that user was removed from the roster
        elif controller.is_visitor:
            # Visitor Controller
            if vatusa_info is None:
                # Visitor isn't on VATUSA roster -- add them
                util.vatusa.add_visitor_to_roster(cid)
            pass
        else:
            pass
        # All Controllers


if __name__ == '__main__':
    run()
