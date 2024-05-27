from ANNIEMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🏓🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "ɪᴄʜɪ ᴛʜᴀ ɪᴛᴄʜɪᴛʜᴀ.. ᴇɴ ᴋɴɴᴀᴛʜᴜʟᴀ ɪᴛᴛᴄʜɪ ᴛʜᴀᴀ💕🙈",
          "ᴋᴏɴᴊᴀᴍ ᴜᴛᴛʜᴜ ᴘᴀᴀᴛʜᴀʟᴇ ᴄʜᴇʟʟᴀᴛᴛʜᴜᴋᴋᴜ ᴍᴀɴᴅᴀɪᴋᴜʟᴀ ᴋᴏɴᴊᴀᴍ ᴋɪʀᴜᴋᴜ ᴘᴜᴅɪᴠʜɪᴅᴜᴍ🤭🤭",
          "ᴋᴀᴅʜᴀʟ ꜱᴀᴅᴜɢᴜᴅᴜ.. ᴋᴀɴɴᴇ ᴛʜᴏᴅᴜᴛʜᴏᴅᴜ🙈👀",
          "ᴇᴛʜᴜᴋᴜ ᴘᴏɴᴅᴀᴛɪ ᴇɴɴᴀ ꜱᴜᴛᴛʜɪ ᴠᴀᴘᴘᴀᴛɪ🥳🥳",
          "ᴍᴀɴᴄʜᴀ ᴍᴀᴄʜᴀ ᴜɴ ᴍᴇʟᴀ ᴀꜱʜᴀ ᴠᴀᴄʜᴀ🙈🙈💕",
          "ɢᴀɴᴛʜᴀ ᴋᴀɴɴᴀʟᴀɢᴀ 👀",
          "ᴍᴀʟᴀʏᴀᴀɪ ᴇʟᴜɴᴛʜᴇɴ ɴᴀᴀɴ ɪᴘᴘᴏᴢɢᴜᴛʜᴜ🙈.. ᴍᴀɴᴀʟᴀᴀɪ ᴠɪʟᴜɴᴛʜᴀɪ ɴᴇᴇ ɪᴘᴘᴏᴢʜᴜᴛʜᴜ 🤩🤩",
          "ᴀʟᴀɢᴇ ᴜɴᴀᴛʜᴜ 🙈🙈ᴘᴀᴀʀᴛʜᴇɴ ᴀᴅᴀᴅᴀ 👀👀",
          "ᴜɴᴀᴋᴋᴜʟ ɴᴀᴀɴᴇ ᴜʀᴜɢᴜᴍ ɪʀᴀᴠɪʟ ❤️ ɴᴀᴀɴ ꜱᴏʟᴀᴠᴀ💕💕",
          "ꜱᴀɪᴠᴀ ᴍᴜᴛᴛʜᴀᴍ💋 ᴋᴏᴅᴜᴛᴛʜᴀ ᴏᴛᴛʀᴜ ᴘᴏɢᴀ ᴍᴀᴛᴛᴇɴ.. ꜱᴀɢᴀꜱᴀᴛᴛʜᴀ ᴋᴀᴀᴛᴜ 🙈 ꜱᴇᴛᴛʜᴜ ᴘᴏᴠᴀ ᴍᴀᴛᴇɴ",
          "ꜱɴᴇɢɪᴛʜᴀɴᴇ ꜱɴᴇɢɪᴛʜᴀɴᴇ.. ʀᴀɢᴀꜱɪʏᴀ ꜱɴᴇɢɪᴛʜᴀɴᴇ🙈",
          "ɴᴇᴇ ᴋᴜʟɪᴋᴋᴀʏɪʟ ɴᴀɴᴜᴍ ᴋᴏɴᴊᴀᴍ ɴᴀɴᴀɪᴠᴇɴ 🌚🌝",
          "ᴜɴɴᴀɪ ᴀʟʟɪ ᴇᴅᴜᴛᴛʜᴜ.. ᴜʟʟᴀɴɢᴀʏɪʟ ᴍᴜᴅɪᴛʜᴜ.. ᴋᴀɪᴋᴜᴛᴛᴀʏɪʟ 💕🙈",
          "ᴍᴜɴ ɢᴏʙᴜʀᴀ ᴀᴢʜᴀɢᴀɪ ᴜɴ ᴅʜᴀᴠᴀɴɪ ᴍᴏᴏᴅɪᴛᴀᴛʜᴇ 👀 ᴀɴᴛʜᴀ ʀᴀɢᴀꜱɪʏᴀᴛᴛʜᴀɪ ᴍᴀᴢʜᴀɪᴛʜᴜʟɪ 🙈🙈 ᴀᴀᴋᴋɪʏᴀᴛʜᴇ",
          "ɴᴇɴᴊᴀᴍʙᴀʟᴀᴍ ᴘᴀʟᴜᴛᴛʜᴀᴄʜᴜ ᴀɴɪʟ ᴋɪᴛᴛᴀ ᴋᴏᴅᴜᴛᴛʜᴀᴄʜᴜ👀 ᴀɴɪʟ ɪᴘᴘᴏ ᴛʜᴜᴋᴋɪ ᴋᴜᴛʜɪᴋᴋᴀʟᴀᴍ ✨ ᴘᴀʟʟᴜᴍ ᴘᴀᴛʜɪᴋᴋᴀʟᴀᴍ 🤭",
          "ᴘᴇɴɴᴜʟᴋᴋᴜʟ ɪᴛᴛʜᴀɴᴀɪ ꜱᴜɢᴀᴍᴀ ᴀɴᴛʜᴀ ʙʀᴀᴍᴍᴀɴɪɴ ᴛʜɪʀᴀᴍ ᴠᴀᴀᴢʜɢᴀ✨ ᴇɴᴀᴋᴋᴜʟ ᴛʜᴏᴏɴɢɪʏᴀ ꜱᴜɢᴀᴛᴛʜᴀɪ ɪɴᴅʀᴜ ᴇᴢʜᴜᴘᴘɪʏᴀ ᴠɪʀᴀʟ ᴠᴀᴀᴢʜɢᴀ🥵",
          "ᴅᴇᴇᴘᴀɴɢᴀʟ ᴀɴᴀɪᴘᴘᴀʏʜᴇ 🕯️ ᴘᴜᴛʜɪʏᴀ ᴘᴏʀᴜʟ ɴᴀᴀᴍ ᴛʜᴇᴅᴀᴛᴛʜᴀɴ",
          "ᴠɪᴅᴀᴠᴇɴᴅᴜᴍ ᴀᴄʜᴀᴛᴛʜᴀɪ 🫶🏻 ᴛʜᴏᴅᴀᴠᴇɴᴅᴜᴍ ᴜᴛᴄʜᴀᴛᴛʜᴀɪ 😝 ᴀᴛʜɪɢᴀʟᴀɪ ꜱᴇʟᴀɪ ꜱᴏʟʟᴜᴍᴀᴅɪ ᴍɪᴛᴄʜᴀʏᴛʜᴀɪ 🙈",
          "ᴛʜᴇʀɪɴᴛʜᴀ ʙᴀᴀɢᴀɴɢᴀʟ ᴜʏɪʀᴀɪ ᴛʜᴀɴᴛʜɪᴅᴀ 👀ᴍᴀʀᴀɪɴᴛʜᴀ ʙᴀᴀɢᴀɴɢᴀʟ ᴜʏɪʀᴀɪ ᴠᴀᴀɴɢɪᴅᴀ 😍",
          "ɴᴀᴀ ᴠᴀʏᴀꜱᴜᴋᴋᴜ ᴠᴀɴᴛʜᴀ ᴠᴀʏᴀʟɪɴᴀꜱᴀ 🙈 ᴇɴɴᴀ ᴍɪɴᴏʀ ᴜʜ ᴘᴏʟᴀ ᴠᴀᴀꜱɪʏᴀᴅᴀ 💋",
          "ᴄʜʟᴏ ᴜɴ ᴋᴀᴅɪᴛʜᴀᴛᴛʜᴀɪ ᴘᴏᴏᴠᴀʟᴇ ᴛʜɪʀᴀᴋᴋɪɴᴅʀᴇɴ 😍 ᴠɪʀᴀʟᴘᴀᴛᴛᴀʟ ᴜɴᴛʜᴀɴ ᴊᴇᴇᴠᴀɴ ᴋᴀᴀʏᴀᴍ ᴘᴀᴅᴜᴍᴀɴᴅʀᴏ ✨💕",
          "ᴋᴀɴɴᴇ ᴜɴ ᴋᴀᴀʟ ᴋᴏᴢʜᴜꜱɪʟ ᴍᴀɴɪʏᴀᴀɢᴀ ᴍᴀᴛʀᴇɴᴀ.. ᴍᴀɴᴊᴀᴛᴛʜɪʟ🤔 ᴜʀᴀɴɢᴜᴍʙᴏᴛʜᴜ ꜱɪɴᴜɴɢᴀ ᴍᴀᴛᴇɴᴀ 😍🙈",
          "ᴛʜᴀᴘᴘᴜꜱᴇᴜʏᴀ ᴘᴀᴀʀᴛʜᴀʟ ᴏᴛʀᴜᴋᴏʟᴠᴀᴀʏᴀ 👀 ᴍᴇʟᴀᴀᴅᴀɪ ɴᴇᴇɴɢᴜᴍʙᴏᴛʜᴜ ᴠᴇᴋᴋᴀᴍ ᴇɴɴᴀ ᴍᴜɴᴛʜᴀᴀɴᴀʏᴀᴀʟ ❤️🫶🏻🦋",
          "ꜱᴏᴋᴋɪ ᴛʜᴀᴀɴᴇ ᴘᴏɢɪʀᴇɴ ᴍᴀᴍᴀɴ ᴋᴏɴᴊᴀ ɴᴀᴀʟᴀ",
          "ᴇᴢʜᴜ ᴋᴀᴅᴀʟ ᴛʜᴀᴀɴᴅɪᴛʜᴀᴀɴ ᴇᴢʜᴜ ᴍᴀʟᴀɪ ᴛʜᴀᴀɴᴅɪᴛʜᴀᴀɴ🫶🏻 ᴍᴀᴄʜᴀɴ ᴋɪᴛᴛᴀ ᴏᴅɪ ᴠᴀʀᴜᴍ ᴍᴀɴᴀꜱᴜ ❤️",
          "ᴋᴏᴏʀᴀᴘᴀᴛᴛᴜ ꜱᴇʟᴀ ᴛʜᴀɴ ᴠᴀɴɢᴀ ꜱᴏʟɪ ᴋᴇᴋᴋᴜʀᴇɴ 🙈 ᴋᴏᴏᴅᴜᴠɪᴛᴛᴜ ᴋᴏᴏᴅᴜᴘᴀᴀʏᴜᴍ ᴋᴀᴅʜᴀʟᴀᴀʟᴀ ꜱᴜᴛᴛʜᴜʀᴇɴ 🫶🏻",
          "ᴋᴀɴɴɪʟᴇ ᴋᴀʟᴍɪꜱʜᴀᴍ 👀 ᴘᴏᴛʜᴜᴍᴇ ꜱɪʟᴍɪꜱʜᴀᴍ 🙈 ꜱᴘᴀʀɪꜱʜᴀᴍᴏ ᴛʜᴜʟɪ ᴠɪꜱᴀᴍ 🤩",
          " ᴜᴅᴀʟ ᴠᴀᴢʜɪ ᴀᴍɪʀᴛʜᴀᴍ ᴠᴀᴢʜɪɢɪɴᴅʀᴀᴛʜᴏ 🥵  ᴜʏɪʀ ᴍᴀᴛᴛᴜᴍ ᴘᴜᴛʜᴜᴠɪᴛʜᴀ ᴠᴀᴢʜɪ ᴋᴀɴᴅᴀᴛʜᴏ 👀",
          "ᴍᴜᴛᴛʜᴀᴍᴛʜɪɴʙᴀᴠᴀᴍ 💋 ᴍᴜʀᴀᴛᴛᴜ ᴘᴏᴏ ɪᴠᴀʟ 🥵 ᴅʜɪɴᴀᴍᴜᴍ ᴛʜᴏʀᴘᴀᴠᴀᴍ ✨ ᴀɴᴛʜᴀ ᴀᴀᴅᴀɪ ꜱᴀɴᴅᴀʏɪʟ 🌚",
          "ɢᴀɴᴅʜᴀ ᴋᴀɴɴᴀʟᴀɢɪ👀ᴛᴀᴋᴋᴜɴᴜᴛʜᴀ ᴛᴀᴛᴛɪ ᴛʜᴜᴋᴋᴜᴍ ᴍᴜᴛᴛʜᴜ ᴘᴀʟʟᴀʟᴀɢɪ 🌝 ᴍᴜᴛᴛʜᴀᴍ ᴏɴɴᴜ ᴛʜᴀᴅɪ 💋",
          "ᴊɪʟʟᴜ ᴊɪʟʟᴜ ᴊɪɢᴀʀᴜᴅᴀɴᴅᴀ ᴋɪᴛᴛᴀᴠᴀᴅɪ 🙈 ᴜɴɴᴀ ᴀᴘᴘᴅɪʏᴇ ꜱᴀᴘᴘɪᴅᴜᴠᴇɴ ɢᴇᴛᴛʜᴀ ᴛʜᴀᴀɴᴅɪ 🥳",
           ]

