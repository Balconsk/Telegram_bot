from aiogram import types, Dispatcher, filters

command_text = """I do not know this command.
Type /help for help."""


async def command_debug(msg: types.Message):
    await msg.answer(command_text)


def register_command_unknown(dp: Dispatcher):
    dp.register_message_handler(command_debug, filters.Text(startswith='/'))
