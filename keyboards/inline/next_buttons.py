from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import cours_callback

next_courses = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=
                                    [
                                        [
                                            InlineKeyboardButton(
                                                text="Следующие (RU)",
                                                callback_data=cours_callback.new(item_name="ru")),
                                            InlineKeyboardButton(
                                                text="Следующие (EN)",
                                                callback_data=cours_callback.new(item_name="en")
                                            )
                                        ],
                                    ],
                                    )
