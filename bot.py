from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient
from config import Config

# Initialize bot and database
bot = Client("AutoFilterBot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
mongo = MongoClient(Config.MONGO_URL)
db = mongo["AutoFilterDB"]
collection = db["files"]

# Save files in the database
@bot.on_message(filters.document | filters.video | filters.audio & filters.chat(Config.ADMIN_ID))
async def save_file(client, message):
    file_name = message.document.file_name if message.document else message.video.file_name
    file_id = message.document.file_id if message.document else message.video.file_id

    # Save file details to MongoDB
    collection.insert_one({"file_name": file_name, "file_id": file_id})
    await message.reply_text(f"✅ File **{file_name}** added to database!")

# Search for files
@bot.on_message(filters.text & filters.group)
async def search_files(client, message):
    query = message.text.lower()
    results = collection.find({"file_name": {"$regex": query, "$options": "i"}})

    buttons = []
    for result in results:
        buttons.append([InlineKeyboardButton(result["file_name"], callback_data=result["file_id"])])
    
    if buttons:
        await message.reply_text("📂 Here are the matching files:", reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await message.reply_text("❌ No matching files found.")

# Send file when button is clicked
@bot.on_callback_query()
async def send_file(client, callback_query):
    file_id = callback_query.data
    await callback_query.message.reply_document(file_id)

# Run bot
print("🤖 Bot is running...")
bot.run()
