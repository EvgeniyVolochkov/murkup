from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton('Отправь фото кота')
button_2 = KeyboardButton('Перейти на следующую клавиатуру')
keyboard.add(button_1, button_2)

keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
button_3 = KeyboardButton('Отправь фото машины')
button_4 = KeyboardButton('Вернуться на 1 клавиатуру')
keyboard_2.add(button_3, button_4)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой бот', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://avatars.mds.yandex.net/get-entity_search/2487574/434829330/orig', caption='Кот', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Отправь фото машины')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://autovogdenie.ru/wp-content/uploads/2022/05/foto-m4-csl_01.jpg', caption='Машина', reply_markup=keyboard_2)

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отпавить фото машины', reply_markup=keyboard_2)

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отпавить фото кота', reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)