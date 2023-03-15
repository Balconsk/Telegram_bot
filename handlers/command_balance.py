from aiogram import types, Dispatcher

from models.model_sqlite3 import DataBase

database = DataBase()

command_text = "Your balance: {}"


async def command_balance(msg: types.Message):
    tokens = database.get_user_token(msg.from_user.id)
    await msg.answer(command_text.format(tokens))


def register_command_balance(dp: Dispatcher):
    dp.register_message_handler(command_balance, commands='balance')
