import enum


class BetterEnum(enum.Enum):
    def __hash__(self):
        return id(self.name)

    def __eq__(self, other):
        if isinstance(other, BetterEnum):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.name

    @classmethod
    def get(cls, name):
        for option in cls:
            if option.name == name:
                return option
        # Fallback to value match, for ControllerRating
        for option in cls:
            if option.value == name:
                return option
        return None


class ControllerRating(BetterEnum):
    OBS = 1
    S1 = 2
    S2 = 3
    S3 = 4
    C1 = 5
    C3 = 7
    I1 = 8
    I3 = 10
    SUP = 11
    ADM = 12


class ControllerLOAStatus(BetterEnum):
    PENDING = enum.auto()
    ACTIVE = enum.auto()
    DENIED = enum.auto()
    CANCELLED = enum.auto()
    COMPLETED = enum.auto()


class ControllerLogMessage(BetterEnum):
    TRAINING_DEBRIEF_CREATE = 'Training debrief created'
    TRAINING_OBJECTIVES_ASSIGNED = 'Training Objectives assigned: %r'
    TRAINING_OBJECTIVES_COMPLETED = 'Training objectives completed: %r'
    TRAINING_POSITION_CERTIFIED = 'Certification updated for position: %s - %s'


class StaffPosition(BetterEnum):
    ATM = "Air Traffic Manager"
    DATM = "Deputy Air Traffic Manager"
    TA = "Training Administrator"
    DTA = "Deputy Training Administrator"
    EC = "Event Coordinator"
    AEC = "Assistant Event Coordinator"
    WM = "Webmaster"
    AWM = "Assistant Webmaster"
    FM = "Facilities Manager"
    AFM = "Assistant Facilities Manager"
    INS = "Instructor"
    MTR = "Mentor"


class Permission(BetterEnum):
    ADM = 'zse_adm'
    INS = 'zse_ins'
    MTR = 'zse_mtr'
    TA = 'zse_ta'
    EC = 'zse_ec'
    FE = 'zse_fe'


class PositionType(BetterEnum):
    OBS = "Observer"
    DEL = "Clearance Delivery"
    GND = "Ground"
    TWR = "Tower"
    APP = "Approach"
    CTR = "Center"


class TrainingType(BetterEnum):
    CLASSROOM = enum.auto()
    SWEATBOX = enum.auto()
    LIVE_SHADOW = enum.auto()
    OTS = enum.auto()
    WORKSHEET = enum.auto()
    NOTE = enum.auto()


class TrainingObjectiveType(BetterEnum):
    THEORY = enum.auto()


class CertificationType(BetterEnum):
    TRAIN = enum.auto()
    SOLO = enum.auto()
    OTS = enum.auto()
    MINOR = enum.auto()
    FULL = enum.auto()


class DepartureType(BetterEnum):
    PILOT_NAV = enum.auto()
    RADAR_VECTOR = enum.auto()
    HYBRID = enum.auto()


class ExternalLinkType(BetterEnum):
    NAV_TAB_PILOT = enum.auto()


class TrainingStage(BetterEnum):
    MINOR_GROUND = enum.auto()
    MAJOR_GROUND = enum.auto()
    MINOR_TOWER = enum.auto()
    MAJOR_TOWER = enum.auto()
    MINOR_APPROACH = enum.auto()
    MAJOR_APPROACH = enum.auto()
    CENTER = enum.auto()


class TrainingStageRequirementType(BetterEnum):
    VATUSA_EXAM = enum.auto()
    VATUSA_CBT = enum.auto()
    DOCUMENT_READ = enum.auto()
    CONTROLLING_HOURS = enum.auto()
    CALENDAR_DAYS = enum.auto()
    MANUAL_REVIEW = enum.auto()
    MANUAL_REVIEW_INS = enum.auto()
    MANUAL_REVIEW_TA = enum.auto()
    TRAINING_SESSIONS = enum.auto()

