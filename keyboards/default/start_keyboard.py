from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh menyu"),
        ],
    ],
    resize_keyboard=True,
)
menu_ru = ReplyKeyboardMarkup(
     keyboard=[
        [
            KeyboardButton(text="Главное меню"),
        ],
    ],
    resize_keyboard=True,
)

lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'zbek")
        ],
        [
            KeyboardButton(text="Русский")
        ],
    ]
)
