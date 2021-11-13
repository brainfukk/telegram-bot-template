import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.core.config import TELEGRAM_BOT_API_TOKEN

bot = Bot(token=TELEGRAM_BOT_API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def send_message(chat_id: int, text: str, reply_markup):
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)


def sync_send_message(chat_id, text, reply_markup):
    return asyncio.run(send_message(chat_id, text, reply_markup))
