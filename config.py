import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials - Get these from the Telegram API website
API_ID = int(getenv("API_ID",8045459))
API_HASH = getenv("API_HASH", "e6d1f09120e17a4372fe022dde88511b")
BOT_TOKEN = getenv("BOT_TOKEN", "2096983652:AAFxrSQZQRCp3jbuzbxUOKOhBqOf1aLRDoc")

# Specify where to get the following credentials
OWNER_USERNAME = getenv("OWNER_USERNAME","rajeshrakis")
BOT_USERNAME = getenv("BOT_USERNAME", "thedakkidaikathaval_bot")
BOT_NAME = getenv("BOT_NAME", "𝞖𝘌𝘈𝘙𝘛𝞑𝘌𝘈𝘛𝂬♡𝂬𝘿𝘙𝘜𝘎𝘡")
ASSUSERNAME = getenv("ASSUSERNAME", "ice_babygirl")
EVALOP = list(map(int, getenv("EVALOP", "5059737154").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://zewdatabase:ijoXgdmQ0NCyg9DO@zewgame.urb3i.mongodb.net/ontap?retryWrites=true&w=majority")
LOGGER_ID = int(getenv("LOGGER_ID", -1001735663878))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# External APIs - Get these from their respective providers
GPT_API = getenv("GPT_API", "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")
PLAYHT_API = getenv("PLAYHT_API", "22e323f342024c0fb4ee430eeb9d0011")
OWNER_ID = int(getenv("OWNER_ID", 1281282633))

# Heroku deployment settings - Refer to Heroku documentation on how to obtain these
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/rajeshrakis/HB-Drugz")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support and contact information - Provide your own support channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HeartBeat_Offi")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/HeartBeat_Muzic")

# Server limits and configurations - These can be set based on your server configurations
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# External service credentials - Obtain these from Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# Telegram file size limits - Set these according to your requirements
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Pyrogram session strings - You need to generate these yourself
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot introduction messages - These can be customized as per your preference
AMBOT = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "🦋", "🕊️", "🦋", "🦋", "🦋", "🪄", "💌", "🦋", "🦋", "🧨"
]

