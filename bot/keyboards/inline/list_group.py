import requests
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data
from bot.data.config import BASE_URL

rs = requests.get(url=f"{BASE_URL}backend/list/groups/")
data = rs.json()

list_group = InlineKeyboardMarkup(row_width=2)
for i in data:
    list_group.add(InlineKeyboardButton(f"{i['name']}", callback_data=f"{i['name']}"))