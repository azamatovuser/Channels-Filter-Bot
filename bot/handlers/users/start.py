import requests
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.keyboards.inline.groups import groups
from bot.keyboards.default.menu import menu
from bot.keyboards.inline.list_group import list_group
from bot.keyboards.inline.yes_or_no import yes_or_no
from loader import dp, bot
from aiogram.utils import callback_data
from bot.data.config import BASE_URL
from bot.states.question import QuestionState

rs = requests.get(url=f"{BASE_URL}backend/list/groups/")
data = rs.json()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_id
    user_full_name = message.from_user.full_name
    data2 = {
        "id": user_id,
        "full_name": user_full_name
    }
    rs2 = requests.post(url=f"{BASE_URL}backend/person/create/", data=data2)
    await message.answer(f"Привет, {message.from_user.full_name}! "
                         f"Я бот, который поможет тебе выбрать "
                         f"группу по твоим интересам", reply_markup=groups)


