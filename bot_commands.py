# bot_commands.py
import discord
from discord.ext import commands
from datetime import datetime
from .growtopia_data import get_growtopia_data # Import fungsi dari file growtopia_data.py

def setup_commands(bot):
    """
    Menyiapkan perintah bot Discord.
    """

    @bot.event
    async def on_ready():
        print(f"Bot sudah online sebagai {bot.user} (ID: {bot.user.id})")

    @bot.command(name="status")
    async def status(ctx):
        """
        Ketika user mengetikkan !status, fungsi ini akan terpanggil.
        Menampilkan status server Growtopia.
        """
        data = get_growtopia_data() # Panggil fungsi untuk mengambil data Growtopia

        embed = discord.Embed(
            title="🌐 Growtopia Server Status",
            color=0x00FF00,
            timestamp=datetime.utcnow()
        )

        wotd_link = data["WOTDLink"]
        if wotd_link.startswith("http://") or wotd_link.startswith("https://"):
            embed.set_thumbnail(url=wotd_link)

        embed.add_field(name="👥 Online User", value=str(data["Online_User"]), inline=False)
        embed.add_field(name="🏷️ World of the Day", value=data["WOTDName"], inline=False)

        embed.add_field(name="⏰ GT TIME", value=data["GTTime"], inline=True)
        embed.add_field(name="📅 GT DATE", value=data["GTDate"], inline=True)
        embed.set_footer(text="FanKing Bot")

        await ctx.send(embed=embed)
