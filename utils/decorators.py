import logging
import traceback
from bot import admins
from functools import wraps
from pyrogram import Client
from pyrogram.types import Message

def admins(func):
    @wraps(func)
    async def check_admin(client: Client, message: Message, *args, **kwargs):
        try:
            user = message.sender_chat or message.from_user
            if user.id in admins:
                return await func(client, message, *args, **kwargs)
            else:
                await message.reply("🔒 You're not authorized to use me!")
        except Exception as err:
            logging.error(err.with_traceback())
            logging.error(traceback.format_exc())
            raise err
    return check_admin