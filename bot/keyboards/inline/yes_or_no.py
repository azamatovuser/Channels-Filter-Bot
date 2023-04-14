from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

yes_or_no = InlineKeyboardMarkup(row_width=2)
yes = InlineKeyboardButton("Да", callback_data='yes_no')
no = InlineKeyboardButton("Нет", callback_data='yes_no')
yes_or_no.add(yes, no)