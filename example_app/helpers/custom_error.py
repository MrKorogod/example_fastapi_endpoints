from fastapi import Request
from fastapi.responses import JSONResponse

class ExampleCustomError(Exception):
    message: str
    status_code: int

    def __init__(self, message: str, status_code: int = 422):
        self.message = message
        self.status_code = status_code


async def example_exception_handler(request: Request, exc: ExampleCustomError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status_code": exc.status_code, "detail": exc.message}
    )