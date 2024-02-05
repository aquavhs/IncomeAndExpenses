import asyncio

from aiogram.filters import CommandStart
from aiogram.types import Message

from TGBOT.handlers import start_handler
from TGBOT.settings.config import bot, dp
from TGBOT.settings.database import createdbx, add_user_data, is_user_in_table




async def main():
    dp.include_router(start_handler.router)
    createdbx()
    await dp.start_polling(bot)


# Start the bot with skip_updates set to True
if __name__ == '__main__':
    asyncio.run(main())