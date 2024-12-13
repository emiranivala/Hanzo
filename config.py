import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "11693223"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "495b1c6af3a3a250b06d07049f32ec80")

#Database 
DB_URI = os.environ.get("DB_URI", "")
