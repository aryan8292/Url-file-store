import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "23273287"))
  API_HASH = os.environ.get("API_HASH", "2c8dbe9c5823a819a25201d7c2ccc3c6")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Vku79bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001856581505"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "ziplinker.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "a73ab244be8aa742065881d647c98055e0d017b6")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5079629749"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Aryan6969:Aryan6969@cluster0.krhmwhe.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001764859194")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001856581505"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
  ABOUT_BOT_TEXT = f"✅"
  ABOUT_DEV_TEXT = f""" 😘 """
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
