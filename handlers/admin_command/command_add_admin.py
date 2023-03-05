from asyncio import sleep as async_sleep
from aiogram import types, Dispatcher, filters


async def command_add_admin(msg: types.Message):
    admin_id = msg.get_args()
    # test admin_id
    try:
        int(admin_id)
    except ValueError:
        await msg.answer("Incorrect user ID.")
        return None
    with open('admin_list.txt', 'a') as file:
        file.write(f',{admin_id}')
    await msg.reply(f"User {admin_id}, now an administrator")


def register_command_add_admin(dp: Dispatcher):
    dp.register_message_handler(command_add_admin, filters.IDFilter(user_id=5530490710), commands='add_admin')

