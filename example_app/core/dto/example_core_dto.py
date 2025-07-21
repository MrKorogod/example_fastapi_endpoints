from pydantic import BaseModel, Field

from example_app.helpers.path_helper import resource_path


#=======================================================================================================================

class LoggerDto(BaseModel):
    log_file: str = Field(default=resource_path("applied_files/logs/main.log"),
                          description="Путь до файла логов")
    level: str = Field(default="INFO",
                       description="Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)")

    rotation_trigger: str = Field(default="100 MB",
                                  description="Максимальный размер лога")
    compression: str = Field(default="tar",
                             description="Тип сжатия логов")
    retention: str = Field(default="7 day",
                           description="Период хранения старых логов после сжатия")

#=======================================================================================================================

class ServerDto(BaseModel):
    host: str = Field(default="0.0.0.0",
                      description="IP-адрес сервера")
    port: int = Field(default=8005,
                      description="Порт сервера")
    reload: bool = Field(default=False, description="Автоматический перезапуск сервера, при внесении изменений в код")

#=======================================================================================================================

class DataBaseConfigDto(BaseModel):
    database_user: str = Field(default='testuser',
                               description="Пользователь базы данных")
    database_password: str = Field(default='Test123',
                                   description="Пароль пользователя базы данных")
    data_base_name: str = Field(default='example_db_name',
                                description="Наименование базы данных")
    schema_name: str = Field(default='example_shema_name',
                             description="Наименование схемы базы данных")
    host: str = Field(default="localhost",
                      description="IP-адрес базы данных")
    port: int = Field(default=5432,
                      description="Порт базы данных")
    async_engine: bool = Field(default=True,
                               description="Флаг асинхронного подключения к базе данных")
    future: bool = Field(default=True,
                         description="Флаг для использования одного API при миграциях на версиях 1.4 и 2.0 SQLAlchemy")
    echo: bool = Field(default=True,
                       description="Логирование событий БД")
    pool_size: int = Field(default=5,
                           description="Максимальное количество соединений")
    max_overflow: int = Field(default=10,
                              description="Максимальное количество соединений сверх лимита")

#=======================================================================================================================

class FileStorageConfigDto(BaseModel):
    file_folder_path: str = Field(default=resource_path("applied_files/stored_files"),
                                  description="Путь к директории, в которую будут загружаться файлы")

#=======================================================================================================================

class CoreDto(BaseModel):
    logger_info: LoggerDto = Field(default=LoggerDto())
    data_base_config: DataBaseConfigDto = Field(default=DataBaseConfigDto())
    file_storage_config: FileStorageConfigDto = Field(default=FileStorageConfigDto())
    server_info: ServerDto = Field(default=ServerDto())

#=======================================================================================================================