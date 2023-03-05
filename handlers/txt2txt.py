from asyncio import get_event_loop
from services import openai_controls
from aiogram import types, Dispatcher


async def txt2txt(msg: types.Message):
    # noinspection SpellCheckingInspection
    answer = await msg.reply('🕓 Response generation...')
    loop = get_event_loop()
    try:
        text = await loop.run_in_executor(None, openai_controls.prom2gpt, msg.text)
        await answer.edit_text(text)
    except Exception:
        await msg.reply("There was an error while executing your request. Can you repeat it?")


def register_txt2txt(dp: Dispatcher):
    dp.register_message_handler(txt2txt, state=None)
