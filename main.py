from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_2, get_keyboard_1
from keyboard.key_inline import inline_but_1, inline_but_2


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://avatars.mds.yandex.net/get-entity_search/2487574/434829330/orig', caption='Кот', reply_markup= inline_but_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото машины')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://autovogdenie.ru/wp-content/uploads/2022/05/foto-m4-csl_01.jpg', caption='BMW MM4 CSL', reply_markup= inline_but_2())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отпавить фото машины', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отпавить фото кота', reply_markup=get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)