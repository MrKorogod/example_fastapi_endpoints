from enum import Enum
from functools import wraps

from loguru import logger


def permission_required(permissions: Enum ):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            logger.debug(f"Permission decorator for {func.__name__}")
            transport = kwargs.get('transport')
            logger.debug(f"transport {transport}")
            await has_permission(transport.user, permissions)
            return await func(*args, **kwargs)
        return wrapper
    return decorator

async def has_permission(user, required_permission: Enum):
    """Данная функция проверяет доступы записанные в роль пользователя,
     либо присвоенные пользователю на прямую и доступ, передающийся в переменную в декораторе"""

    logger.info(f"================================has_permission================================")
    logger.debug(f"Permission {required_permission}")
    logger.debug(f"user {user}")
