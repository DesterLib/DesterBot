# from bot import group_ids, admins
# from pyrogram.types import Message
# from pyrogram import Client, filters
# from pyrogram.enums.parse_mode import ParseMode

# @Client.on_message(filters.command("ban") & filters.chat(group_ids) & admins)
# async def ban_command_message_handler(c: Client, m: Message):
#     try:
#         if m.reply_to_message:
#             user = m.reply_to_message.sender_chat or m.reply_to_message.from_user
#         else:
#             user = await c.get_users(m.command[1])
#         await c.ban_chat_member(group_ids, user.id)
#         await m.reply_text(f"🔨 {user.mention(style=ParseMode.MARKDOWN)} has been banned!")
#     except Exception as e:
#         await m.reply_text(f"An error occurred: `{e}`")

# @Client.on_message(filters.command("unban") & filters.chat(group_ids) & admins)
# async def unban_command_message_handler(c: Client, m: Message):
#     try:
#         if m.reply_to_message:
#             user = m.reply_to_message.sender_chat or m.reply_to_message.from_user
#         else:
#             user = await c.get_users(m.command[1])
#         await c.unban_chat_member(group_ids, user.id)
#         await m.reply_text(f"✅ {user.mention(style=ParseMode.MARKDOWN)} has been unbanned!")
#     except Exception as e:
#         await m.reply_text(f"An error occurred: `{e}`")

# @Client.on_message(filters.command("admin") & filters.chat(group_ids) & admins)
# async def test_admin_command_message_handler(c: Client, m: Message):
#     await m.reply_text(f"Test successful!")