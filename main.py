import disnake
from disnake.ext import commands
import os


TOKEN = "MTIyNDk5MDEyMTE3OTQ4NDIyMg.GeRZDl.qzcrhUeCNOWc7chcJj9xyskPl8gn6BTujlMEJI"
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("bot ready")
    bot.remove_slash_command("me")
    bot.remove_slash_command("gif")
    bot.remove_slash_command("msg")
    bot.remove_slash_command("nick")
    bot.remove_slash_command("shrug")
    bot.remove_slash_command("spoiler")
    bot.remove_slash_command("tableflip")
    bot.remove_slash_command("thread")
    bot.remove_slash_command("tts")
    bot.remove_slash_command("unflip")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(TOKEN)
