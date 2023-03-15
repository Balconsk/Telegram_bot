from aiogram import types, Dispatcher, filters

command_text = """🔵 What am I?
I am a bot that can generate responses to your queries.

🔵 My available commands are:
/img (query) - Generate image 🖼 (one img = 500 tokens)
/ask (query) - Send a text query. (Not working yet)
"""


async def command_help(msg: types.Message):
    await msg.answer(command_text)


def register_command_help(dp: Dispatcher):
    dp.register_message_handler(command_help, filters.CommandHelp())
