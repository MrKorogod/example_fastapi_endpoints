import json
from pathlib import Path

from loguru import logger

from example_app.core.dto.example_core_dto import CoreDto
from example_app.helpers.custom_error import ExampleCustomError
from example_app.helpers.path_helper import resource_path


def load_config(conf_path: Path) -> CoreDto | None:
    try:
        with open(conf_path, "r") as _json_file:
            conf = CoreDto(**json.loads(_json_file.read()))
            return conf
    except Exception as e:
        logger.error(e)
        raise ExampleCustomError(status_code=500,message=f"Failed in load config. Exeption = {e}")


def set_config(config_dir: str = None) -> CoreDto:
    if config_dir is None:
        config_dir = resource_path("../applied_files/config")
    conf_dir = Path(config_dir)
    conf_path = conf_dir.joinpath(Path("config.json"))
    if conf_path.exists():
        conf = load_config(conf_path)
    else:
        conf = CoreDto()
        conf_dir.mkdir(exist_ok=True, parents=True)
        with open(conf_path, 'w') as f:
            conf_for_write = conf.model_dump_json(indent=4)
            logger.debug(conf_for_write)
            f.write(conf_for_write)
    return conf


# app_config = set_config(config_dir=None)