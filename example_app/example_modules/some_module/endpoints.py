from typing import List
from fastapi import APIRouter, Depends

from example_app.core.protector import AppTransport, protector
from example_app.example_modules.some_module.dto import SomeResponseDto, SomeFilterDto, SomeRequestDto
from example_app.example_modules.some_module.loader import SomeLoader

some_router = APIRouter(
    prefix="/example",
    tags=["example"],
    responses={
        200: {"description": "Success"},
        401: {"description": "Unauthorized"},
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    }
)

@some_router.get("/", summary="Возвращает объекты БД",
                    description="Возвращает объекты БД в зависимости от параметров фильтрации",
                    response_model=SomeResponseDto | List[SomeResponseDto])
async def get_versions(transport: AppTransport = Depends(protector), filter_dto: SomeFilterDto = Depends()):
    return await SomeLoader.get(filter_dto = filter_dto, transport=transport)


@some_router.post("/", summary="Add version for software",
                     description="Создает новую запись версии для программного обеспечения в базе данных с предоставленным идентификатором программного обеспечения, версией и пути файла",
                     response_model=SomeResponseDto)
async def add_version(in_dto: SomeRequestDto.SomeCreateDto,
                          transport: AppTransport = Depends(protector)):
    return await SomeLoader.create(in_dto=in_dto, transport=transport)


@some_router.delete("/{version_id}", summary="Delete version",
                       description="Remove a version entry from the database by its unique version ID",
                       response_model=VersionResponseDto)
async def delete_version(version_id: int,
                         transport: AppTransport = Depends(protector)):
    return await SomeLoader.delete(model_id=version_id, transport=transport)

