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

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title='Help Options for ' + str(ctx.guild.name),
        colour=discord.Colour.dark_gold(),
        timestamp=datetime.utcnow(),
    )
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text='This bot was created by jacohobb#2174')
    embed.add_field(name='[.help_admin]', value='For server control', inline=False)
    embed.add_field(name='[.help_info]', value='Commands to get info on the sever and its users.', inline=False)
    embed.add_field(name='[.help_poll]', value='General help', inline=False)

    await ctx.send(embed=embed)

@client.command(pass_context=True, aliases=['admin_help', 'ah'])
async def help_admin(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title='Admin Controls for ' + str(ctx.guild.name),
        colour=discord.Colour.dark_gold(),
        timestamp=datetime.utcnow()
    )
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_author(name='Admin Help/Server Controls')
    embed.add_field(name='[.ban], [.b]', value='.ban @user to ban a user [Reason: Optional]', inline=False)
    embed.add_field(name='[.unban], [.ub]', value='.unban user#code to unban a user.',
                    inline=False)
    embed.add_field(name='[.banned_list], [.bl]', value='.banned_list to print out all banned users.', inline=False)
    embed.add_field(name='[.kick], [.k]', value='.kick @user to kick a user.', inline=False)
    embed.add_field(name='[.mute], [.m]', value='.mute @user to mute a user.', inline=False)
    embed.add_field(name='[.unmute], [.um]', value='.unmute @user to un-mute a user.', inline=False)
    embed.add_field(name='[.ping], [.p]', value='Returns bot latency', inline=False)

    await author.send(embed=embed)

@client.command(pass_context=True, aliases=['server_info_help', 'sh'])
async def help_server_info(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.dark_gold(),
        title='Server Info for ' + str(ctx.guild.name),
        timestamp=datetime.utcnow()
    )
    embed.set_thumbnail(url=ctx.guild.icon_url)

    embed.add_field(name='[.userinfo], [ui]', value='.userinfo @user or leave user blank for data about yourself.',
                    inline=False)
    embed.add_field(name='[.serverinfo], [si]', value='.serverinfo for data about the server.', inline=False)
    embed.add_field(name='[.userroles], [ur]', value='.userroles for a list of a users rolls.', inline=False)

    await ctx.send(embed=embed)

@client.command(pass_context=True, aliases=['poll_help'])
async def help_poll(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.dark_gold(),
        title='Server Info for ' + str(ctx.guild.name),
        timestamp=datetime.utcnow()
    )
    embed.set_thumbnail(url=ctx.guild.icon_url)

    embed.add_field(name='[.poll]', value='.poll "question" up-to-10-answers',
                    inline=False)
    await ctx.send(embed=embed)

# Adds the ability to access the cogs folder and run files
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)