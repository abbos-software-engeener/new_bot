import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu, lang,menu_ru
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from states.status import PersonalData

from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # try:
    #     user = await db.add_user(
    #         telegram_id=message.from_user.id,
    #         full_name=message.from_user.full_name,
    #         username=message.from_user.username,
    #     )
    # except asyncpg.exceptions.UniqueViolationError:
    #     user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(
        """
Здравствуйте! 
Я онлайн помощник компании TRIPLEBOX. 
На каком языке Вы хотите продолжить диалог?


Salom! 
Men TRIPLEBOX kompaniyasining onlayn yordamchisiman. 
Muloqotni qaysi tilda davom ettirishni istaysiz?
        """,
        reply_markup=menu,
    )

@dp.message_handler(Text(startswith="O'zbek"),state=None)
async def bot_start(message: types.Message, ):
    await PersonalData.uz.set()
    await message.edit_text(text="Bo'limni tanlang", reply_markup=menu)


@dp.message_handler(Text(startswith="Русский"),state=None)
async def bot_start(message: types.Message, ):
    await PersonalData.ru.set()
    await message.edit_text(text="Выберите раздел", reply_markup=menu_ru)


    # ADMINGA xabar beramiz
    # count = await db.count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
