from enum import Enum

from fastapi import Request
from fastapi.responses import JSONResponse

class ExampleCustomError(Exception):
    message: str
    status_code: int

    def __init__(self, message: str, status_code: int = 422, app_error_code: Enum | None = None):
        self.message = message
        self.status_code = status_code
        self.app_error_code = app_error_code.value if app_error_code else None


async def example_exception_handler(request: Request, exc: ExampleCustomError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status_code": exc.status_code, "detail": exc.message}
    )