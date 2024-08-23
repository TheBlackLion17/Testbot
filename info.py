import re
from os import environ
import asyncio
from logging import WARNING, getLogger
from pyrogram import Client
from time import time
import logging 

LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)
getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)

SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '29812636'))
API_HASH = environ.get('API_HASH', '581c6dd6f0af0f8c8326c9b28920ae54')
BOT_TOKEN = environ.get('BOT_TOKEN', "7174411060:AAGacM2p1oH8PbnwROxZRs3meuUbSLa1cv8")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002222025998'))



app = Client(
    "app2", 
    bot_token=BOT_TOKEN, 
    api_id=API_ID, 
    api_hash=API_HASH)
LOGGER.info("ᴡᴀɪᴛ ʙʀᴏ.. ʙᴏᴛ sᴛᴀʀᴛ ʜᴏ ʀʜᴀ ʜᴀɪ")
app.start()


