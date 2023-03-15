from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import telegram_key
import registration

bot = Bot(telegram_key)
dp = Dispatcher(bot=bot)
registration.all_registrations(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
