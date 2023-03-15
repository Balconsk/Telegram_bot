from asyncio import get_event_loop
from services import openai_controls
from aiogram import types, Dispatcher
from models.model_sqlite3 import DataBase

database = DataBase()

command_text = 'The link to the image is only valid for 30 minutes\n<b><a href="{}">LINK</a></b>'


async def command_img(msg: types.Message):
    # noinspection SpellCheckingInspection
    answer = await msg.reply('🕓 Image generation...')
    loop = get_event_loop()
    try:
        text = await loop.run_in_executor(None, openai_controls.prom2dall_e, msg.text)
        await answer.edit_text(command_text.format(text), parse_mode='HTML')
        try:
            database.write_log_openai(user_id=msg.from_user.id, prompt=msg.text, answer=text,
                                      product="text-davinci-003", status=0)
        except:
            print("Error write in database")
    except Exception:
        await msg.reply("There was an error while executing your request. Can you repeat it?")
        database.write_log_openai(user_id=msg.from_user.id, prompt=msg.text,
                                  product="text-davinci-003", status=1)


def register_command_img(dp: Dispatcher):
    dp.register_message_handler(command_img, commands='img')
