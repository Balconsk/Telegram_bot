from aiogram import types, Dispatcher
from models.model_sqlite3 import DataBase
from filters.admin_filter import IsAdmin

database = DataBase()


async def command_remove_allowed_user(msg: types.Message):
    user_id = msg.get_args()
    try:
        int(user_id)
    except ValueError:
        await msg.answer("Incorrect user ID.")
        return None
    if database.remove_allowed_user(user_id):
        await msg.reply(f"User {user_id} remove from group allowed users")
    else:
        await msg.reply(f"Error\n\nThere is no such user. Check if your user id is correct")


def register_command_remove_allowed_user(dp: Dispatcher):
    dp.register_message_handler(command_remove_allowed_user, IsAdmin(),
                                commands='remove_allowed_user')
