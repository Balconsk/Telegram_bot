from aiogram import types

from models.model_sqlite3 import DataBase

from aiogram.dispatcher.filters import BoundFilter

database = DataBase()


class BalanceCheck(BoundFilter):
    # If users not allowed then filter return True and handler denial be work
    async def check(self, msg: types.Message) -> bool:
        return not database.get_user_token(msg.from_user.id) > 0


def registration_allowed_users_filter(dp):
    dp.filters_factory.bind(BalanceCheck)
