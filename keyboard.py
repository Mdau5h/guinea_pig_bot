from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_new = KeyboardButton('/create_new')
btn_last = KeyboardButton('/get_last')
btn_some = KeyboardButton('/get_some')

kb = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_new, btn_last)
