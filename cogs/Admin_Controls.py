import discord
from discord.ext import commands

class Admin(commands.Cog):
    Admin = 'Admin Controls'

    def __init__(self, bot):
        self.bot = bot

def setup(client):
    client.add_cog(Admin(client))