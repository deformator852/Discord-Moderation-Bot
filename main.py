import disnake
from disnake.ext import commands
import os


TOKEN = "MTIyNDk5MDEyMTE3OTQ4NDIyMg.GeRZDl.qzcrhUeCNOWc7chcJj9xyskPl8gn6BTujlMEJI"
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("bot ready")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(TOKEN)
