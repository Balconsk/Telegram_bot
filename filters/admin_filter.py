from aiogram import types

from models.model_sqlite3 import DataBase

from aiogram.dispatcher.filters import BoundFilter

database = DataBase()


class IsAdmin(BoundFilter):
    async def check(self, msg: types.Message) -> bool:
        return msg.from_user.id in database.get_admin_list()


def registration_admin_filter(dp):
    dp.filters_factory.bind(IsAdmin)
