from typing import List


class VATUSAVisitingFacilityInfo:
    id: int
    cid: int
    facility: str

    def __init__(self, data):
        self.id = data.get('id')
        self.cid = data.get('cid')
        self.facility = data.get('facility')


class VATUSAUserInfo:
    cid: int
    fname: str
    lname: str
    email: str
    facility: str
    rating: int
    promotion_eligible: bool
    transfer_eligible: bool
    rating_short: str
    visiting_facilities: List[VATUSAVisitingFacilityInfo]
    isMentor: bool
    isSupIns: bool
    last_promotion: str

    def __init__(self, data):
        self.cid = data.get('cid')
        self.fname = data.get('fname')
        self.lname = data.get('lname')
        self.email = data.get('email')
        self.facility = data.get('facility')
        self.rating = data.get('rating')
        self.rating_short = data.get('rating_short')
        self.promotion_eligible = data.get('promotion_eligible')
        self.transfer_eligible = data.get('transfer_eligible')
        self.visiting_facilities = [VATUSAVisitingFacilityInfo(row) for row in data.get('visiting_facilities', [])]
        self.isMentor = data.get('isMentor')
        self.isSupIns = data.get('isSupIns')
        self.last_promotion = data.get('last_promotion')
        self.flag_homecontroller = data.get('flag_homecontroller')
