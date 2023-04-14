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


@dp.message_handler(text=['Вернуться в меню'])
async def menuback(message:types.Message):
    await message.answer(f"{message.from_user.full_name}, вы вернулись в начальное состояние.\n"
                         f"Для старта отправьте /start", reply_markup=types.ReplyKeyboardRemove())