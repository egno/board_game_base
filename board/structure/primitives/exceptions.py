class PointException(Exception):
    pass


class MaxValueException(PointException):
    pass


class MaxDimensionsException(PointException):
    pass


class RotationException(PointException):
    pass
