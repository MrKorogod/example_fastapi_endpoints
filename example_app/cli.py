import os
import sys
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from example_app.helpers.custom_error import ExampleCustomError, example_exception_handler
from example_app.helpers.set_config_helper import set_config
from example_app.helpers.set_routers import set_routes

# ======================================================================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ======================================================================================================================

static_dir = os.path.join(BASE_DIR, "applied_files", "admin_panel", "static")
index_html_dir = os.path.join(BASE_DIR, "applied_files", 'admin_panel')
config_dir = os.path.join(BASE_DIR, "applied_files", "config", "config.json")

# ======================================================================================================================

app_config = set_config(config_dir)

# ======================================================================================================================

logger.add(app_config.logger_info.log_file, format="{time} {level} {message}", level=app_config.logger_info.level)

# ======================================================================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_routes(all_routers, app)
    yield

app = FastAPI(lifespan=lifespan)







app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "applied_files", "admin_panel", "static")), name="static")

app.add_exception_handler(ExampleCustomError, example_exception_handler)

@app.get("/")
async def get_index(request: Request):
    return FileResponse(os.path.join(index_html_dir, "index.html"))




if __name__ == '__main__':
    logger.debug(app.routes)
    uvicorn.run("cli:app", host='localhost', port=8021, reload=True)