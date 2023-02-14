from aiogram import executor
from main import bot, dp
from bot import start_command


if __name__ == "__main__":
    dp.register_message_handler(start_command, commands="start")
    executor.start_polling(dp, skip_updates=True)
