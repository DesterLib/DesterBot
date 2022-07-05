from pyrogram import Client, filters, emoji
from pyrogram.types import ChatJoinRequest, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from bot import group_id

welcome_txt = """
<b>Hey there {mention},</b>
Thank you for joining our small community.
You'll have to follow some steps before joining our group.
<b>Press the button</b> below to continue.
"""

@Client.on_chat_join_request(filters.chat(group_id))
async def chat_join_request_handler(c: Client, req: ChatJoinRequest):
    await c.send_message(req.from_user.id, welcome_txt.format(mention=req.from_user.mention),
                         reply_markup=InlineKeyboardMarkup(
                             [[InlineKeyboardButton('Continue', callback_data='welcome_1')]]
                         ))

@Client.on_callback_query(filters.regex(r"^welcome_(\d)$"))
async def edit_welcome_message(c: Client, query: CallbackQuery):
    await query.answer()
    if query.matches[0].group(1) == "0":
        await c.decline_chat_join_request(group_id, query.from_user.id)
        txt = "Looks like you ain't fit for this group, have a nice day~"
        buttons = None
    elif query.matches[0].group(1) == "1":
        txt = open("strings/rules.md", "r").read()
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("T&C", url="https://dester.gq/docs/additional-info/terms-and-conditions"), InlineKeyboardButton("Privacy Policy", url='https://dester.gq/docs/additional-info/privacy-policy')],
            [InlineKeyboardButton("✅", callback_data="welcome_2")],
        ])
    elif query.matches[0].group(1) == "2":
        txt = open("strings/asking_for_help.md", "r").read()
        buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("❌", callback_data="welcome_0"),
            InlineKeyboardButton("✅", callback_data="welcome_3"),
        ], [InlineKeyboardButton("Docs", url="dester.gq")]])
    elif query.matches[0].group(1) == "3":
        txt = open("strings/about_community.md", "r").read()
        await c.approve_chat_join_request(group_id, query.from_user.id)
        buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("Visit group", url="https://t.me/dester_community"),
            InlineKeyboardButton("Offtopic Chat", url="https://t.me/+HbStdsIn4yY2NTc0"),
        ]])
    await query.message.edit(text=txt, reply_markup=buttons, disable_web_page_preview=True)