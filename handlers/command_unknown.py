from aiogram import types, Dispatcher, filters


async def command_unknown(msg: types.Message):
    pass


def register_command_unknown(dp: Dispatcher):
    dp.register_message_handler(command_unknown, filters.Text(startswith='/'))
