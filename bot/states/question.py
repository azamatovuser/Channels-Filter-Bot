from aiogram.dispatcher.filters.state import StatesGroup, State


class QuestionState(StatesGroup):
    group = State()
    answer = State()