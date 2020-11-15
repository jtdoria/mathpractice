"""Class definitions for exceptions / errors."""


class BaseError(Exception):
    """Base class for other exceptions."""
    pass


class FailedToConvertError(BaseError):
    """Raised when an object can't be converted to one of the objects defined in definitions.py.

    Attributes
        original_object: object which failed to convert
        tried_type: type to which we tried to convert original_object

    test:
    raise FailedToConvertError(6, 'funky thing')
    """
    def __init__(self, original_object, tried_type):
        self.original_object = original_object
        self.msg = f"Could not convert {original_object} of type {type(original_object)} to a {tried_type}."
        super().__init__(self.msg)


class FailedToIdentifyError(BaseError):
    """Raised when we fail to match a standard python object with one of the objects defined in definitions.py.

    Attributes
        original_object: object which could not be matched

    test:
    raise FailedToIdentifyError(6)
    """
    def __init__(self, original_object):
        self.original_object = original_object
        self.msg = f"Could not identify which object type to convert {original_object} of type {type(original_object)}."
        super().__init__(self.msg)
