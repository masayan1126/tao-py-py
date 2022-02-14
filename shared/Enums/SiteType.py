from enum import Enum


class SiteType(Enum):
    NOT_NEEDS_LOGIM = 1
    NEEDS_LOGIM_AND_ONE_STEP = 2
    NEEDS_LOGIM_AND_TWO_STEP = 3
