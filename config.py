import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23783378"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1151425ad8d6fa61d47247f9ee841a37")

#Database 
DB_URI = os.environ.get("DB_URI", "")
