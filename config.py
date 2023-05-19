from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MUST_JOIN = getenv("MUST_JOIN", None)
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = getenv("MONGO_DB_URI")
