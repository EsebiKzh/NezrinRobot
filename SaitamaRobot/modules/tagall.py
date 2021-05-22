from pyrogram import filters

from SaitamaRobot.pyrogramee.pluginshelper import admins_only, get_text
from SaitamaRobot import pbot


@pbot.on_message(filters.command("tagall") & ~filters.edited & ~filters.bot)
@admins_only
async def tagall(client, message):
    await message.reply("✅`Tağ Prosesi Başladı...`")
    chat_id = message.chat.id
    string = ""
    limit = 100
    icm = client.iter_chat_members(message.chat.id)
    async for member in icm:
        tag = member.user.mention
        if limit <= 8:
            if tag != None:
                string += f"👤{tag}\n"
            else:
                string += f"{member.user.mention}\n"
            limit += 100
        else:
            await client.send_message(chat_id, text=string)
            limit = 100
            string = ""
            

__mod_name__ = "🖇️Tağ"
__help__ = """
- /tagall : Hərkəsi tağ edər
"""
