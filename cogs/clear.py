from disnake.ext import commands
import disnake


class Clear(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.slash_command()
    async def clear(
        inter: disnake.ApplicationCommandInteraction, limit: int | None = None
    ):
        await inter.channel.purge(limit=limit)
        embed = disnake.Embed(title="Cleaned channel", color=0x00FF00)
        await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Clear(bot))
