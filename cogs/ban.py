from disnake.ext import commands

import disnake


class Ban(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot

    @commands.has_permissions(administrator=True)
    @commands.slash_command(description="The command ban the user")
    async def ban(self, ctx, user: disnake.Member):
        embed = disnake.Embed(title=f"Ban {user.name}", color=0xFF0000)
        await ctx.guild.ban(user)
        await ctx.send(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))
