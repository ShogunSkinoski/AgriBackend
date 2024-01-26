from typing import TypeVar, Generic

ResponseType = TypeVar('ResponseType')

class GenericResponse(Generic[ResponseType]):
    value: ResponseType
    success: bool
    message: str