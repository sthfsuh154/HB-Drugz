import asyncio
import datetime
from ANNIEMUSIC import app
from pyrogram import Client
from config import START_IMG_URL
from ANNIEMUSIC.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MESSAGE = f"""
[𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝞑𝘌𝘈𝘛𝂬♡𝂬𝘿𝘙𝘜𝘎𝘡▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/{app.username})
 𝐈ѕ α 𝐒мαят 𝐏яσ ⚡️ 𝐌υѕιᴄ 𝐁σт 🦋

❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎

💕 𝐏яσ 𝐅єαтυяєѕ 🦋

♫︎🌹 𝐅υη 𝐓αgѕ 🥂
♫︎🌹 𝐖єʟᴄσмє 𝐆яєєтιηg 💐
♫︎🌹 𝐋єƒт 𝐍σтє 🍾
♫︎🌹 𝐕ᴄ 𝐈ηνιтє 𝐂αя∂ 🎉
♫︎🌹 𝐕ι∂єσ 𝐃σωηʟσα∂ 📹 
♫︎🌹 𝐀υ∂ισ 𝐃σωηʟσα∂ 🎶

♫︎🌹 𝐒υρρσят 𝐋ινє 𝐒тяєαм αη∂ 𝐘συтυвє 𝐒тяєαмѕ 🥳 
♫︎🌹 𝐌σνιє & 𝐕ι∂єσ 𝐒тяєαмιηg 24x7 💝

❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎

♫︎🏓 𝐏ʟαу + 𝐕ρʟαу + 𝐒тяєαм
    ( /play /vplay /stream )

♫︎🏓 𝐓αgαʟʟ + 𝐌єηтιση + 𝐆мтαg
     ( /tagall /mention /gmtag )
♫︎🏓 𝐆ηтαg + 𝐕ᴄтαg + 𝐋σνєтαg
     ( /gntag /vctag /lovetag )
♫︎🏓 𝐒ιηgʟє + 𝐇єαятвєαт + 𝐇σηєумσση
     ( /single /heartbeat /honeymoon )
♫︎🏓 𝐂συρʟєѕ + 𝐓αмιʟтαg
     ( /couples /tamiltag )

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
