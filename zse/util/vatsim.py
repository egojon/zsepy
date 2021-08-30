from zse.common import config
import json
import requests


class VATSIMRatingsInfo:
    id: int
    rating: int
    pilotrating: int
    susp_date: str
    reg_date: str
    region: str
    division: str
    subdivision: str
    lastratingchange: str
    email: str
    name_first: str
    name_last: str

    def __init__(self, data):
        self.id = data.get('id')
        self.rating = data.get('rating')
        self.pilotrating = data.get('pilotrating')
        self.susp_date = data.get('susp_date')
        self.reg_date = data.get('reg_date')
        self.region = data.get('region')
        self.division = data.get('division')
        self.subdivision = data.get('subdivision')
        self.lastratingchange = data.get('lastratingchange')
        self.email = data.get('email')
        self.name_first = data.get('name_first')
        self.name_last = data.get('name_last')


def get_info_from_cid(cid: int) -> VATSIMRatingsInfo:
    r = requests.get('https://api.vatsim.net/api/ratings/%d/' % cid,
                     headers={"Authorization": "Token %s" % config.VATSIM_API_KEY})
    data = json.loads(r.text)
    if data.get('detail') == 'Not Found.':
        return None
    info = VATSIMRatingsInfo(data)
    return info
