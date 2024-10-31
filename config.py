import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25276967"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "daf793293a5a244e5c426a129656e0a1")

#Database 
DB_URI = os.environ.get("DB_URI", "")
