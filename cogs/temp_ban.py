import datetime
import os
from disnake.ext import commands
import disnake

from enums import Color


class TempBan(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.slash_command(description="Give a user ban for time")
    async def temp_ban(
        self,
        ctx,
        member: disnake.Member,
        reason: str,
        minutes: int,
    ):
        time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
        await ctx.guild.ban(member, reason=reason)
        ban_embed = disnake.Embed(
            title="Temp ban",
            description=f"Temp ban {member.name} because of {reason}.Unban via {minutes} minutes",
            color=Color.RED.value,
        )
        file_path = os.path.join(os.getcwd(), "images", "ban.jpg")
        file = disnake.File(file_path, filename="ban.jpg")
        ban_embed.set_image(file=file)
        await ctx.send(embed=ban_embed)
        await disnake.utils.sleep_until(time)
        await ctx.guild.unban(member)
        unban_embed = disnake.Embed(title="Unban member", color=Color.GREEN.value)
        await ctx.send(embed=unban_embed)


def setup(bot: commands.Bot):
    bot.add_cog(TempBan(bot))