VC_TAG = ["ɪᴄʜɪ ᴛʜᴀ ɪᴛᴄʜɪᴛʜᴀ.. ᴇɴ ᴋɴɴᴀᴛʜᴜʟᴀ ɪᴛᴛᴄʜɪ ᴛʜᴀᴀ💕🙈",
          "ᴋᴏɴᴊᴀᴍ ᴜᴛᴛʜᴜ ᴘᴀᴀᴛʜᴀʟᴇ ᴄʜᴇʟʟᴀᴛᴛʜᴜᴋᴋᴜ ᴍᴀɴᴅᴀɪᴋᴜʟᴀ ᴋᴏɴᴊᴀᴍ ᴋɪʀᴜᴋᴜ ᴘᴜᴅɪᴠʜɪᴅᴜᴍ🤭🤭",
          "ᴋᴀᴅʜᴀʟ ꜱᴀᴅᴜɢᴜᴅᴜ.. ᴋᴀɴɴᴇ ᴛʜᴏᴅᴜᴛʜᴏᴅᴜ🙈👀",
          "ᴇᴛʜᴜᴋᴜ ᴘᴏɴᴅᴀᴛɪ ᴇɴɴᴀ ꜱᴜᴛᴛʜɪ ᴠᴀᴘᴘᴀᴛɪ🥳🥳",
          "ᴍᴀɴᴄʜᴀ ᴍᴀᴄʜᴀ ᴜɴ ᴍᴇʟᴀ ᴀꜱʜᴀ ᴠᴀᴄʜᴀ🙈🙈💕",
          "ɢᴀɴᴛʜᴀ ᴋᴀɴɴᴀʟᴀɢᴀ 👀",
          "ᴍᴀʟᴀʏᴀᴀɪ ᴇʟᴜɴᴛʜᴇɴ ɴᴀᴀɴ ɪᴘᴘᴏᴢɢᴜᴛʜᴜ🙈.. ᴍᴀɴᴀʟᴀᴀɪ ᴠɪʟᴜɴᴛʜᴀɪ ɴᴇᴇ ɪᴘᴘᴏᴢʜᴜᴛʜᴜ 🤩🤩",
          "ᴀʟᴀɢᴇ ᴜɴᴀᴛʜᴜ 🙈🙈ᴘᴀᴀʀᴛʜᴇɴ ᴀᴅᴀᴅᴀ 👀👀",
          "ᴜɴᴀᴋᴋᴜʟ ɴᴀᴀɴᴇ ᴜʀᴜɢᴜᴍ ɪʀᴀᴠɪʟ ❤️ ɴᴀᴀɴ ꜱᴏʟᴀᴠᴀ💕💕",
          "ꜱᴀɪᴠᴀ ᴍᴜᴛᴛʜᴀᴍ💋 ᴋᴏᴅᴜᴛᴛʜᴀ ᴏᴛᴛʀᴜ ᴘᴏɢᴀ ᴍᴀᴛᴛᴇɴ.. ꜱᴀɢᴀꜱᴀᴛᴛʜᴀ ᴋᴀᴀᴛᴜ 🙈 ꜱᴇᴛᴛʜᴜ ᴘᴏᴠᴀ ᴍᴀᴛᴇɴ",
          "ꜱɴᴇɢɪᴛʜᴀɴᴇ ꜱɴᴇɢɪᴛʜᴀɴᴇ.. ʀᴀɢᴀꜱɪʏᴀ ꜱɴᴇɢɪᴛʜᴀɴᴇ🙈",
          "ɴᴇᴇ ᴋᴜʟɪᴋᴋᴀʏɪʟ ɴᴀɴᴜᴍ ᴋᴏɴᴊᴀᴍ ɴᴀɴᴀɪᴠᴇɴ 🌚🌝",
          "ᴜɴɴᴀɪ ᴀʟʟɪ ᴇᴅᴜᴛᴛʜᴜ.. ᴜʟʟᴀɴɢᴀʏɪʟ ᴍᴜᴅɪᴛʜᴜ.. ᴋᴀɪᴋᴜᴛᴛᴀʏɪʟ 💕🙈",
          "ᴍᴜɴ ɢᴏʙᴜʀᴀ ᴀᴢʜᴀɢᴀɪ ᴜɴ ᴅʜᴀᴠᴀɴɪ ᴍᴏᴏᴅɪᴛᴀᴛʜᴇ 👀 ᴀɴᴛʜᴀ ʀᴀɢᴀꜱɪʏᴀᴛᴛʜᴀɪ ᴍᴀᴢʜᴀɪᴛʜᴜʟɪ 🙈🙈 ᴀᴀᴋᴋɪʏᴀᴛʜᴇ",
          "ɴᴇɴᴊᴀᴍʙᴀʟᴀᴍ ᴘᴀʟᴜᴛᴛʜᴀᴄʜᴜ ᴀɴɪʟ ᴋɪᴛᴛᴀ ᴋᴏᴅᴜᴛᴛʜᴀᴄʜᴜ👀 ᴀɴɪʟ ɪᴘᴘᴏ ᴛʜᴜᴋᴋɪ ᴋᴜᴛʜɪᴋᴋᴀʟᴀᴍ ✨ ᴘᴀʟʟᴜᴍ ᴘᴀᴛʜɪᴋᴋᴀʟᴀᴍ 🤭",
          "ᴘᴇɴɴᴜʟᴋᴋᴜʟ ɪᴛᴛʜᴀɴᴀɪ ꜱᴜɢᴀᴍᴀ ᴀɴᴛʜᴀ ʙʀᴀᴍᴍᴀɴɪɴ ᴛʜɪʀᴀᴍ ᴠᴀᴀᴢʜɢᴀ✨ ᴇɴᴀᴋᴋᴜʟ ᴛʜᴏᴏɴɢɪʏᴀ ꜱᴜɢᴀᴛᴛʜᴀɪ ɪɴᴅʀᴜ ᴇᴢʜᴜᴘᴘɪʏᴀ ᴠɪʀᴀʟ ᴠᴀᴀᴢʜɢᴀ🥵",
          "ᴅᴇᴇᴘᴀɴɢᴀʟ ᴀɴᴀɪᴘᴘᴀʏʜᴇ 🕯️ ᴘᴜᴛʜɪʏᴀ ᴘᴏʀᴜʟ ɴᴀᴀᴍ ᴛʜᴇᴅᴀᴛᴛʜᴀɴ",
          "ᴠɪᴅᴀᴠᴇɴᴅᴜᴍ ᴀᴄʜᴀᴛᴛʜᴀɪ 🫶🏻 ᴛʜᴏᴅᴀᴠᴇɴᴅᴜᴍ ᴜᴛᴄʜᴀᴛᴛʜᴀɪ 😝 ᴀᴛʜɪɢᴀʟᴀɪ ꜱᴇʟᴀɪ ꜱᴏʟʟᴜᴍᴀᴅɪ ᴍɪᴛᴄʜᴀʏᴛʜᴀɪ 🙈",
          "ᴛʜᴇʀɪɴᴛʜᴀ ʙᴀᴀɢᴀɴɢᴀʟ ᴜʏɪʀᴀɪ ᴛʜᴀɴᴛʜɪᴅᴀ 👀ᴍᴀʀᴀɪɴᴛʜᴀ ʙᴀᴀɢᴀɴɢᴀʟ ᴜʏɪʀᴀɪ ᴠᴀᴀɴɢɪᴅᴀ 😍",
          "ɴᴀᴀ ᴠᴀʏᴀꜱᴜᴋᴋᴜ ᴠᴀɴᴛʜᴀ ᴠᴀʏᴀʟɪɴᴀꜱᴀ 🙈 ᴇɴɴᴀ ᴍɪɴᴏʀ ᴜʜ ᴘᴏʟᴀ ᴠᴀᴀꜱɪʏᴀᴅᴀ 💋",
          "ᴄʜʟᴏ ᴜɴ ᴋᴀᴅɪᴛʜᴀᴛᴛʜᴀɪ ᴘᴏᴏᴠᴀʟᴇ ᴛʜɪʀᴀᴋᴋɪɴᴅʀᴇɴ 😍 ᴠɪʀᴀʟᴘᴀᴛᴛᴀʟ ᴜɴᴛʜᴀɴ ᴊᴇᴇᴠᴀɴ ᴋᴀᴀʏᴀᴍ ᴘᴀᴅᴜᴍᴀɴᴅʀᴏ ✨💕",
          "ᴋᴀɴɴᴇ ᴜɴ ᴋᴀᴀʟ ᴋᴏᴢʜᴜꜱɪʟ ᴍᴀɴɪʏᴀᴀɢᴀ ᴍᴀᴛʀᴇɴᴀ.. ᴍᴀɴᴊᴀᴛᴛʜɪʟ🤔 ᴜʀᴀɴɢᴜᴍʙᴏᴛʜᴜ ꜱɪɴᴜɴɢᴀ ᴍᴀᴛᴇɴᴀ 😍🙈",
          "ᴛʜᴀᴘᴘᴜꜱᴇᴜʏᴀ ᴘᴀᴀʀᴛʜᴀʟ ᴏᴛʀᴜᴋᴏʟᴠᴀᴀʏᴀ 👀 ᴍᴇʟᴀᴀᴅᴀɪ ɴᴇᴇɴɢᴜᴍʙᴏᴛʜᴜ ᴠᴇᴋᴋᴀᴍ ᴇɴɴᴀ ᴍᴜɴᴛʜᴀᴀɴᴀʏᴀᴀʟ ❤️🫶🏻🦋",
          "ꜱᴏᴋᴋɪ ᴛʜᴀᴀɴᴇ ᴘᴏɢɪʀᴇɴ ᴍᴀᴍᴀɴ ᴋᴏɴᴊᴀ ɴᴀᴀʟᴀ",
          "ᴇᴢʜᴜ ᴋᴀᴅᴀʟ ᴛʜᴀᴀɴᴅɪᴛʜᴀᴀɴ ᴇᴢʜᴜ ᴍᴀʟᴀɪ ᴛʜᴀᴀɴᴅɪᴛʜᴀᴀɴ🫶🏻 ᴍᴀᴄʜᴀɴ ᴋɪᴛᴛᴀ ᴏᴅɪ ᴠᴀʀᴜᴍ ᴍᴀɴᴀꜱᴜ ❤️",
          "ᴋᴏᴏʀᴀᴘᴀᴛᴛᴜ ꜱᴇʟᴀ ᴛʜᴀɴ ᴠᴀɴɢᴀ ꜱᴏʟɪ ᴋᴇᴋᴋᴜʀᴇɴ 🙈 ᴋᴏᴏᴅᴜᴠɪᴛᴛᴜ ᴋᴏᴏᴅᴜᴘᴀᴀʏᴜᴍ ᴋᴀᴅʜᴀʟᴀᴀʟᴀ ꜱᴜᴛᴛʜᴜʀᴇɴ 🫶🏻",
          "ᴋᴀɴɴɪʟᴇ ᴋᴀʟᴍɪꜱʜᴀᴍ 👀 ᴘᴏᴛʜᴜᴍᴇ ꜱɪʟᴍɪꜱʜᴀᴍ 🙈 ꜱᴘᴀʀɪꜱʜᴀᴍᴏ ᴛʜᴜʟɪ ᴠɪꜱᴀᴍ 🤩",
          " ᴜᴅᴀʟ ᴠᴀᴢʜɪ ᴀᴍɪʀᴛʜᴀᴍ ᴠᴀᴢʜɪɢɪɴᴅʀᴀᴛʜᴏ 🥵  ᴜʏɪʀ ᴍᴀᴛᴛᴜᴍ ᴘᴜᴛʜᴜᴠɪᴛʜᴀ ᴠᴀᴢʜɪ ᴋᴀɴᴅᴀᴛʜᴏ 👀",
          "ᴍᴜᴛᴛʜᴀᴍᴛʜɪɴʙᴀᴠᴀᴍ 💋 ᴍᴜʀᴀᴛᴛᴜ ᴘᴏᴏ ɪᴠᴀʟ 🥵 ᴅʜɪɴᴀᴍᴜᴍ ᴛʜᴏʀᴘᴀᴠᴀᴍ ✨ ᴀɴᴛʜᴀ ᴀᴀᴅᴀɪ ꜱᴀɴᴅᴀʏɪʟ 🌚",
          "ɢᴀɴᴅʜᴀ ᴋᴀɴɴᴀʟᴀɢɪ👀ᴛᴀᴋᴋᴜɴᴜᴛʜᴀ ᴛᴀᴛᴛɪ ᴛʜᴜᴋᴋᴜᴍ ᴍᴜᴛᴛʜᴜ ᴘᴀʟʟᴀʟᴀɢɪ 🌝 ᴍᴜᴛᴛʜᴀᴍ ᴏɴɴᴜ ᴛʜᴀᴅɪ 💋",
          "ᴊɪʟʟᴜ ᴊɪʟʟᴜ ᴊɪɢᴀʀᴜᴅᴀɴᴅᴀ ᴋɪᴛᴛᴀᴠᴀᴅɪ 🙈 ᴜɴɴᴀ ᴀᴘᴘᴅɪʏᴇ ꜱᴀᴘᴘɪᴅᴜᴠᴇɴ ɢᴇᴛᴛʜᴀ ᴛʜᴀᴀɴᴅɪ 🥳",
        ]


@app.on_message(filters.command(["heartbeat", "honeymoon" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/heartbeat ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/heartbeat ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/heartbeat ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["honeymoon"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["cancel", "cancel"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")
          
