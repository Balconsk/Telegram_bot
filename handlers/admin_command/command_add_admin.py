from aiogram import types, Dispatcher, filters
from models.model_sqlite3 import DataBase
from filters.admin_filter import IsAdmin

database = DataBase()


async def command_add_admin(msg: types.Message):
    admin_id = msg.get_args()
    # test admin_id
    try:
        int(admin_id)
    except ValueError:
        await msg.answer("Incorrect user ID.")
        return None
    if database.add_admin(admin_id):
        await msg.reply(f"User {admin_id}, now an administrator")
    else:
        await msg.reply(f"Error\n\nUser {admin_id} may already be an administrator")


def register_command_add_admin(dp: Dispatcher):
    dp.register_message_handler(command_add_admin, IsAdmin(),
                                commands='add_admin')
