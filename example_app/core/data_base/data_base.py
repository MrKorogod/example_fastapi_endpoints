from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import text

from example_app.core.data_base.app_declarative_base import metadata
from example_app.core.dto.example_core_dto import DataBaseConfigDto
from example_app.helpers.set_config_helper import app_config


class Database:
    """Класс для работы с базой данных"""
    _instance = None
    _engine = None
    _session_factory = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance



    @classmethod
    async def initialize(cls, db_config: DataBaseConfigDto):
        """Инициализация подключения к базе данных"""

        if cls._engine is None:
            connection_string = f"postgresql+asyncpg://{db_config.database_user}:{db_config.database_password}@{db_config.host}:{db_config.port}/{db_config.data_base_name}"

            cls._engine = create_async_engine(
                connection_string,
                echo=db_config.echo,
                future=db_config.future,
                pool_size=db_config.pool_size,
                max_overflow=db_config.max_overflow
            )

            cls._session_factory = async_sessionmaker(
                cls._engine,
                expire_on_commit=False,
                class_=AsyncSession
            )

            # Создаем таблицы, если они не существуют
            async with cls._engine.begin() as conn:
                # Создаем схему, если она указана
                if db_config.schema_name:
                    metadata.schema = db_config.schema_name
                    await conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {db_config.schema_name}"))
                # Создаем таблицы
                await conn.run_sync(metadata.create_all)
            
            logger.info("Database connection initialized and tables created")

            logger.info("Database connection initialized")


    @classmethod
    async def get_session(cls) -> AsyncSession:
        if cls._session_factory is None:
            db_config: DataBaseConfigDto
            await cls.initialize(app_config.data_base_config)

        return cls._session_factory()

   

    @classmethod
    async def close(cls):
        """Закрытие подключения к базе данных"""
        if cls._engine is not None:
            await cls._engine.dispose()
            cls._engine = None
            cls._session_factory = None
            logger.info("Database connection closed")


async def get_db_session():
    session = await Database.get_session()
    try:
        yield session
    finally:
        await session.close()


