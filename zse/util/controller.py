from zse.common.constants import ControllerRating
from zse.model.controller import Controller, ControllerPositions
from zse.types.vatusa import VATUSAUserInfo
from zse import query
from zse import util
import datetime


def add_controller(cid: int, *, vatsim_info=None, vatusa_info=None) -> Controller:
    controller = query.controller.get_controller_by_cid(cid)
    if controller is not None:
        # Don't need to add controller again if they already exist
        return controller
    if vatsim_info is None:
        vatsim_info = util.vatsim.get_info_from_cid(cid)
    if vatusa_info is None:
        vatusa_info = util.vatusa.get_user_from_cid(cid)
    if vatsim_info is None:
        # Invalid CID
        return None
    controller = Controller()
    controller.vatsim_cid = vatsim_info.id  # Only set vatsim_cid on initial creation
    controller.first_name = vatusa_info.fname if vatusa_info is not None else vatsim_info.name_first
    controller.last_name = vatusa_info.lname if vatusa_info is not None else vatsim_info.name_last
    controller.display_name = '%s %s' % (controller.first_name, controller.last_name)
    controller.email_address = vatusa_info.email if vatusa_info is not None else vatsim_info.email
    controller.facility = vatusa_info.facility if vatusa_info is not None \
        else 'VAT%s' % vatsim_info.division if vatsim_info.division \
        else None
    controller.rating = ControllerRating.get(vatusa_info.rating) if vatusa_info is not None \
        else ControllerRating.get(vatsim_info.rating)
    query.add(controller)
    return controller


def update_controller_info_from_vatusa(controller: Controller, vatusa_info: VATUSAUserInfo):
    if vatusa_info is None:
        return
    if controller.first_name != vatusa_info.fname or controller.last_name != vatusa_info.lname:
        controller.first_name = vatusa_info.fname if vatusa_info.fname is not None else controller.first_name
        controller.last_name = vatusa_info.lname if vatusa_info.lname is not None else controller.last_name
        # TODO - Notify ATM, DATM on name changes
    # controller.display_name = '%s %s' % (controller.first_name, controller.last_name)
    # TODO - Determine how / when to update display_name, as this might be changed manually
    controller.email_address = vatusa_info.email if vatusa_info.email is not None else controller.email_address
    controller.facility = vatusa_info.facility if vatusa_info.facility is not None else controller.facility


def pick_initials(controller: Controller) -> str:
    # TODO - Pick initials
    return None


def setup_home_controller(controller: Controller):
    # TODO - Send welcome email for Home Controllers
    # TODO - Notify ATM, DATM of new controller
    controller.is_home = True
    _setup_controller(controller)


def setup_visitor_controller(controller: Controller):
    # TODO - Send welcome email for Visitors
    controller.is_visitor = True
    _setup_controller(controller)


def _setup_controller(controller: Controller):
    controller.is_active = True
    controller.member_since = datetime.datetime.now()
    if controller.initials is None:
        controller.initials = pick_initials(controller)
    if controller.positions is None:
        controller_positions = ControllerPositions()
        controller_positions.vatsim_cid = controller.vatsim_cid
        query.add(controller_positions)
        controller.positions = controller_positions


def remove_controller(controller: Controller):
    # TODO - Add log that controller was removed
    controller.is_active = False
    controller.is_home = False
    controller.is_visitor = False
    revoke_all_controller_positions(controller)


def revoke_all_controller_positions(controller: Controller):
    positions: ControllerPositions = controller.positions
    positions.delivery = None
    positions.ground = None
    positions.tower = None
    positions.approach = None
    positions.center = None
