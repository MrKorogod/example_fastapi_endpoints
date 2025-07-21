from pydantic import BaseModel, Field

# ======================================================================================================================

class SomeResponseDto(BaseModel):
    """Пример возвращаемого объекта"""
    id: int = Field(description="ID возвращаемой модели")
    example_param: str | None = Field(description="Пример не обязательного текстового возвращаемого параметра")
    example_f_key_field_id: int = Field(description="Возвращаемое значение ID связанной с данной моделью модели")

# ======================================================================================================================

class BaseFilterDto(BaseModel):
    """Пример ДТО для фильтрации по базовым параметрам моделей"""
    model_id: int | None = Field(default=None, description="ID модели")
    created_at: str | None = Field(default=None, description="Дата создания")
    updated_at: str | None = Field(default=None, description="Дата обновления")

    order_by: str | None = Field(default=None, description="Сортировка, например: 'name' или '-id'")
    limit: int | None = Field(default=None, description="Лимит")
    offset: int | None = Field(default=None, description="Смещение")

class SomeFilterDto(BaseFilterDto):
    example_f_key_field_id: int | None = Field(None, description="Значение ID связанной с данной моделью модели")

# ======================================================================================================================