from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config as tg


async def get_fsub(bot, message):
    target_channel_id = tg.FSUB_ID  # Your channel ID
    user_id = message.from_user.id
    try:
        await bot.get_chat_member(target_channel_id, user_id)
    except UserNotParticipant:
        channel_link = (await bot.get_chat(target_channel_id)).invite_link
        join_button = InlineKeyboardButton("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=channel_link)
        keyboard = [[join_button]]
        await message.reply(
            f"<b><blockquote>Dᴇᴀʀ Usᴇʀ {message.from_user.mention}!</blockquote>\n<blockquote>Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊</blockquote>\n<blockquote>Dᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</blockquote></b>",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return False
    else:
        return True
