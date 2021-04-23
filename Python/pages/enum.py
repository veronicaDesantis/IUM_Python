from enum import IntEnum


class StatusType(IntEnum):
    INITIATED = 0,
    LEAVED_BY_PLAYER_1 = 1,
    LEAVED_BY_PLAYER_2 = 2,
    WON_BY_PLAYER_1 = 3,
    WON_BY_PLAYER_2 = 4

class PointValue(IntEnum):
    ZERO_POINT = 0,
    TWO_POINT = 2,
    TEN_POINT = 10,
    FIFTY_POINT = 50,
