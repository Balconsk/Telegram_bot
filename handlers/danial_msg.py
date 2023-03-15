from aiogram import types, Dispatcher

from filters.alowed_users import IsAllowedUsers

command_text = """This is a private bot."""


async def danial_msg(msg: types.Message):
    await msg.answer(command_text)


def register_danial_msg(dp: Dispatcher):
    dp.register_message_handler(danial_msg, IsAllowedUsers())
