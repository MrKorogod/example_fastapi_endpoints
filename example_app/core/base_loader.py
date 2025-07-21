from abc import ABCMeta

from loguru import logger
from sqlalchemy import select
from pydantic import BaseModel
from fastapi import HTTPException

from example_app.core.data_base.app_declarative_base import Base
from example_app.core.dto.base_filter_dto import BaseFilterDto
from example_app.core.protector import AppTransport


class BaseModelLoader(ABCMeta):
    db_model: type[Base] = None

    @classmethod
    async def get(cls, filter_params: BaseFilterDto, transport: AppTransport):
        logger.debug(f"BaseModelLoader.get")

        filter_params_dict = filter_params.model_dump(exclude_defaults=True)
        query = select(cls.db_model).filter_by(**filter_params_dict)

        if filter_params.limit:
            query = query.limit(filter_params.limit)
        if filter_params.offset:
            query = query.offset(filter_params.offset)
        if filter_params.order_by:
            query = query.order_by(filter_params.order_by)

        if not (model := (await transport.db_session.execute(query)).scalar()):
            raise HTTPException(status_code=404, detail=f"Model = {cls.db_model.__name__} not found")
        return model

    @classmethod
    async def create(cls, in_dto: BaseModel, transport: AppTransport):
        logger.debug(f"BaseModelLoader.create")

    @classmethod
    async def update(cls, model_id: int, in_dto: BaseModel, transport: AppTransport):
        logger.info(f"BaseModelLoader.update")

    @classmethod
    async def delete(cls, model_id: int, transport: AppTransport):
        logger.info(f"BaseModelLoader.delete")


