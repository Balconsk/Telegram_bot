from aiogram import types, Dispatcher
from models.model_sqlite3 import DataBase
from filters.admin_filter import IsAdmin

database = DataBase()


async def command_add_allowed_user(msg: types.Message):
    user_id = msg.get_args()
    try:
        int(user_id)
    except ValueError:
        await msg.answer("Incorrect user ID.")
        return None
    if database.add_allowed_user(user_id):
        await msg.reply(f"User {user_id}, now an allowed user")
    else:
        await msg.reply(f"Error\n\nUser {user_id} may already be an allowed user")


def register_command_add_allowed_user(dp: Dispatcher):
    dp.register_message_handler(command_add_allowed_user, IsAdmin(),
                                commands='add_allowed_user')
