from aiogram.dispatcher.filters.state import StatesGroup, State


# # Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
# class PersonalData(StatesGroup):
#     # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
#     uz = State() # ism
#     ru = State() # email
#     en = State() # Tel raqami


class PersonalData(StatesGroup):
    # Foydalanuvchi buyerda n ta holatdan o'tishi kerak
    name = State() # ism
    # address = State() # Tel raqami
    phoneNum = State()
    # work = State()
    # check = State()
    # tarif = State()   