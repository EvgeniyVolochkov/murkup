from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def inline_but_1():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline_1 = InlineKeyboardButton('Посмотреть', url='https://kinpet.ru/top-20-samykh-populyarnykh-porod-koshek-v-mire-i-v-rossii/?utm_source=yandex-direct&utm_medium=cpc&utm_campaign=Article_42&utm_content=14091807051&utm_term=47514208967_87351837_5189286836&yclid=11494819362187247615')
    keyboard_inline.add(but_inline_1)
    return keyboard_inline

def inline_but_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=1)
    but_inline_2 = InlineKeyboardButton('Посмотреть', url= 'https://www.bmw-m.com/en/all-models/overview-m-and-m-performance/bmw-m4-csl/2022/bmw-m4-csl.html')
    keyboard_inline_2.add(but_inline_2)
    return keyboard_inline_2