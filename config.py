import os

class Config:
    API_ID = int(os.getenv("API_ID", "123456"))  # Get from my.telegram.org
    API_HASH = os.getenv("API_HASH", "your_api_hash")  # Get from my.telegram.org
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Get from @BotFather
    MONGO_URL = os.getenv("MONGO_URL", "your_mongodb_uri")  # MongoDB connection
    ADMIN_ID = [123456789]  # Your Telegram user ID (Admin)
