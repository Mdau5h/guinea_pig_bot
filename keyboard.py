from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btn_new = KeyboardButton('/makenote')
btn_last = KeyboardButton('/last')

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb.row(btn_new, btn_last)
