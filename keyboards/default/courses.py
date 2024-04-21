from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

all_c = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Все курсы")
        ],
        [
            KeyboardButton(text="Курсы (RU)")
        ],
        [
            KeyboardButton(text="Курсы (EN)")
        ],
    ],
    resize_keyboard=True
)
