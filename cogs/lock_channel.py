import asyncio
import datetime
from disnake.ext import commands
import disnake

from enums import Color


class Lock(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.slash_command(
        description="Close the channel for a certain period of time"
    )
    async def lock(inter: disnake.ApplicationCommandInteraction, minutes: str):
        minutes = int(minutes)
        time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
        cool_time = disnake.utils.format_dt(time, "t")
        embed = disnake.Embed(
            title="Lock channel",
            description=f"Channel will unlock in: {cool_time}",
            color=Color.RED.value,
        )
        await inter.response.send_message(
            embed=embed,
        )
        channel = inter.channel
        overwrite = disnake.PermissionOverwrite(send_messages=False)
        await channel.set_permissions(inter.guild.default_role, overwrite=overwrite)
        await asyncio.sleep(minutes * 60)
        overwrite = disnake.PermissionOverwrite(send_messages=True)
        await channel.set_permissions(inter.guild.default_role, overwrite=overwrite)


def setup(bot: commands.Bot):
    bot.add_cog(Lock(bot))
