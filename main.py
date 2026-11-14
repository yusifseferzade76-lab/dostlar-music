import os

print("DOSTLAR MUSIC BOT")
print("SYSTEM: ONLINE")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not all([API_ID, API_HASH, BOT_TOKEN]):
    raise ValueError("GitHub Secrets məlumatları çatışmır")

print("API SETTINGS: OK")
print("DOSTLAR MUSIC READY")