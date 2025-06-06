from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice
from aiogram.utils import executor
import logging

BOT_TOKEN = '7906990574:AAEMgoPQvayFug06v6w49p3k7cfp5c8owuA'
PAYMENT_PROVIDER_TOKEN = '381764678:TEST:TEST'
PDF_PATH = 'metodichka.pdf'
PRICE_RUB = 1500

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'buy'])
async def cmd_buy(message: types.Message):
    prices = [LabeledPrice(label='Методичка PDF', amount=PRICE_RUB * 100)]
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Методичка по H. pylori',
        description='Методичка PDF по персонализированному подходу к лечению H. pylori',
        provider_token=PAYMENT_PROVIDER_TOKEN,
        currency='RUB',
        prices=prices,
        start_parameter='buy-method',
        payload='metodichka_001'
    )

@dp.pre_checkout_query_handler(lambda q: True)
async def pre_checkout(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def got_payment(message: types.Message):
    await message.answer("✅ Спасибо за оплату! Вот Ваша методичка 📘")
    await message.answer_document(open(PDF_PATH, 'rb'))

if __name__ == '__main__':
    executor.start_polling(dp)
