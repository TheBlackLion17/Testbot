import re
from os import environ
import asyncio
from logging import WARNING, getLogger
from pyrogram import Client
from time import time
import logging 

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


LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
