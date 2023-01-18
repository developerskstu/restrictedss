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
SESSION = "AQAYj-pEjOemZEMH5-_Nc6unXqWCM8gdMESE-WwN9NsLoGr38F3qpkM7ag-WOJXCbDiB1nioIkK8lCUsYEvNautBKsdYBGvchZ8S7sFKp9Bph8Zm2vdFHK41-L55zG9gD4i1jan4lWzdKx_O6JCkpCGDrdmFO1u9jUs3G9TM7WtCrC76PMFIlbTRpWc69wZPU31vFVF2q73VKZ8sJF1lUxBUlNyMCn1RMSQ7QxCTWShC5LLaHYj5Ogta--cEefRJ_nqkMvLbczGpMG1FVPrYoPtIRwGAI6KLjUVZwg1B0gPh-djeDSPUnIIYQSkZtUn_TEHqfPEG44drjacBhfU_KZT1AAAAAUk7U9cA"
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
