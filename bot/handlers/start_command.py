from aiogram.types import Message
from bot.keyboards.menu import Menu


async def start_command(message: Message):
    menu = Menu()
    await message.reply("Я - Soter Bot. \nДобро Пожаловать в меню:", reply_markup=menu.get_menu())