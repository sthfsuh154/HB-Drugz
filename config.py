import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials - Get these from the Telegram API website
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Specify where to get the following credentials
OWNER_USERNAME = getenv("OWNER_USERNAME","rajeshrakis")
BOT_USERNAME = getenv("BOT_USERNAME", "thedakkidaikathaval_bot")
BOT_NAME = getenv("BOT_NAME", "𝞖𝘌𝘈𝘙𝘛𝞑𝘌𝘈𝘛𝂬♡𝂬𝘿𝘙𝘜𝘎𝘡")
ASSUSERNAME = getenv("ASSUSERNAME", "ice_babygirl")
EVALOP = list(map(int, getenv("EVALOP", "5059737154").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", -1001735663878))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# External APIs - Get these from their respective providers
GPT_API = getenv("GPT_API")
PLAYHT_API = getenv("PLAYHT_API")
OWNER_ID = int(getenv("OWNER_ID", 1281282633))

# Heroku deployment settings - Refer to Heroku documentation on how to obtain these
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/rajeshrakis/HB-Drugz")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
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
    "𝐇ɛʟʟօ {0} ~\n\n💕 𝐓нιѕ 𝐈ѕ {1} \n α 𝐒мαят 𝐏яσ ⚡️ 𝐌υѕιᴄ 𝐁σт 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐏яσ 𝐅єαтυяєѕ 🦋\n\n♫︎🌹 𝐅υη 𝐓αgѕ 🥂 \n\n♫︎🌹 𝐖єʟᴄσмє 𝐆яєєтιηg 💐 \n\n♫︎🌹 𝐋єƒт 𝐍σтє 🍾 \n\n♫︎🌹 𝐕ᴄ 𝐈ηνιтє 𝐂αя∂ 🎉 \n\n♫︎🌹 𝐕ι∂єσ 𝐃σωηʟσα∂ 📹 \n\n♫︎🌹 𝐀υ∂ισ 𝐃σωηʟσα∂ 🎶 \n\n♫︎🌹 𝐒υρρσят 𝐋ινє 𝐒тяєαм αη∂ 𝐘συтυвє 𝐒тяєαмѕ 🥳 \n\n♫︎🌹 𝐌σνιє & 𝐕ι∂єσ 𝐒тяєαмιηg 24x7 💝 \n\n 💕 𝐌αкє 𝐌є 𝐀∂мιη αη∂ 𝐄ηנσу 𝐌σяє 𝐅єαтυяєѕ 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐍єтωσяк 🦋 [𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/HeartBeat_Muzic)",
    "𝐇ɛʟʟօ {0} ~\n\n💕 𝐓нιѕ 𝐈ѕ {1} \n α 𝐒мαят 𝐏яσ ⚡️ 𝐌υѕιᴄ 𝐁σт 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐏яσ 𝐅єαтυяєѕ 🦋\n\n♫︎🌹 𝐅υη 𝐓αgѕ 🥂 \n\n♫︎🌹 𝐖єʟᴄσмє 𝐆яєєтιηg 💐 \n\n♫︎🌹 𝐋єƒт 𝐍σтє 🍾 \n\n♫︎🌹 𝐕ᴄ 𝐈ηνιтє 𝐂αя∂ 🎉 \n\n♫︎🌹 𝐕ι∂єσ 𝐃σωηʟσα∂ 📹 \n\n♫︎🌹 𝐀υ∂ισ 𝐃σωηʟσα∂ 🎶 \n\n♫︎🌹 𝐒υρρσят 𝐋ινє 𝐒тяєαм αη∂ 𝐘συтυвє 𝐒тяєαмѕ 🥳 \n\n♫︎🌹 𝐌σνιє & 𝐕ι∂єσ 𝐒тяєαмιηg 24x7 💝 \n\n 💕 𝐌αкє 𝐌є 𝐀∂мιη αη∂ 𝐄ηנσу 𝐌σяє 𝐅єαтυяєѕ 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n♫︎💕 𝐏ʟαу + 𝐕ρʟαу + 𝐒тяєαм \n\n♫︎💕 𝐓αgαʟʟ + 𝐌єηтιση + 𝐆мтαg \n\n♫︎💕 𝐆ηтαg + 𝐕ᴄтαg + 𝐋σνєтαg \n\n♫︎💕 𝐒ιηgʟє + 𝐇єαятвєαт + 𝐇σηєумσση \n\n♫︎💕 𝐂συρʟєѕ + 𝐓αмιʟтαg \n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐍єтωσяк 🦋 [𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/HeartBeat_Muzic)",
    "𝐇ɛʟʟօ {0} ~\n\n💕 𝐓нιѕ 𝐈ѕ {1} \n α 𝐒мαят 𝐏яσ ⚡️ 𝐌υѕιᴄ 𝐁σт 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐏яσ 𝐅єαтυяєѕ 🦋\n\n♫︎🌹 𝐅υη 𝐓αgѕ 🥂 \n\n♫︎🌹 𝐖єʟᴄσмє 𝐆яєєтιηg 💐 \n\n♫︎🌹 𝐋єƒт 𝐍σтє 🍾 \n\n♫︎🌹 𝐕ᴄ 𝐈ηνιтє 𝐂αя∂ 🎉 \n\n♫︎🌹 𝐕ι∂єσ 𝐃σωηʟσα∂ 📹 \n\n♫︎🌹 𝐀υ∂ισ 𝐃σωηʟσα∂ 🎶 \n\n♫︎🌹 𝐒υρρσят 𝐋ινє 𝐒тяєαм αη∂ 𝐘συтυвє 𝐒тяєαмѕ 🥳 \n\n♫︎🌹 𝐌σνιє & 𝐕ι∂єσ 𝐒тяєαмιηg 24x7 💝 \n\n 💕 𝐌αкє 𝐌є 𝐀∂мιη αη∂ 𝐄ηנσу 𝐌σяє 𝐅єαтυяєѕ 🦋\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n♫︎💕 𝐏ʟαу + 𝐕ρʟαу + 𝐒тяєαм \n\n♫︎💕 𝐓αgαʟʟ + 𝐌єηтιση + 𝐆мтαg \n\n♫︎💕 𝐆ηтαg + 𝐕ᴄтαg + 𝐋σνєтαg \n\n♫︎💕 𝐒ιηgʟє + 𝐇єαятвєαт + 𝐇σηєумσση \n\n♫︎💕 𝐂συρʟєѕ + 𝐓αмιʟтαg \n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐔ρтιмє 🦋  {2}\n\n💕 𝐒єяνєя𝐒тσяαgє 🦋 {3}\n\n💕 𝐂ρυ𝐋σα∂ 🦋 {4}\n\n💕 𝐑αм𝐂σηѕυρтιση 🦋 {5}\n\n💕 𝐔ѕєяѕ 🦋 {6}\n\n💕 𝐂нαтѕ 🦋 {7}\n\n❦︎ . * ● ° ꨄ︎ ¸ . ❦︎　° :. ꨄ︎ * • ○ ° ❦︎\n\n💕 𝐍єтωσяк 🦋 [𝅗ـﮩ٨ـ𝅽𝅾𓆩𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ𓆪ﮩ٨ـ𝅽𝅾‐𝅘](https://t.me/HeartBeat_Muzic)"
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
