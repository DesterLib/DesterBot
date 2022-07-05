from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_command_message_handler(_, m: Message):
    await m.reply_text("Hello, I'm a bot!")