AMOP = [
    "𝐇𝔢𝔩𝔩𝔬 {0} ~\n\n💕 𝐓𝔥𝔦𝔰 𝐈𝔰 {1} \n 𝔞 𝐒𝔪𝔞𝔯𝔱 𝐏𝔯𝔬 ⚡️ 𝐌𝔲𝔰𝔦𝔠 𝐁𝔬𝔱 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐏𝔯𝔬 𝐅𝔢𝔞𝔱𝔲𝔯𝔢𝔰 🦋\n\n♫︎🌹 𝐅𝔲𝔫 𝐓𝔞𝔤𝔰  🥂 \n\n♫︎🌹 𝐖𝔢𝔩𝔠𝔬𝔪𝔢 𝐆𝔯𝔢𝔢𝔱𝔦𝔫𝔤 💐 \n\n♫︎🌹 𝐋𝔢𝔣𝔱 𝐍𝔬𝔱𝔢 🍾 \n\n♫︎🌹 𝐕𝔠 𝐈𝔫𝔳𝔦𝔱𝔢 𝐂𝔞𝔯𝔡 🎉 \n\n♫︎🌹 𝐕𝔦𝔡𝔢𝔬 𝐃𝔬𝔴𝔫𝔩𝔬𝔞𝔡 📹 \n\n♫︎🌹 𝐀𝔲𝔡𝔦𝔬 𝐃𝔬𝔴𝔫𝔩𝔬𝔞𝔡 🎶 \n\n♫︎🌹 𝐒𝔲𝔭𝔭𝔬𝔯𝔯 𝐋𝔦𝔳𝔢 𝐒𝔱𝔯𝔢𝔞𝔪 𝔞𝔫𝔡 𝐘𝔬𝔲𝔱𝔲𝔟𝔢 𝐒𝔱𝔯𝔢𝔞𝔪𝔰 🥳 \n\n♫︎🌹 𝐌𝔬𝔳𝔦𝔢 & 𝐕𝔦𝔡𝔢𝔬 𝐒𝔱𝔯𝔢𝔞𝔪𝔦𝔫𝔤 24x7 💝 \n\n 💕 𝐌𝔞𝔨𝔢 𝐌𝔢 𝐀𝔡𝔪𝔦𝔫 𝔞𝔫𝔡 𝐄𝔫𝔧𝔬𝔶 𝐌𝔬𝔯𝔢 𝐅𝔢𝔞𝔱𝔲𝔯𝔢𝔰 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐍𝔢𝔱𝔴𝔬𝔯𝔨 🦋 [𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/HeartBeat_Muzic)",
    "𝐇𝔢𝔩𝔩𝔬 {0} ~\n\n💕 𝐓𝔥𝔦𝔰 𝐈𝔰 {1} \n 𝔞 𝐒𝔪𝔞𝔯𝔱 𝐏𝔯𝔬 ⚡️ 𝐌𝔲𝔰𝔦𝔠 𝐁𝔬𝔱 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐏𝔯𝔬 𝐅𝔢𝔞𝔱𝔲𝔯𝔢𝔰 🦋\n\n♫︎🌹 𝐅𝔲𝔫 𝐓𝔞𝔤𝔰  🥂 \n\n♫︎🌹 𝐖𝔢𝔩𝔠𝔬𝔪𝔢 𝐆𝔯𝔢𝔢𝔱𝔦𝔫𝔤 💐 \n\n♫︎🌹 𝐋𝔢𝔣𝔱 𝐍𝔬𝔱𝔢 🍾 \n\n♫︎🌹 𝐕𝔠 𝐈𝔫𝔳𝔦𝔱𝔢 𝐂𝔞𝔯𝔡 🎉 \n\n♫︎🌹 𝐕𝔦𝔡𝔢𝔬 𝐃𝔬𝔴𝔫𝔩𝔬𝔞𝔡 📹 \n\n♫︎🌹 𝐀𝔲𝔡𝔦𝔬 𝐃𝔬𝔴𝔫𝔩𝔬𝔞𝔡 🎶 \n\n♫︎🌹 𝐒𝔲𝔭𝔭𝔬𝔯𝔯 𝐋𝔦𝔳𝔢 𝐒𝔱𝔯𝔢𝔞𝔪 𝔞𝔫𝔡 𝐘𝔬𝔲𝔱𝔲𝔟𝔢 𝐒𝔱𝔯𝔢𝔞𝔪𝔰 🥳 \n\n♫︎🌹 𝐌𝔬𝔳𝔦𝔢 & 𝐕𝔦𝔡𝔢𝔬 𝐒𝔱𝔯𝔢𝔞𝔪𝔦𝔫𝔤 24x7 💝 \n\n 💕 𝐌𝔞𝔨𝔢 𝐌𝔢 𝐀𝔡𝔪𝔦𝔫 𝔞𝔫𝔡 𝐄𝔫𝔧𝔬𝔶 𝐌𝔬𝔯𝔢 𝐅𝔢𝔞𝔱𝔲𝔯𝔢𝔰 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n♫︎💕 𝐏𝔩𝔞𝔶 + 𝐕𝔭𝔩𝔞𝔶 + 𝐒𝔱𝔯𝔢𝔞𝔪 \n\n♫︎💕 𝐓𝔞𝔤𝔞𝔩𝔩 + 𝐌𝔢𝔫𝔱𝔦𝔬𝔫 + 𝐆𝔪𝔱𝔞𝔤 \n\n♫︎💕 𝐆𝔫𝔱𝔞𝔤 + 𝐕𝔠𝔱𝔞𝔤 + 𝐋𝔬𝔳𝔢𝔱𝔞𝔤 \n\n♫︎💕 𝐒𝔦𝔫𝔤𝔩𝔢 + 𝐇𝔢𝔞𝔯𝔱𝔟𝔢𝔞𝔱 + 𝐇𝔬𝔫𝔢𝔶𝔪𝔬𝔬𝔫 \n\n♫︎💕 𝐂𝔬𝔲𝔭𝔩𝔢𝔰 + 𝐓𝔞𝔪𝔦𝔩𝔱𝔞𝔤 \n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐍𝔢𝔱𝔴𝔬𝔯𝔨 🦋 [𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/HeartBeat_Muzic)",
    "𝐇𝔢𝔩𝔩𝔬 {0} ~\n\n💕 𝐓𝔥𝔦𝔰 𝐈𝔰 {1} \n 𝔞 𝐒𝔪𝔞𝔯𝔱 𝐏𝔯𝔬 ⚡️ 𝐌𝔲𝔰𝔦𝔠 𝐁𝔬𝔱 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐏𝔯𝔬 𝐅𝔢𝔞𝔱𝔲𝔯𝔢𝔰 🦋\n\n♫︎🌹 𝐅𝔲𝔫 𝐓𝔞𝔤𝔰  🥂 \n\n♫︎🌹 𝐖𝔢𝔩𝔠𝔬𝔪𝔢 𝐆𝔯𝔢𝔢𝔱𝔦𝔫𝔤 💐 \n\n♫︎🌹 𝐋𝔢𝔣𝔱 𝐍𝔬𝔱𝔢 🍾 \n\n♫︎🌹 𝐕𝔠 𝐈𝔫𝔳𝔦𝔱𝔢 𝐂𝔞𝔯𝔡 🎉 \n\n♫︎🌹 𝐕𝔦𝔡𝔢𝔬 𝐃𝔬𝔴𝔫𝔩𝔬𝔞𝔡 📹 \n\n♫︎🌹 𝐀𝔲𝔡𝔦𝔬 𝐃𝔬𝔴𝔫𝔩𝔬𝔞𝔡 🎶 \n\n♫︎🌹 𝐒𝔲𝔭𝔭𝔬𝔯𝔯 𝐋𝔦𝔳𝔢 𝐒𝔱𝔯𝔢𝔞𝔪 𝔞𝔫𝔡 𝐘𝔬𝔲𝔱𝔲𝔟𝔢 𝐒𝔱𝔯𝔢𝔞𝔪𝔰 🥳 \n\n♫︎🌹 𝐌𝔬𝔳𝔦𝔢 & 𝐕𝔦𝔡𝔢𝔬 𝐒𝔱𝔯𝔢𝔞𝔪𝔦𝔫𝔤 24x7 💝 \n\n 💕 𝐌𝔞𝔨𝔢 𝐌𝔢 𝐀𝔡𝔪𝔦𝔫 𝔞𝔫𝔡 𝐄𝔫𝔧𝔬𝔶 𝐌𝔬𝔯𝔢 𝐅𝔢𝔞𝔱𝔲𝔯𝔢𝔰 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n♫︎💕 𝐏𝔩𝔞𝔶 + 𝐕𝔭𝔩𝔞𝔶 + 𝐒𝔱𝔯𝔢𝔞𝔪 \n\n♫︎💕 𝐓𝔞𝔤𝔞𝔩𝔩 + 𝐌𝔢𝔫𝔱𝔦𝔬𝔫 + 𝐆𝔪𝔱𝔞𝔤 \n\n♫︎💕 𝐆𝔫𝔱𝔞𝔤 + 𝐕𝔠𝔱𝔞𝔤 + 𝐋𝔬𝔳𝔢𝔱𝔞𝔤 \n\n♫︎💕 𝐒𝔦𝔫𝔤𝔩𝔢 + 𝐇𝔢𝔞𝔯𝔱𝔟𝔢𝔞𝔱 + 𝐇𝔬𝔫𝔢𝔶𝔪𝔬𝔬𝔫 \n\n♫︎💕 𝐂𝔬𝔲𝔭𝔩𝔢𝔰 + 𝐓𝔞𝔪𝔦𝔩𝔱𝔞𝔤 \n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐔𝔭𝔱𝔦𝔪𝔢 🦋  {2}\n\n💕 𝐒𝔢𝔯𝔳𝔢𝔯𝐒𝔱𝔬𝔯𝔞𝔤𝔴 🦋 {3}\n\n💕 𝐂𝔭𝔲𝐋𝔬𝔞𝔡 🦋 {4}\n\n💕 𝐑𝔞𝔪𝐂𝔬𝔫𝔰𝔲𝔭𝔱𝔦𝔬𝔫 🦋 {5}\n\n💕 𝐔𝔰𝔢𝔯𝔰 🦋 {6}\n\n💕 𝐂𝔥𝔞𝔱𝔰 🦋 {7}\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐍𝔢𝔱𝔴𝔬𝔯𝔨 🦋 [𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/HeartBeat_Muzic)"
      ]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/f21bcb4b8b9c421409b64.png"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "https://graph.org/file/ffdb1be822436121cf5fd.png"
)
PLAYLIST_IMG_URL = "https://graph.org/file/f21bcb4b8b9c421409b64.png"
STATS_IMG_URL = "https://graph.org/file/ffdb1be822436121cf5fd.png"
TELEGRAM_AUDIO_URL = "https://graph.org/file/ffdb1be822436121cf5fd.png"
TELEGRAM_VIDEO_URL = "https://graph.org/file/f21bcb4b8b9c421409b64.png"
STREAM_IMG_URL = "https://graph.org/file/f21bcb4b8b9c421409b64.png"
SOUNCLOUD_IMG_URL = "https://graph.org/file/ffdb1be822436121cf5fd.png"
YOUTUBE_IMG_URL = "https://graph.org/file/f21bcb4b8b9c421409b64.png"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/f21bcb4b8b9c421409b64.png"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
