import aiohttp as aiohttp


# Для отправки данных полученные от пользователей
async def post_quiz(answer):
    async with answer.proxy() as data:
        data = {'user_id': data['user_id'], 'age': data['age'], 'birth': data['birth']}
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://127.0.0.1:8000/answer/quiz/post/", data=data) as response:
            return response.status


# Получение типов сообщений которое отправляет бот пользователю
async def get_type_message(style):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://127.0.0.1:8000/answer/words/get/{style}/") as response:
            return await response.json()
