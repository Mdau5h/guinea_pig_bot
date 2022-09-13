from app.config import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from manager import FSM, DBManager
from keyboard import kb


API_TOKEN = config.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
manager = DBManager()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    welcome_message = "Привет! Это бот-дневник. Он сохранит твои секреты. \n" \
                      "Запусти команду /new, чтобы сделать запись. \n" \
                      "Запусти команду /last, чтобы увидеть последнюю запись. \n"
    await message.answer(welcome_message, reply_markup=kb)
    await message.delete()


@dp.message_handler(commands='new', state=None)
async def new_message(message: types.Message):
    answer = "Ну, рассказывай, шо там у тебя"
    await FSM.new_msg.set()
    await message.answer(answer, reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(state=FSM.new_msg)
async def load_message(message: types.Message, state: FSMContext):
    manager.add_message(raw_message=message.text)
    answer = "Ну ты ващееее! Ниче, бывает! Я это запомню)"
    await state.finish()
    await message.answer(answer, reply_markup=kb)


@dp.message_handler(commands=['last'])
async def send_message(message: types.Message):

    record_date, record_body = manager.last_message()
    answer = f"Последняя запись от: {record_date}. \n" \
             f"{record_body}"
    await message.answer(answer, reply_markup=kb)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

