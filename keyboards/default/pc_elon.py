from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Elon berish!"),
            KeyboardButton(text = "Kompyuter sotuv kanali 💻")
        ]
    ],
    resize_keyboard=True
)