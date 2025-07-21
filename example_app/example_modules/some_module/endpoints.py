from typing import List
from fastapi import APIRouter, Depends

from example_app.core.permission_handler import permission_required
from example_app.core.protector import AppTransport, protector
from example_app.example_modules.some_module.dto import SomeResponseDto, SomeFilterDto, SomeRequestDto
from example_app.example_modules.some_module.loader import SomeLoader
from example_app.example_modules.some_module.some_permission_rights import SomeRightsPoints

# ======================================================================================================================

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

# ======================================================================================================================

@some_router.get("/", summary="Возвращает объекты БД",
                    description="Возвращает объекты БД в зависимости от параметров фильтрации",
                    response_model=SomeResponseDto | List[SomeResponseDto])
@permission_required(SomeRightsPoints.GET_SOME)
async def get_some(transport: AppTransport = Depends(protector), filter_dto: SomeFilterDto = Depends()):
    return await SomeLoader.get(filter_dto = filter_dto, transport=transport)

# ======================================================================================================================

@some_router.post("/", summary="Создает объект в БД",
                     description="Создает новую запись в базе данных",
                     response_model=SomeResponseDto)
@permission_required(SomeRightsPoints.CREATE_SOME)
async def create_some(in_dto: SomeRequestDto.SomeCreateDto,
                          transport: AppTransport = Depends(protector)):
    return await SomeLoader.create(in_dto=in_dto, transport=transport)

# ======================================================================================================================

@some_router.patch("/{model_id}", summary="Обновляет объект в БД",
                     description="Обновляет существующую запись в БД",
                     response_model=SomeResponseDto)
@permission_required(SomeRightsPoints.UPDATE_SOME)
async def update_some(model_id: int, in_dto: SomeRequestDto.SomeCreateDto,
                          transport: AppTransport = Depends(protector)):
    return await SomeLoader.update(model_id=model_id, in_dto=in_dto, transport=transport)

# ======================================================================================================================

@some_router.delete("/{model_id}", summary="Удаляем объект",
                       description="Удаляет объект в БД",
                       response_model=SomeResponseDto)
@permission_required(SomeRightsPoints.DELETE_SOME)
async def delete_some(model_id: int,
                         transport: AppTransport = Depends(protector)):
    return await SomeLoader.delete(model_id=model_id, transport=transport)

# ======================================================================================================================

