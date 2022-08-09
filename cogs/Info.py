import discord
from discord.ext import commands
from discord import Embed, Member
from typing import Optional
from datetime import datetime

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.OWNER_ID = 'OWNER_ID'

    @commands.Cog.listener()
    async def on_ready(self):
        print('Info is now running')

    @commands.command(name='userinfo', aliases=['ui'])
    async def user_info(self, ctx, target: Optional[Member], user_id=self.OWNER_ID):

        try:

            target = target or ctx.author

            embed = Embed(title='User Information',
                          colour=discord.Colour.dark_gold(),
                          timestamp=datetime.utcnow())

            embed.set_thumbnail(url=target.avatar_url)

            fields = [('Name', str(target), True),
                      ('ID', target.id, True),
                      ('Bot?', target.bot, True),
                      ('Top Role', target.top_role.mention, True),
                      ('Status', str(target.status).title(), True),
                      ("Activity",
                       f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}",
                       True),
                      ('Created On', target.created_at.strftime('%m/%d/%Y %H:%M:%S'), True),
                      ('Joined On', target.joined_at.strftime('%m/%d/%Y %H:%M:%S'), True),
                      ('Boosted', bool(target.premium_since), True)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await ctx.send(embed=embed)

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'User_info error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.command(name='serverinfo', aliases=['si'])
    async def server_info(self, ctx, user_id=self.OWNER_ID):

        try:

            embed = Embed(title='Server Information',
                          colour=discord.Colour.dark_gold(),
                          timestamp=datetime.utcnow())

            embed.set_thumbnail(url=ctx.guild.icon_url)

            statuses = [len(list(filter(lambda m: str(m.status) == 'online', ctx.guild.members))),
                        len(list(filter(lambda m: str(m.status) == 'idle', ctx.guild.members))),
                        len(list(filter(lambda m: str(m.status) == 'dnd', ctx.guild.members))),
                        len(list(filter(lambda m: str(m.status) == 'offline', ctx.guild.members)))]

            fields = [('ID', ctx.guild.id, True),
                      ('Owner', ctx.guild.owner, True),
                      ('Region', ctx.guild.region, True),
                      ('Created at', ctx.guild.created_at.strftime('%m/%d/%Y %H:%M:%S'), True),
                      ('Members', len(ctx.guild.members), True),
                      ('Humans', len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                      ('Bots', len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                      ('Banned Members', len(await ctx.guild.bans()), True),
                      ('Statuses', f'🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}', True),
                      ('Text Channels', len(ctx.guild.text_channels), True),
                      ('Voice Channels', len(ctx.guild.voice_channels), True),
                      ('Categories', len(ctx.guild.categories), True),
                      ('Roles', len(ctx.guild.roles), True),
                      ('Invites', len(await ctx.guild.invites()), True),
                      ('\u200b', '\u200b', True)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await ctx.send(embed=embed)

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'Server_info error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.command(aliases=['ur', 'userroles', 'userrole', 'user_role'])
    async def user_roles(self, ctx, target: Optional[Member], user_id=self.OWNER_ID):

        try:

            target = target or ctx.author
            rolelist = [r.mention for r in target.roles if r != ctx.guild.default_role]
            roles = ", ".join(rolelist)

            embed = Embed(title=f'Roles for {target}',
                          colour=discord.Colour.dark_gold(),
                          timestamp=datetime.utcnow())

            embed.set_thumbnail(url=target.avatar_url)

            fields = [('All user rolls', roles, True)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=str(roles), inline=inline)

            await ctx.send(embed=embed)

        except:
            target = await self.bot.fetch_user(user_id)
            await target.send(f'User_roles error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

def setup(bot):
    bot.add_cog(Info(bot))