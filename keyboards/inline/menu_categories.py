from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import cours_callback

all_categories = InlineKeyboardMarkup(row_width=3,
                                      inline_keyboard=
                                      [
                                          [InlineKeyboardButton(
                                              text="Бесплатно",
                                              callback_data=cours_callback.new(item_name="en")),
                                              InlineKeyboardButton(
                                                  text="Business",
                                                  callback_data=cours_callback.new(item_name="ru")),
                                              InlineKeyboardButton(
                                                  text="Design",
                                                  callback_data=cours_callback.new(item_name="en"))
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text="Development",
                                                  callback_data=cours_callback.new(item_name="en")),
                                              InlineKeyboardButton(
                                                  text="IT & Software",
                                                  callback_data=cours_callback.new(item_name="en")),
                                              InlineKeyboardButton(
                                                  text="Marketing",
                                                  callback_data=cours_callback.new(item_name="en"))
                                          ]
                                      ],
                                      )
