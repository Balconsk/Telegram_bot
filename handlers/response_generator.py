from asyncio import get_event_loop
from services import openai_controls
from aiogram import types, Dispatcher
from models.model_sqlite3 import DataBase

database = DataBase()


async def response_generator(msg: types.Message):
    # noinspection SpellCheckingInspection
    answer = await msg.reply('🧐 Response generation...')
    loop = get_event_loop()
    try:
        response = await loop.run_in_executor(None, openai_controls.prom2gpt, msg.text)
        answer_text = response['text']
        await answer.edit_text(answer_text)
        try:
            database.change_token(msg.from_user.id, response['token']*(-1))
            database.write_log_openai(user_id=msg.from_user.id, prompt=msg.text, answer=answer_text,
                                      product="text-davinci-003", token=response['token'], status=0)
        except:
            print("Error write in database")
    except:
        await msg.reply("There was an error while executing your request. Can you repeat it?")
        database.write_log_openai(user_id=msg.from_user.id, prompt=msg.text,
                                  product="text-davinci-003", status=1)


def register_response_generator(dp: Dispatcher):
    dp.register_message_handler(response_generator, )
