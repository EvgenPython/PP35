from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery
from keyboards.inline.callback_data import cours_callback
from keyboards.inline.next_buttons import next_courses
from loader import dp
from utils.misc.requ_data import AllCourses, EnCourses, RuCourses
from keyboards.inline.menu_categories import all_categories


@dp.message_handler(Command('cat'))
async def get_all_categories(message: types.Message):
    await message.answer("Выберите категорию:", reply_markup=all_categories)

@dp.callback_query_handler(cours_callback.filter(item_name="ru"))
async def get_next_free_courses(call: CallbackQuery):
    await call.answer(cache_time=60)
    # logging.info(f"i= {call.data}")
    data = FreeCourses()
    for i in range(12):
        await call.message.answer(f"{data.one_courses(i)[0]}\n{data.one_courses(i)[1]}\n"
                                  f"Автор: {data.one_courses(i)[2]}\n"
                                  f"Язык курса: {data.one_courses(i)[3]}\n"
                                  f"Стоимость: {data.one_courses(i)[4]}\n"
                                  f"Описание: {data.one_courses(i)[5]}")