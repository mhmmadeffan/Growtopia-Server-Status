# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot_commands import setup_commands # Import fungsi setup_commands dari file bot_commands.py

# =====================================================
# Muat variabel lingkungan dari .env
# =====================================================
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# =====================================================
# Setup bot Discord
# =====================================================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Setup commands dari bot_commands.py
setup_commands(bot)

if __name__ == "__main__":
    if TOKEN is None:
        print("⚠️ DISCORD_TOKEN belum diatur di file .env")
    else:
        bot.run(TOKEN)
