from enum import Enum, auto

class GameStates(Enum):
    NOT_STARTED = auto()
    STARTED = auto()
    COMPLETED = auto()