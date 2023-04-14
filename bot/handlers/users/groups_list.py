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
from functools import partial


@dp.callback_query_handler(text=['part_groups'])
async def part_groups(call: types.CallbackQuery):
    await call.message.answer("Вы являетесь специалистом этой сферы?", reply_markup=yes_or_no)
    await call.message.delete()


@dp.callback_query_handler(text=['all_groups'])
async def all_groups(call: types.CallbackQuery):
    rs1 = requests.get(url=f"{BASE_URL}backend/list/groups/")
    data1 = rs1.json()
    for i in data1:
        name = f"{i['name']}\n"
        links = "\n".join(title['title'] for title in i['link'])
        await call.message.answer(name + links, reply_markup=menu)
    await call.message.delete()


@dp.callback_query_handler(text=['yes_no'], state=None)
async def yes(call: types.CallbackQuery):
    await call.message.answer('Категории', reply_markup=list_group)
    await QuestionState.group.set()
    await QuestionState.next()
    await call.message.delete()


async def groups_callback(call: types.CallbackQuery, state: FSMContext, group_name: str):
    selected_group = next((group for group in data4 if group['name'] == group_name), None)
    if selected_group is not None:
        name = f"{selected_group['name']}\n"
        links = "\n".join(title['title'] for title in selected_group['link'])
        await call.message.answer(name + links, reply_markup=menu)
        await state.finish()

    await call.answer(cache_time=3)
    await call.message.delete()


rs4 = requests.get(url=f"{BASE_URL}backend/list/groups/")
data4 = rs4.json()

for i in data4:
    group_name = i['name']
    dp.callback_query_handler(lambda callback_query, group_name=group_name: callback_query.data == group_name,
                              state=QuestionState.answer)(partial(groups_callback, group_name=group_name))


    async def all_groups(call: types.CallbackQuery, state: FSMContext):
        name = f"{i['name']}\n"
        links = "\n".join(title['title'] for title in i['link'])
        await call.message.answer(name+links, reply_markup=menu)
        await state.finish()
        await call.answer(cache_time=3)
        await call.message.delete()
