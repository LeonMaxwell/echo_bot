from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from connect_base import get_type_message, post_quiz
from states import QuizStates


async def command_default(message: types.Message):
    res = await get_type_message(style='def')
    await message.answer(f"{res.get('message')}")


async def command_start(message: types.Message, state: FSMContext):
    await QuizStates.start.set()
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
    await message.answer(f"Сколько вам лет?")


async def command_age(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await QuizStates.next()
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await message.answer("Где вы родились?")
    else:
        await message.answer("Введенный возраст не корректен!")


async def command_birth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['birth'] = message.text
    res = await post_quiz(state)
    await state.finish()
    if res:
        answer = await get_type_message(style="acs")
    else:
        answer = await get_type_message(style="err")
    await message.answer(f"{answer.get('message')}")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'], state='*')
    dp.register_message_handler(command_age, state=QuizStates.start)
    dp.register_message_handler(command_birth, state=QuizStates.age)
    dp.register_message_handler(command_default, state=None)