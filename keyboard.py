from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_new = KeyboardButton('/new')
btn_last = KeyboardButton('/last')

kb = ReplyKeyboardMarkup(resize_keyboard=True)

kb.row(btn_new, btn_last)
