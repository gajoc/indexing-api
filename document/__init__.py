from enum import Enum, IntEnum


class Language(str, Enum):
    LATIN = 'latin'


class Legitimation(IntEnum):
    LEGITIMATE = 0
    ILLEGITIMATE = 1


class Sex(str, Enum):
    MALE = 'male'
    FEMALE = 'female'


DEFAULT_KEY_IN_DOCUMENTS = 'origin'
