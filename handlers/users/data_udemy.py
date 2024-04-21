from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_data import cours_callback
from keyboards.inline.next_buttons import next_courses
from loader import dp
from utils.misc.requ_data import AllCourses, EnCourses, RuCourses
from keyboards.default import all_c


@dp.message_handler(Command('all'))
async def get_all_courses(message: types.Message):
    await message.answer("Выберите курсы из меню ниже:", reply_markup=all_c)


@dp.message_handler(text="Все курсы")
async def get_all_courses(message: types.Message):
    data = AllCourses()
    print(data)
    for i in range(12):
        await message.answer(f"{data.one_courses(i)[0]}\n{data.one_courses(i)[1]}\n"
                             f"Author: {data.one_courses(i)[2]}\n"
                             f"Language: {data.one_courses(i)[3]}\n"
                             f"Price: {data.one_courses(i)[4]}\n"
                             f"Description: {data.one_courses(i)[5]}")


@dp.message_handler(text="Курсы (RU)")
async def get_ru_courses(message: types.Message):
    data = RuCourses()
    for i in range(12):
        await message.answer(f"{data.one_courses(i)[0]}\n{data.one_courses(i)[1]}\n"
                             f"Автор: {data.one_courses(i)[2]}\n"
                             f"Язык курса: {data.one_courses(i)[3]}\n"
                             f"Стоимость: {data.one_courses(i)[4]}\n"
                             f"Описание: {data.one_courses(i)[5]}")


@dp.message_handler(text="Курсы (EN)")
async def get_en_courses(message: types.Message):
    data = EnCourses()
    for i in range(12):
        await message.answer(f"{data.one_courses(i)[0]}\n{data.one_courses(i)[1]}\n"
                             f"Author: {data.one_courses(i)[2]}\n"
                             f"Language: {data.one_courses(i)[3]}\n"
                             f"Price: {data.one_courses(i)[4]}\n"
                             f"Description: {data.one_courses(i)[5]}")


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text="Выберите следующую подборку", reply_markup=next_courses)


@dp.callback_query_handler(cours_callback.filter(item_name="ru"))
async def get_next_ru_courses(call: CallbackQuery):
    await call.answer(cache_time=60)
    # logging.info(f"i= {call.data}")
    data = RuCourses()
    for i in range(12):
        await call.message.answer(f"{data.one_courses(i)[0]}\n{data.one_courses(i)[1]}\n"
                                  f"Автор: {data.one_courses(i)[2]}\n"
                                  f"Язык курса: {data.one_courses(i)[3]}\n"
                                  f"Стоимость: {data.one_courses(i)[4]}\n"
                                  f"Описание: {data.one_courses(i)[5]}")


@dp.callback_query_handler(cours_callback.filter(item_name="en"))
async def get_next_en_courses(call: CallbackQuery):
    await call.answer(cache_time=60)
    data = EnCourses()
    for i in range(12):
        await call.message.answer(f"{data.one_courses(i)[0]}\n{data.one_courses(i)[1]}\n"
                                  f"Author: {data.one_courses(i)[2]}\n"
                                  f"Language: {data.one_courses(i)[3]}\n"
                                  f"Price: {data.one_courses(i)[4]}\n"
                                  f"Description: {data.one_courses(i)[5]}")

