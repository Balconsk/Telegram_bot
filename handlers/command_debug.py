from asyncio import sleep as async_sleep
from aiogram import types, Dispatcher

command_text = """This command is used for development.
This message will be deleted after 15 seconds.
🙂 User_id - {}
💬 Chat_id - {}"""


async def command_debug(msg: types.Message):
    await msg.delete()
    bot_msg = await msg.answer(command_text.format(msg.from_user.id, msg.chat.id))
    await async_sleep(15)
    await bot_msg.delete()


def register_command_debug(dp: Dispatcher):
    dp.register_message_handler(command_debug, commands='debug')
