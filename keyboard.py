from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btn_new = KeyboardButton('/create_new')
btn_last = KeyboardButton('/get_last')
btn_some = KeyboardButton('/get_some')

kb = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_new, btn_last, btn_some)

in_btn_prev = InlineKeyboardButton(text='<<', callback_data='prev_page')
in_btn_next = InlineKeyboardButton(text='>>', callback_data='next_page')


in_kb_first_pg = InlineKeyboardMarkup(row_width=1).row(in_btn_next)
in_kb = InlineKeyboardMarkup(row_width=1).row(in_btn_prev, in_btn_next)
in_kb_last_pg = InlineKeyboardMarkup(row_width=1).row(in_btn_prev)
