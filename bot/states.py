from aiogram.dispatcher.filters.state import State, StatesGroup


class QuizStates(StatesGroup):
    start = State()
    age = State()
