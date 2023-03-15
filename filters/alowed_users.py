from aiogram import types

from models.model_sqlite3 import DataBase

from aiogram.dispatcher.filters import BoundFilter

database = DataBase()


class IsAllowedUsers(BoundFilter):
    # If users not allowed then filter return True and handler denial be work
    async def check(self, msg: types.Message) -> bool:
        return not(msg.from_user.id in database.get_allowed_users_list())


def registration_allowed_users_filter(dp):
    dp.filters_factory.bind(IsAllowedUsers)
