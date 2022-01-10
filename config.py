import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Eliza")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "SehathSanvidu")
ALIVE_NAME = getenv("ALIVE_NAME", "Eliza")
BOT_USERNAME = getenv("BOT_USERNAME", "MrsElizaRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ElizaAssistantHelper3")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ElizaSupporters")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Updates_of_ElizaBot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/3cbc7167d67e07a915a08.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Team-ELiza-SL/Eliza-Music-SL")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/599d286c45bee9611b625.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/185903d089b6d5edbaaf8.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/347a8d3cefdcec71ce072.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/991fe273af5c45719b41d.jpg")
