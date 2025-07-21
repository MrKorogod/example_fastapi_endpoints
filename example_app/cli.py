import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from example_app.all_routers import all_routers
from example_app.helpers.custom_error import ExampleCustomError, example_exception_handler
from example_app.helpers.directory_path import index_html_dir
from example_app.helpers.set_config_helper import app_config
from example_app.helpers.set_routers import set_routes

# ======================================================================================================================

logger.add(app_config.logger_info.log_file, format="{time} {level} {message}", level=app_config.logger_info.level)

# ======================================================================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_routes(all_routers, app)
    yield

# ======================================================================================================================
app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "applied_files", "admin_panel", "static")), name="static")

app.add_exception_handler(ExampleCustomError, example_exception_handler)

# ======================================================================================================================
@app.get("/")
async def get_index(request: Request):
    return FileResponse(os.path.join(index_html_dir, "index.html"))

# ======================================================================================================================
if __name__ == '__main__':
    logger.debug(app.routes)
    uvicorn.run("cli:app", host='localhost', port=8021, reload=True)