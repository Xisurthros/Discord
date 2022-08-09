import discord
from discord.ext import commands
from discord import Embed, Member
from typing import Optional
from datetime import datetime

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Info is now running')

def setup(bot):
    bot.add_cog(Info(bot))