import asyncio
import datetime
from ANNIEMUSIC import app
from pyrogram import Client
from config import START_IMG_URL
from ANNIEMUSIC.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MESSAGE = f"""
[𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝞑𝘌𝘈𝘛𝂬♡𝂬𝘿𝘙𝘜𝘎𝘡▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/{app.username})
𝐈𝔰 𝔞 𝐒𝔪𝔞𝔯𝔱 𝐏𝔯𝔬 ⚡️ 𝐌𝔲𝔰𝔦𝔠 𝐁𝔬𝔱 🦋

❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎

💕 𝐏𝔯𝔬 𝐅𝔢𝔞𝔱𝔲𝔯𝔢𝔰 🦋

♫︎🌹 𝐅𝔲𝔫 𝐓𝔞𝔤𝔰 🥂
♫︎🌹 𝐖𝔢𝔩𝔠𝔬𝔪𝔢 𝐆𝔯𝔢𝔢𝔱𝔦𝔫𝔤 💐
♫︎🌹 𝐋𝔢𝔣𝔱 𝐍𝔬𝔱𝔢 🍾
♫︎🌹 𝐕𝔠 𝐈𝔫𝔳𝔦𝔱𝔢 𝐂𝔞𝔯𝔡 🎉
♫︎🌹 𝐕𝔦𝔡𝔢𝔬 𝐃𝔬𝔴𝔫𝔩𝔬𝔞𝔡 📹 
♫︎🌹 𝐀𝔲𝔡𝔦𝔬 𝐃𝔬𝔴𝔫𝔩𝔬𝔞𝔡 🎶

♫︎🌹 𝐒𝔲𝔭𝔭𝔬𝔯𝔯 𝐋𝔦𝔳𝔢 𝐒𝔱𝔯𝔢𝔞𝔪 𝔞𝔫𝔡 𝐘𝔬𝔲𝔱𝔲𝔟𝔢 𝐒𝔱𝔯𝔢𝔞𝔪𝔰 🥳 
♫︎🌹 𝐌𝔬𝔳𝔦𝔢 & 𝐕𝔦𝔡𝔢𝔬 𝐒𝔱𝔯𝔢𝔞𝔪𝔦𝔫𝔤 24x7 💝

❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎

♫︎🏓 𝐏𝔩𝔞𝔶 + 𝐕𝔭𝔩𝔞𝔶 + 𝐒𝔱𝔯𝔢𝔞𝔪

♫︎🏓 𝐓𝔞𝔤𝔞𝔩𝔩 + 𝐌𝔢𝔫𝔱𝔦𝔬𝔫 + 𝐆𝔪𝔱𝔞𝔤
♫︎🏓 𝐆𝔫𝔱𝔞𝔤 + 𝐕𝔠𝔱𝔞𝔤 + 𝐋𝔬𝔳𝔢𝔱𝔞𝔤
♫︎🏓 𝐒𝔦𝔫𝔤𝔩𝔢 + 𝐇𝔢𝔞𝔯𝔱𝔟𝔢𝔞𝔱 + 𝐇𝔬𝔫𝔢𝔶𝔪𝔬𝔬𝔫
♫︎🏓 𝐂𝔬𝔲𝔭𝔩𝔢𝔰 + 𝐓𝔞𝔪𝔦𝔩𝔱𝔞𝔤

❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎

💕 𝐍єтωσяк 🦋
[𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/HeartBeat_Muzic)

❥︎─♡︎𝕰𝖓𝖏𝖔𝖞 𝕿𝖍𝖊 𝕯𝖗𝖚𝖌𝖟♡︎─❦︎
"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("💕 𝐄𝔫𝔫𝔞 𝐄𝔡𝔲𝔱𝔱𝔥𝔲𝔨𝔬 🦋", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)  # Sleep for 1 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats
async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(180000)  # Sleep (180000 seconds) between next broadcast

# Start the continuous broadcast loop
asyncio.create_task(continuous_broadcast())
