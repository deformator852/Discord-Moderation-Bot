from disnake.ext import commands
import disnake

from enums import Color


class UnlockChannel(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.slash_command(description="Command that unlock channel")
    async def unlock(self, inter: disnake.ApplicationCommandInteraction):
        channel = inter.channel
        overwrite = disnake.PermissionOverwrite(send_messages=True)
        await channel.set_permissions(inter.guild.default_role, overwrite=overwrite)
        embed = disnake.Embed(title="Unlock chat", color=Color.GREEN.value)
        await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(UnlockChannel(bot))
