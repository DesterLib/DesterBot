import os
import logging
import asyncio
from dotenv import load_dotenv
from pyrogram import Client, enums, idle
from pyrogram.errors import ChannelInvalid

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format='[%(asctime)s][%(levelname)s] - %(name)s ==> %(message)s')

logging.getLogger('pyrogram').setLevel(logging.WARNING)
logger = logging.getLogger("bot")

load_dotenv()

bot = Client(
    name="dester_bot",
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN"),
    plugins={"root": "plugins"},
    in_memory=True,
)

admin_reload_interval = int(os.getenv("ADMIN_RELOAD_INTERVAL", 60))
admin_list = []
group_id = int( os.getenv("GROUP_ID"))
admin_chat = int(os.getenv("ADMIN_CHAT_ID"))


async def update_admins():
    global admin_list
    while True:
        while not bot.is_initialized:
            await asyncio.sleep(5)
        try:
            async for chat_member in bot.get_chat_members(group_id, filter=enums.chat_members_filter.ChatMembersFilter.ADMINISTRATORS):
                if chat_member.user.is_bot:
                    continue
                if chat_member.user.id in admin_list:
                    continue
                logger.info(f"Adding {chat_member.user.first_name} to admin list")
                admin_list.append(chat_member.user.id)
        except ChannelInvalid:
            logger.critical("Group ID {} is invalid or bot not added to Group".format(group_id))
            exit(1)
        await asyncio.sleep(admin_reload_interval)
    
async def start_bot():
    await bot.start()
    logger.info("Bot started")
    await idle()

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(update_admins())
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        logger.info("Bot stopped")
        quit()