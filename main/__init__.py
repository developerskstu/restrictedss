#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24229815
API_HASH = "6d03e392b1200580a85ef243f83a48a5"
BOT_TOKEN = "5818737155:AAFgEZ3p6PGaHmKqW3QcLEotCb_EsDba9xg"
SESSION = "AQCxt5WEiHqq8DH-glWcAMOp2PdgKXi4L8hEsL7FjnoCN-t9P9-ITdpSnylg1uPL4HO3cAjuSa-lM6p4SqDcn7liLhfgHawNZQOvMn15aZDwApQ_h-GOhCgdSEW_ZNiHHObNhKtwHf-3wwpg0fMJsmOvo5S23CrPa-zWpE1sYGiblwpE8FOs-5qeSmy5Z8NBvlehbFL-YnD0f3XoI8O6ew4yP_5ifvKExBIDCIPC4WccU3hj--uhNx1u73Bm8CQvQJgdnu2obfj4U_TQRC23CVQMfXhTLs2dNROcadTUB7Yl5MqtL2DS_82c_AhQeSsaWuOn7jBUg1p-1d9kPYEekBgYAAAAAUk7U9cA"
FORCESUB = "tested_botss"
AUTH = 5523592151

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
