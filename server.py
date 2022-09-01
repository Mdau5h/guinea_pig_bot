from app.config import config
import logging
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = config.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    welcome_message = "Привет! Это бот-дневник. Он сохранит твои секреты. \n" \
                      "Запусти команду /makenote, чтобы сделать запись. \n" \
                      "Запусти команду /last, чтобы увидеть последнюю запись. \n"
    await message.answer(welcome_message)
    await message.delete()


@dp.message_handler(commands=['makenote', 'last'])
async def send_message(message: types.Message):
    welcome_message = "Извини, данный функционал пока не реализован. Мой создатель работает над этим!"
    await message.answer(welcome_message)
    await message.delete()





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

