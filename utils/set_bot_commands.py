from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("all", "Смотреть курсы"),
            types.BotCommand("items", "Смотреть следующие"),
            types.BotCommand("cat", "Выбрать категорию"),
            types.BotCommand("help", "Вывести справку"),
        ]
    )
