from aiogram import executor
import handlers
from settings import dp


if __name__ == '__main__':
    handlers.register_handlers_client(dp)
    executor.start_polling(dp, skip_updates=True)