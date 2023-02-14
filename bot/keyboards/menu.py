from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Menu:
    @staticmethod
    def get_menu():
        markup = InlineKeyboardMarkup(row_width=3)
        markup.add(
            InlineKeyboardButton("🗿 Профиль", callback_data="profile"),
            InlineKeyboardButton("💵 Заработать", callback_data="earn"),
        )

        markup.row(
            InlineKeyboardButton("♾ Convert", callback_data="convert"),
        )

        markup.add(
            InlineKeyboardButton("💼 Мои профессии", callback_data="professions"),
            InlineKeyboardButton("⚙️ Настройки", callback_data="settings"),
            InlineKeyboardButton("🏆 Задачи", callback_data="tasks"),
            InlineKeyboardButton("⤵️ Перейти в панель управления", callback_data="admin_panel"),
        )
        return markup
