from example_app.helpers.set_config_helper import app_config


class SchemaMixin:
    """Миксины для указания пользровательской схемы"""
    __table_args__ = {'schema': app_config.data_base_config.schema_name}

