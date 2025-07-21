from typing import List
from loguru import logger

from example_app.core.base_loader import BaseModelLoader
from example_app.core.protector import AppTransport
from example_app.example_modules.some_module.dto import SomeFilterDto, SomeResponseDto
from example_app.example_modules.some_module.error_code import ExampleErrorCode
from example_app.example_modules.some_module.some_db_model import SomeDBModel
from example_app.helpers.custom_error import ExampleCustomError


class SomeLoader(BaseModelLoader):
    model = SomeDBModel

    @classmethod
    async def get(cls, filter_dto: SomeFilterDto, transport: AppTransport) -> SomeResponseDto | List[SomeResponseDto]:

        try:
            logger.debug(f"FilterDto: {filter_dto}")
            logger.debug(f"Transport: {transport}")
        except Exception as e:
            raise ExampleCustomError(status_code=500,
                                     app_error_code = ExampleErrorCode.some_error,
                                     message=f"Failed in load config. Exeption = {e}")

        return await BaseModelLoader.get(filter_dto, transport)


