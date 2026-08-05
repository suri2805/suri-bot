import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Đăng nhập thành công: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "Suri" in message.content.lower():
        await message.channel.send(f"Đứa nào gọi tao {message.author.mention}! 👋")

    if "ngu" == message.content.lower():
        await message.channel.send("mày ngu đấy")

    await bot.process_commands(message)

bot.run(TOKEN)
