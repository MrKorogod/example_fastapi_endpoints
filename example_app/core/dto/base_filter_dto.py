from pydantic import BaseModel, Field


class BaseFilterDto(BaseModel):
    """Пример ДТО для фильтрации по базовым параметрам моделей"""
    model_id: int | None = Field(default=None, description="ID модели")
    created_at: str | None = Field(default=None, description="Дата создания")
    updated_at: str | None = Field(default=None, description="Дата обновления")

    order_by: str | None = Field(default=None, description="Сортировка, например: 'name' или '-id'")
    limit: int | None = Field(default=None, description="Лимит")
    offset: int | None = Field(default=None, description="Смещение")
