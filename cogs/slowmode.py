from disnake.ext import commands
import disnake

from enums import Color


class SlowMode(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.slash_command(description="Turn on slow mode in channel")
    async def slow_mode_on(
        self, inter: disnake.ApplicationCommandInteraction, delay: int
    ):
        channel = inter.channel
        await channel.edit(slowmode_delay=delay)
        embed = disnake.Embed(
            title="Turn on slow mode",
            description=f"You can write a message every {delay} seconds",
            color=Color.GREEN.value,
        )
        await inter.response.send_message(embed=embed)

    @commands.has_permissions(administrator=True)
    @commands.slash_command(description="Turn off slow mode in channel")
    async def slow_mode_off(self, inter: disnake.ApplicationCommandInteraction):
        channel = inter.channel
        await channel.edit(slowmode_delay=0)
        embed = disnake.Embed(
            title="Turn off slow mode",
            color=Color.RED.value,
        )
        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(SlowMode(bot))
