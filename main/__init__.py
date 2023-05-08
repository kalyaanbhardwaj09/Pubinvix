#Github.com/mrinvisible7

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("11335251", default=None, cast=int)
API_HASH = config("39b4e23f71dcdd6138067fa7ff4656c9", default=None)
BOT_TOKEN = config("6070837253:AAGYpHylT7uJ5hSm2jdMYfP7XccThuM4lIs", default=None)
SESSION = config("AQAasn227sseM5F3qSyLPD86M-obq_xPsF4UIEGADeVNyVFhVtY4qZUQha7ACw311vZULPj_tVikuiyak_ArUjM4OyVFWLeXjJHGZDdV9d_UDrRlZGvXkOCoyzDEwvCB4fq9rG8aMSYGruAn4vnMqWjKJePtePkJEYYkrxul1IRdWt7KVH-jK7mD37Q0bK6xA6AuNaeFuhkjYEX4jpr6emqpIbw_RaYG5QGn795zvcfmIsafPbVzwcW_dX_Ee-fpwNDeXNq9-DVTmEjDQPXksuwxVHagu18mWZD_Bs_28KQGrqKt24jtjNd45LsKqdL-yWvmmfm-sUWXpUgqtTs0N_FDAAAAATpUc_AA", default=None)
FORCESUB = config("forceeaubb", default=None)
AUTH = config("5273580528", default=None)
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

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
    #print(e)
    logger.info(e)
    sys.exit(1)
