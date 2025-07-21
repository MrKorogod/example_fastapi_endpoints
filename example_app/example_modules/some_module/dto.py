from pydantic import BaseModel, Field

from example_app.core.dto.base_filter_dto import BaseFilterDto

# ======================================================================================================================

class SomeFilterDto(BaseFilterDto):
    example_f_key_field_id: int | None = Field(None, description="Значение ID связанной с данной моделью модели")

# ======================================================================================================================

class SomeResponseDto(BaseModel):
    """Пример возвращаемого объекта"""
    id: int = Field(default=..., description="ID возвращаемой модели")
    name: str = Field(default=..., description="Наименование модели")
    example_param: str | None = Field(default=None, description="Пример не обязательного текстового возвращаемого параметра")
    example_f_key_field_id: int | None = Field(default=None, description="Возвращаемое значение ID связанной с данной моделью модели")

# ======================================================================================================================

class SomeRequestDto:
    class SomeCreateDto(BaseModel):
        name: str = Field(default=..., description="Наименование модели")
        example_param: str | None = Field(default=None,
                                          description="Пример не обязательного текстового возвращаемого параметра")
        example_f_key_field_id: int | None = Field(default=None,
                                                   description="Возвращаемое значение ID связанной с данной моделью модели")

    class SomeUpdateDto(BaseModel):
        name: str | None = Field(default=None, description="Наименование модели")
        example_param: str | None = Field(default=None,
                                          description="Пример не обязательного текстового возвращаемого параметра")
        example_f_key_field_id: int | None = Field(default=None,
                                                   description="Возвращаемое значение ID связанной с данной моделью модели")


