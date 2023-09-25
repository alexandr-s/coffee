import enum


class GrindEnums(enum.Enum):
    MIN_GRIND = 1
    MAX_GRIND = 14
    DEFAULT_GRIND = 7


class TemperatureEnums(enum.Enum):
    MIN_TEMPERATURE = 1
    MAX_TEMPERATURE = 100


class RateEnums(enum.Enum):
    MIN_RATE = 1
    MAX_RATE = 10
