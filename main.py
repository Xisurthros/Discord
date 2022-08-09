import discord
from discord.ext import commands
from secrets import TOKEN, OWNER_ID

print('Bot is running')
print(discord.__version__)

BOT_CHANNEL_ID = 'BOT_CHANNEL_ID' # Set custom channel id to restrict bot to specific channel
OWNER_ID = 'OWNER_ID'   # Set to restrict special commands to bot owner only

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

client.remove_command('help')

@client.event
async def on_ready():
    activity = discord.Game(name="Your Status Here")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_member_join(member):
    channel_id = client.get_channel(BOT_CHANNEL_ID)
    await channel_id.send(f'{member.mention} has joined the server, Welcome')
    print(f'{member} has joined a server')

# This allows a specific user to load and unload different .py files
def is_it_me(ctx):
    return ctx.author.id == OWNER_ID

@client.event
async def on_member_remove(member):
    member_id = member.id
    channel_id = client.get_channel(BOT_CHANNEL_ID)
    await channel_id.send(f'{member.mention} has left the server')
    print(f'{member} has left a server')

@client.command()
@commands.check(is_it_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Please re-enter the command and add a cog to load')
    if isinstance(error, PermissionError):
        await ctx.send(f'You do not have permission to do that.')

@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please re-enter the command and add a cog to unload')

# Adds the ability to access the cogs folder and run files
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)