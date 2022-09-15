from app.config import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from manager import FSM, DBManager
from keyboard import *


API_TOKEN = config.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = DBManager()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    welcome_message = "Привет! Это бот-дневник. Он сохранит твои секреты. \n" \
                      "Запусти команду /create_new, чтобы сделать запись. \n" \
                      "Запусти команду /get_last, чтобы увидеть последнюю запись. \n" \
                      "Запусти команду /get_some, чтобы выбрать запись для просмотра. \n"
    await message.answer(welcome_message, reply_markup=kb)
    await message.delete()


@dp.message_handler(commands='create_new', state=None)
async def new_record(message: types.Message):
    answer = "Ну, рассказывай, шо там у тебя"
    await FSM.new_msg.set()
    await message.answer(answer, reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(state=FSM.new_msg)
async def load_record(message: types.Message, state: FSMContext):
    db.add_message(raw_message=message.text)
    answer = "Ну ты ващееее! Ниче, бывает! Я это запомню)"
    await state.finish()
    await message.answer(answer, reply_markup=kb)


@dp.message_handler(commands=['get_last'])
async def send_last_record(message: types.Message):
    last_record = db.get_last_message()
    answer = f"Последняя запись от: {last_record[0]}. \n" \
             f"{last_record[1]}"
    await message.answer(answer, reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['get_some'])
async def send_record_list(message: types.Message):
    list_description = f'В моей памяти вот столько записей: {db.get_messages_count()}. \n' \
                       f'Выбери номер для просмотра. \n' \
                       f'Стрелками можешь выбрать страницу. '
    await message.answer(list_description, reply_markup=ReplyKeyboardRemove())
    msg_list = db.get_message_list()
    answer = '\n'.join([f'{msg[0]}: {msg[1]}' for msg in msg_list])
    await message.answer(answer, reply_markup=in_kb_last_pg)
    # await FSM.msg_list.set()
    await message.delete()



# @dp.message_handler(commands=['get_some'])
# async def get_record_by_id(message: types.Message):
#     record_date, record_body = db.get_message_by_id(1)
#     answer = f"Запись с id 1: {record_date}. \n" \
#              f"{record_body}"
#     await message.answer(answer, reply_markup=kb)
#     await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

