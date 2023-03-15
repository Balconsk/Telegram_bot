from aiogram import types, Dispatcher
from models.model_sqlite3 import DataBase
from filters.admin_filter import IsAdmin

database = DataBase()


async def command_change_token(msg: types.Message):
    user_id, token = msg.get_args().split(' ')
    if database.change_token(user_id, token):
        await msg.reply(f"User {user_id}, now have {token} tokens ")
    else:
        await msg.reply(f"Error\n\nThere is no such user. Check if your user id is correct")


def register_command_change_token(dp: Dispatcher):
    dp.register_message_handler(command_change_token, IsAdmin(),
                                commands='change_token')
