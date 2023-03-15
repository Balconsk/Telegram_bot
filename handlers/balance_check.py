from aiogram import types, Dispatcher

from filters.balance_check import BalanceCheck
from models.model_sqlite3 import DataBase

database = DataBase()

command_text = "You haven't tokens.\nYour balance: {}"


async def balance_check(msg: types.Message):
    tokens = database.get_user_token(msg.from_user.id)
    await msg.answer(command_text.format(tokens))


def register_balance_check(dp: Dispatcher):
    dp.register_message_handler(balance_check, BalanceCheck())
