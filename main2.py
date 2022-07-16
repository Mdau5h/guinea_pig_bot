from app.config import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from count import get_data

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

    welcome_message = "Привет! Этот бот рассчитает твой долг. \n" \
                      "Вызови команду '/count', чтобы узнать, сколько ты задолжала Ивану 😊\n" \
                      "(касается только части, на которую капают проценты)"
    await message.reply(welcome_message)


@dp.message_handler(commands=['count'])
async def send_welcome(message: types.Message):
    data = get_data()
    await message.reply(f"Общий долг на сегодня: {data['main_debt']}\n"
                        f"Сумма накопленных процентов: {data['every_day_fee']}\n"
                        f"Повторить расчет: '/count'\n"
                        )

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


