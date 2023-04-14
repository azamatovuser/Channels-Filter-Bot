from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

groups = InlineKeyboardMarkup(row_width=2)
part = InlineKeyboardButton("Подобрать группу", callback_data='part_groups')
all = InlineKeyboardButton("Список групп", callback_data='all_groups')
groups.add(part, all)