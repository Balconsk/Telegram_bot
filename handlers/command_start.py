from aiogram import types, Dispatcher, filters

# noinspection SpellCheckingInspection
command_text = """Hello, good to see you. 👋
I'm a bot I can answer questions and more. 😏
You can type /help for details. 📋
"""


async def command_start(msg: types.Message):
    await msg.answer(command_text)


def register_command_start(dp: Dispatcher):
    dp.register_message_handler(command_start, filters.CommandStart())
