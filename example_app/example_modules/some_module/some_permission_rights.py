from enum import Enum


class SomeRightsPoints(Enum):
    GET_SOME = {
        'verbose_name':
            {
                'ru': 'Право на просмотр моделей',
                'en': 'The right to view models'
            }
    }
    CREATE_SOME = {
        'verbose_name':
            {
                'ru': 'Право на создание моделей',
                'en': 'The right to create models'
            }
    }
    UPDATE_SOME = {
        'verbose_name':
            {
                'ru': 'Право на обновление моделей',
                'en': 'The right to update models'
            }
    }
    DELETE_SOME = {
        'verbose_name':
            {
                'ru': 'Право на удаление моделей',
                'en': 'The right to remove models'
            },

    }

