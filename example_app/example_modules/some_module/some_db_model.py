from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from example_app.core.data_base.app_declarative_base import Base
from example_app.core.data_base.mixin_models import SchemaMixin


class SomeDBModel(SchemaMixin, Base):
    """Software version Model"""
    __tablename__ = "some_model"


    name: Mapped[str] = mapped_column(String(255), nullable=False)
    example_f_key_field_id: Mapped[int] = mapped_column(Integer, ForeignKey("software.model_id"), nullable=False)
    example_param: Mapped[str] = mapped_column()

    # Обратное отношение к fk_model
    software: Mapped["FKModel"] = relationship("FKModel", back_populates="some_model")