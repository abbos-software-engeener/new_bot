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
    ],
    resize_keyboard=True,

)
register = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Ro'yxatdan o'tish"),
        # KeyboardButton(text="Forum haqida ma’lumot"),
    ],
    ],
    resize_keyboard=True
)

uy = ReplyKeyboardMarkup(
    keyboard=[
       [
            KeyboardButton(text="/show")
       ],
    ],
    resize_keyboard=True
)

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Contact', request_contact=True),
            # KeyboardButton(text='Location', request_location=True),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

info = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='TELEFON RAQAMLAR '),            
            KeyboardButton(text='LOKATSIYALAR '),            
            KeyboardButton(text='LOYIHALAR va OBYEKTLAR'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

location_button=ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Lokatsiya', request_location=True),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

finish=ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Tugatish'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)