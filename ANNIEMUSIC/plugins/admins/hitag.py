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

TAGMES = [ " *நீங்கள் எங்கே இருக்கிறீர்கள்?🤗🥱* ",
           " *நீங்கள் தூங்குகிறீர்களா? ஆன்லைனில் வருகிறீர்களா?😊* ",
           " *சரி ஏதாவது பேசலாம்😃* ",
           " *நீங்கள் சாப்பிட்டீர்களா?.??🥲* ",
           " *வீட்டில் எல்லோரும் எப்படி இருக்கிறார்கள்?🥺* ",
           " *நான் உன்னை மிகவும் இழக்கிறேன் என்று எனக்குத் தெரியும்🤭* ",
           " *ஏய், இது எப்படி தீர்வு???🤨* ",
           " *நல்லா தூங்குனாயா..??🙂* ",
           " *உங்கள் பெயர் என்ன..??🥲* ",
           " *நீ உனது காலை உணவை எடுத்து கொண்டாயா???😋* ",
           " *உங்கள் குழுவில் என்னை கடத்துங்கள்😍* ",
           " *உங்கள் friend உங்களைத் தேடுகிறார், விரைவில் ஆன்லைனில் வாருங்கள்😅😅* ",
           " *நீ என்னுடன் நட்பு கொள்வாயா..??🤔* ",
           " *நீ தூங்க சென்றாயா?🙄🙄* ",
           ]

VC_TAG = [ 
        "*𝘖𝘪𝘪 𝘝𝘤 𝘫𝘰𝘪𝘯 𝘱𝘢𝘯𝘯𝘶 𝘭𝘶𝘴𝘶",
         "𝐂𝙾𝙼𝙴 𝚅𝙲 𝙱𝙰𝙱𝚈 𝙵𝙰𝚂𝚃🏓",
         "𝐁𝙰𝙱𝚈 நீயும் கொஞ்சம் இங்கே வா.🥰",
         "𝘝𝘤 𝘷𝘢 𝘱𝘦𝘴𝘢𝘭𝘢. 𝘪𝘭𝘭𝘢 𝘴𝘰𝘯𝘨 𝘬𝘦𝘬𝘢𝘭𝘢𝘮🤨",
         "𝘐𝘯𝘯𝘢𝘪𝘬𝘶 𝘝𝘊 𝘳𝘰𝘮𝘣𝘢 𝘧𝘶𝘯-𝘢 𝘱𝘰𝘵𝘩𝘶.🤣",
         "𝘕𝘦 𝘦𝘯𝘢 𝘱𝘢𝘯𝘥𝘳𝘢𝘯𝘶 𝘴𝘰𝘭𝘭𝘢 𝘷𝘤 𝘷𝘢😁",
         "𝘜𝘯𝘯𝘢 𝘱𝘢𝘵𝘵𝘩𝘪 𝘱𝘦𝘴𝘢𝘭𝘢𝘮 𝘷𝘤 𝘷𝘢⚽",
         "𝘕𝘢 𝘺𝘢𝘳𝘶𝘯𝘶 𝘴𝘰𝘭𝘳𝘦𝘯 𝘷𝘤 𝘷𝘢🥺",
         "𝘙𝘰𝘮𝘣𝘢 𝘣𝘰𝘳𝘦-𝘢 𝘪𝘳𝘶𝘬𝘬𝘢. 𝘷𝘢 𝘧𝘶𝘯 𝘱𝘢𝘯𝘢𝘭𝘢𝘮😥",
         "𝘦𝘱𝘱𝘢𝘷𝘶𝘮 𝘣𝘰𝘳𝘪𝘯𝘨. 𝘷𝘤 𝘷𝘢 𝘦𝘯𝘵𝘦𝘳𝘵𝘢𝘪𝘯 𝘱𝘢𝘯𝘢𝘭𝘢𝘮🙄",
         "𝘦𝘯𝘯𝘢𝘥𝘢 𝘪𝘵𝘩𝘶. 𝘪𝘯𝘢𝘪𝘬𝘶 𝘪𝘷𝘭𝘰 𝘮𝘰𝘬𝘬𝘢𝘺𝘢 𝘱𝘰𝘵𝘩𝘶. 𝘷𝘤-𝘢𝘵𝘩𝘶 𝘷𝘢𝘺𝘦𝘯?🤔",
         "𝘴𝘢𝘱𝘵𝘢𝘺𝘢. 𝘴𝘢𝘳𝘪 𝘷𝘢 𝘷𝘤 𝘱𝘰𝘭𝘢𝘮🙂"
        ]


@app.on_message(filters.command(["tamiltag" ], prefixes=["/"]))
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
        return await message.reply("/tamiltag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tamiltag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tamiltag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
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


@app.on_message(filters.command(["vctag"], prefixes=["/"]))
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
        return await message.reply("๏ 🦋Stopped Mention.....🫠๏")
