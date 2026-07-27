import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"{bot.user} 已上線")


@bot.tree.command(
    name="ping",
    description="測試 Bot 是否在線"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "💜 F.H. Bot 在線！"
    )


bot.run(TOKEN)
