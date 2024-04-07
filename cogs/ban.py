import os
from disnake.ext import commands
from enums import Color
import disnake


class Ban(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.slash_command(description="The command ban the user")
    async def ban(self, ctx, reason: str, user: disnake.Member):
        file_path = os.path.join(os.getcwd(), "images", "ban.jpg")
        file = disnake.File(file_path, filename="ban.jpg")
        embed = disnake.Embed(title=f"Ban {user.name}", color=Color.RED.value)
        embed.set_image(file=file)
        await ctx.guild.ban(user)
        await ctx.send(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))
