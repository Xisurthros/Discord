import discord
from discord.ext import commands

class Admin(commands.Cog):
    Admin = 'Admin Controls'

    def __init__(self, bot):
        self.bot = bot
        self.OWNER_ID = 'OWNER_ID'
        self.mute = 'MUTED_ROLE_ID'

    @commands.Cog.listener()
    async def on_ready(self):

        print('Admin is running')

    @commands.command(aliases=['p'])
    async def ping(self, ctx, user_id=self.OWNER_ID):

        try:
            await ctx.send(f"**Pong!** {round(self.bot.latency * 1000)}ms")

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'Ping error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.command(aliases=['k'], description='.kick [@user] to kick a user.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None, user_id=self.OWNER_ID):

        try:
            await member.kick(reason=reason)
            await ctx.send(f'User {member.mention} has been kicked.')

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'Kick error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.command(aliases=['b'], description='.ban [@user] to ban a user.')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None, user_id=self.OWNER_ID):

        try:
            await member.ban(reason=reason)
            await ctx.send(f'User {member.mention} has been banned.')

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'Ban error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.command(aliases=['ub'], description='.unban [@user] to unban a user.')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member, user_id=self.OWNER_ID):

        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'User {user.mention} has been unbanned')
                    return

            await ctx.send(f'User {user.mention} was not found')

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'Unban error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.command(aliases=['bl'], description='.banned_list to print out all banned users.')
    @commands.has_permissions(ban_members=True)
    async def banned_list(self, ctx, user_id=self.OWNER_ID):

        try:
            banned_users = await ctx.guild.bans()

            embed = Embed(title=f'Banned list for {ctx.guild.name}',
                          description='**Users**',
                          colour=discord.Colour.dark_gold(),
                          timestamp=datetime.utcnow())

            embed.set_thumbnail(url=ctx.guild.icon_url)

            for ban_entry in banned_users:
                embed.add_field(name=f'{ban_entry.user.name}#{ban_entry.user.discriminator}',
                                value=f'ID: {ban_entry.user.id} Reason: {ban_entry.reason}', inline=False)

            await ctx.send(embed=embed)

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'Banned_list error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.command(aliases=['m'], description='.mute [@user] to mute a user.')
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, user_id=self.OWNER_ID):

        try:
            muted_role = ctx.guild.get_role(self.muted_role)
            await member.add_roles(muted_role)
            await ctx.send(f'{member.mention} has been muted')

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'Mute error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.command(aliases=['um'], description='.mute [@user] to un-mute a user.')
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member, user_id=self.OWNER_ID):

        try:
            muted_role = ctx.guild.get_role(self.muted_role)
            await member.remove_roles(muted_role)
            await ctx.send(f'{member.mention} has been un-muted')

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'Unmute error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')


def setup(client):
    client.add_cog(Admin(client))