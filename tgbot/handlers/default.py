from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.models.role import UserRole


async def admin_start(msg: Message):
    await msg.reply(f"Hello, {msg.from_user.first_name}!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start,
        commands=["start"],
        state="*",
        role=UserRole.DEFAULT,
    )
    # # or you can pass multiple roles:
    # dp.register_message_handler(admin_start, commands=["start"], state="*", role=[UserRole.ADMIN])
    # # or use another filter:
    # dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
