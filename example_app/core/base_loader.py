from abc import ABCMeta

from loguru import logger
from pydantic import BaseModel

from example_app.core.data_base.app_declarative_base import Base
from example_app.core.dto.base_filter_dto import BaseFilterDto
from example_app.core.protector import AppTransport


class BaseModelLoader(ABCMeta):
    db_model: type[Base] = None

    @classmethod
    async def get(cls, filter_params: BaseFilterDto, transport: AppTransport):
        logger.debug(f"BaseModelLoader.get")

    @classmethod
    async def create(cls, in_dto: BaseModel, transport: AppTransport):
        logger.debug(f"BaseModelLoader.create")

    @classmethod
    async def update(cls, model_id: int, in_dto: BaseModel, transport: AppTransport):
        logger.info(f"BaseModelLoader.update")

    @classmethod
    async def delete(cls, model_id: int, transport: AppTransport):
        logger.info(f"BaseModelLoader.delete")


