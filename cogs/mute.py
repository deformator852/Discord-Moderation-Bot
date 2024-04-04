import datetime
import os
from disnake.ext import commands
import disnake


class Mute(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.has_permissions(mute_members=True)
    @commands.slash_command(description="The command mute the user")
    async def mute(
        self,
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member,
        minutes: str,
        reason: str,
    ):
        if member.top_role > inter.author.top_role:
            file_path = os.path.join(os.getcwd(), "images", "mute.jpg")
            file = disnake.File(file_path, filename="mute.jpg")
            minutes = int(minutes)
            time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
            await member.timeout(reason=reason, until=time)
            embed = disnake.Embed(
                title=f"Mute {member.name} because of {reason}.Unmute via {minutes} minutes",
                color=0xFF0000,
            )
            embed.set_image(file=file)
            await inter.response.send_message(embed=embed)

    @commands.has_permissions(mute_members=True)
    @commands.slash_command(description="The command mute the user")
    async def unmute(
        self,
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member,
    ):
        if member.top_role > inter.author.top_role:
            await member.timeout(until=None)
            embed = disnake.Embed(title=f"Unmute {member.name}", color=0x00FF00)
            await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Mute(bot))
