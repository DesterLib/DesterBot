import os
import logging
import asyncio
from dotenv import load_dotenv
from pyrogram import Client, enums, idle

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
admins = []
group_ids = int(os.getenv("GROUP_IDS"))
group_ids = [int(_id) for _id in group_ids.split()]
admin_chat = int(os.getenv("ADMIN_CHAT_ID"))

async def update_admins():
    global admins
    while True:
        logger.info("Updating admins")
        while not bot.is_initialized:
            await asyncio.sleep(5)
        async for chat_member in bot.get_chat_members(group_ids, filter=enums.chat_members_filter.ChatMembersFilter.ADMINISTRATORS):
                if chat_member.user.is_bot:
                    continue
                if chat_member.user.id in admins:
                    continue
                logger.info(f"Adding {chat_member.user.first_name} to admin list")
                admins.append(chat_member.user.id)
        await asyncio.sleep(admin_reload_interval)
    
async def start_bot():
    await bot.start()
    logger.info("Bot started")
    await idle()

async def main():
    await asyncio.gather(start_bot(), update_admins())

if __name__ == '__main__':
    asyncio.run(main())