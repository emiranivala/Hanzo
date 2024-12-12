import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20259558"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ce95ed6fecb559fecbb6fb7ebed176e4")

#Database 
DB_URI = os.environ.get("DB_URI", "")
