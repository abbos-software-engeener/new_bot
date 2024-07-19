from typing import Union
from aiogram import types
from aiogram.types import CallbackQuery, Message
from data.config import BOT_TOKEN
import requests
from aiogram.dispatcher import FSMContext
from states.status import PersonalData
from keyboards.default.start_keyboard import *
from keyboards.inline.menu_keyboards import (
    menu_cd,
    categories_keyboard,
    subcategories_keyboard,
    items_keyboard,
    item_keyboard,
)
from loader import dp, db, bot
def fetch_item_by_id(id):
    url = f'https://test.edugately.com/api/house/{id}'  # Replace with your API endpoint
    response = requests.get(url)
    return response.json()


# def fetch_item_by_id(id):
#     url = f'https://test.edugately.com/api/house/{id}'  # Replace with your API endpoint
#     response = requests.get(url)
#     return response.json()


client_url = "https://test.edugately.com/api/client-create/"
response = requests.get(client_url)

# Bosh menyu matni uchun handler
@dp.message_handler(text="Bosh menyu")
async def show_menu(message: types.Message):
    # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
    await list_categories(message)

@dp.message_handler(text="Главное меню")
async def show_menu(message: types.Message):
    # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
    await list_categories(message)

# Kategoriyalarni qaytaruvchi funksiya. Callback query yoki Message qabul qilishi ham mumkin.
# **kwargs yordamida esa boshqa parametrlarni ham qabul qiladi: (category, subcategory, item_id)
async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Keyboardni chaqiramiz
    markup = await categories_keyboard()

    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz
    if isinstance(message, Message):
        await message.answer("Bo'lim tanlang", reply_markup=markup)

    # Agar foydalanuvchidan Callback kelsa Callback natbibi o'zgartiramiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


# Ost-kategoriyalarni qaytaruvchi funksiya
async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)

    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
    await callback.message.edit_reply_markup(markup)


# Ost-kategoriyaga tegishli mahsulotlar ro'yxatini yuboruvchi funksiya
async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)
    print(callback)

    await callback.message.edit_text(text="Uy tanlang", reply_markup=markup)



# Biror mahsulot uchun Xarid qilish tugmasini yuboruvchi funksiya
async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    # markup = item_keyboard(category, subcategory, item_id)
    # We get information about the product from the database
    item = await db.get_product(item_id)
    result=fetch_item_by_id(item_id)

    if item["image_data1"]:
        text = f"<a href=\"{result['image_data1']}\">{item['name']}</a>\n\n"
    else:
        text = f"{item['name']}\n\n"
    text += f"Price: {item['price']}$\n{item['description']}"
    
    # await bot.send_photo(callback.from_user.id, photo=item['image_data1'], caption=text, parse_mode='HTML')
    await callback.message.edit_text(text=text, reply_markup=register)



# Yuqoridagi barcha funksiyalar uchun yagona handler
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # Foydalanuvchi so'ragan Kategoriya
    category = callback_data.get("category")

    # Ost-kategoriya (har doim ham bo'lavermaydi)
    subcategory = callback_data.get("subcategory")

    # Mahsulot ID raqami (har doim ham bo'lavermaydi)
    item_id = int(callback_data.get("item_id"))

    # Har bir Level (qavatga) mos funksiyalarni yozib chiqamiz
    levels = {
        "0": list_categories,  # Kategoriyalarni qaytaramiz
        "1": list_subcategories,  # Ost-kategoriyalarni qaytaramiz
        "2": list_items,  # Mahsulotlarni qaytaramiz
        "3": show_item,  # Mahsulotni ko'rsatamiz
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call, category=category, subcategory=subcategory, item_id=item_id
    )

@dp.message_handler(text_contains="Ro'yxatdan o'tish", state=None)
async def bot_register(message:types.Message, state: FSMContext):
    job=message.text

    await PersonalData.name.set()

    await message.answer("Ro'yxatdan o'tish uchun to'liq ism familiyangizni kiriting!") 



# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(state=PersonalData.name)
async def enter_test(message: types.Message, state: FSMContext):
    surname = message.text
    await state.update_data(
        {"name": surname}
    )
    await message.answer("Raqamingizni jonating pastdagi tugma orqali !", reply_markup=menuStart)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNum, content_types=types.ContentType.CONTACT)
async def answer_phone(message: types.Message, state: FSMContext,):
    phone = message.contact.phone_number
    await state.update_data(
        {"phone": phone}
    )
    get_data = await state.get_data()
    data = {
        'fullname': get_data.get("name"),
        'phone_number': get_data.get("phone")
    }
    response = requests.post(client_url, json=data)
    if response.status_code == 201:
        # Print the response content
        await message.answer("Muvafaqiyatli ro'yhatdan o'tdingiz.Siz bilan yaqin orada hodimlarimiz aloqaga chqadi.")
    else:
        # Print an error message if the request failed
        await message.answer("Siz oldin ro'yxatdan o'tgansiz.")
    await state.finish()     