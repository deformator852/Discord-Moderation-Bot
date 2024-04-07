from disnake.ext import commands
import disnake

from enums import Color


class Warn(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.slash_command(description="Warn the user")
    async def warn(
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member,
        reason: str,
    ):
        embed = disnake.Embed(
            title="Warning",
            description=f"{member.mention} {reason}",
            color=Color.ORANGE.value,
        )
        await inter.response.send_message(
            embed=embed,
        )


def setup(bot: commands.Bot):
    bot.add_cog(Warn(bot))
