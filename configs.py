import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 19010782))
    API_HASH = os.environ.get("API_HASH", "830f2543690bcfb28d27a47d485c1ba4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5869785250:AAHFFu3cMrVcyiUfY_1_tjpHagARRG_uT34")
    PORT = os.environ.get("PORT", "8080")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQAugWXUCCHwNouC64r2bVlLlFEOvDyg2yJHyKZLHzunYWS5r85xmqUL-BPm3wtoxJqzgS8-LOfuQnsYHAEI6j0NQxpM2IGDC2IeasN1I-NiNt4mcr4sc6zLzUpKKQWtXF6B2_Kme_h0SDM0ClnBpwzywOEEU4Y36Dx7NIK2dGE14FTaC6ZHitmmAwEuZqTlIoM823D8YvWYyxCRdIh5DKb6QqTiF4Q59cznqSymYwGUvozca976PNZmXGTftisOqEcTeMzco_bPO0x1C7_yZTNwaVlG2i90nJAVwIBC2rdTGMYrc14vyoM6lgMAjhFIYAoAtTrd4k2K4iLvRC_GTG5heWtSfwA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001883053973))
    BOT_USERNAME = os.environ.get("BOT_USERNAME, "Team_HDTLinks_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "LOGESH"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Logesh:Logesh2004@cluster0.szthwiu.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Team HDT Link Search Bot.
    
    
    
🤖 My Name: <a href='https://t.me/Botfather'>Lin Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/Logeshps_bot2'>LOGESH</a></b>
"""

    ABOUT_HELP_TEXT = """<b>Secret</b>
<b>Hmm. This is just beginning</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @TEAM_HDT</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @TEAM_HDT</a></b>
"""

