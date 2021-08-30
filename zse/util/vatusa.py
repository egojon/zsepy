from zse.common import config
from zse.types.vatusa import VATUSAUserInfo
import requests
from typing import List


def get_user_from_cid(cid: int) -> VATUSAUserInfo:
    r = requests.get('https://api.vatusa.net/v2/user/%d?apikey=%s' % (cid, config.VATUSA_API_KEY))
    data = r.json().get('data', {})
    if data.get('status') == 'error':
        return None
    info = VATUSAUserInfo(data)
    return info


def get_facility_roster() -> List[VATUSAUserInfo]:
    r = requests.get('https://api.vatusa.net/v2/facility/ZSE/roster/home?apikey=%s' % config.VATUSA_API_KEY)
    data = r.json().get('data', [])
    infos = [VATUSAUserInfo(rec) for rec in data]
    return infos


def add_visitor_to_roster(cid: int) -> bool:
    # TODO - Don't do anything for now, as we don't want to add people while testing.
    return True

def remove_visitor_from_roster(cid: int) -> bool:
    # TODO - Don't do anything for now, as we don't want to remove people while testing.
    return True
