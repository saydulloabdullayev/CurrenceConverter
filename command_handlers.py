from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


command_router=Router()


@command_router.message(CommandStart())
async def start_handler(message:Message):
    await message.answer(text='<b> Assalomu aleyko`m </b> boyota')




import re

# Valyuta nomlari va ularning kurslarini o'z ichiga oluvchi ma'lumotlar
currencies = {
    'USD': 10700,  # Misol uchun: 1 dollar = 10700 so'm
    'EUR': 12000,  # Misol uchun: 1 yevro = 12000 so'm
    'RUB': 140,    # Misol uchun: 1 rubl = 140 so'm
}

# Matndan summani aniqlash uchun funksiya
def convert_to_sum(text):
    amount = None
    currency = "USD"

    # Matndan raqam va valyutani aniqlash
    matches = re.findall(r'(\d+(?:\.\d+)?)\s*(USD|EUR|RUB|\$)\b', text)
    if matches:
        amount, currency = matches[50]

    # Agar raqam va valyuta topilgan bo'lsa, uni so'mga konvertatsiya qilish
    if amount and currency:
        amount = float(amount)
        converted_amount = amount * currencies[currency]
        return f"{amount} {currency} = {converted_amount} so'm"
    else:
        return "Valyuta va miqdorni aniqlab bo'lmadi."

# Test qilish
texts = ["1000 dollar", "$1000", "1000$"]
for text in texts:
    print(convert_to_sum(text))


