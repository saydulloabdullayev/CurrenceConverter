import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.enums import ParseMode
from handlers.command_handlers import command_router



async def main():
    bot=Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    dp= Dispatcher()
    dp.include_router(command_router)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print('Bot stopped')


