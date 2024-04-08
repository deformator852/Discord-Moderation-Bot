from disnake.ext import commands
import disnake

from enums import Color


class Kick(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.slash_command(description="kick the user")
    async def kick(
        self,
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member,
    ):
        embed = disnake.Embed(title="Kick member", color=Color.RED.value)
        await inter.response.send_message(embed=embed)
        await member.kick()


def setup(bot: commands.Bot):
    bot.add_cog(Kick(bot))
