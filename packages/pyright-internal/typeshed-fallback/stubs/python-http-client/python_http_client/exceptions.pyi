from email.message import Message
from typing import Final

class HTTPError(Exception):
    status_code: int
    reason: str
    body: str
    headers: Message
    def __init__(self, *args) -> None: ...
    def __reduce__(self): ...
    @property
    def to_dict(self): ...

class BadRequestsError(HTTPError): ...
class UnauthorizedError(HTTPError): ...
class ForbiddenError(HTTPError): ...
class NotFoundError(HTTPError): ...
class MethodNotAllowedError(HTTPError): ...
class PayloadTooLargeError(HTTPError): ...
class UnsupportedMediaTypeError(HTTPError): ...
class TooManyRequestsError(HTTPError): ...
class InternalServerError(HTTPError): ...
class ServiceUnavailableError(HTTPError): ...
class GatewayTimeoutError(HTTPError): ...

err_dict: Final[dict[int, type[HTTPError]]]

def handle_error(error) -> HTTPError: ...
