import discord
from discord.ext import commands
from secrets import TOKEN

print('Bot is running')
print(discord.__version__)

# This creates and determines the command prefix
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

# This removes the help command for a custom help command later
client.remove_command('help')

@client.command(aliases=['p'])
    async def ping(self, ctx):
        try:
            await ctx.send(f"**Pong!** {round(self.bot.latency * 1000)}ms")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)