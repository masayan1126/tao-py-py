from enum import Enum


class SiteType(Enum):
    NOT_NEEDS_LOGIN = 1
    NEEDS_LOGIN_AND_ONE_STEP = 2
    NEEDS_LOGIN_AND_TWO_STEP = 3
