import discord
from discord.ext import commands
from discord import embeds
from discord.ext.commands import has_permissions
from datetime import datetime, timedelta

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
           "6⃣", "7⃣", "8⃣", "9⃣", "🔟")


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.reaction_message = ''
        self.polls = []
        self.OWNER_ID = 'OWNER_ID'

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll is running')

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def poll(self, ctx, hours: int, question, *options, user_id=self.OWNER_ID):
    	try: 
        	if len(options) > 10:
        	    await ctx.send('You are only allowed 10 options maximum')
        	else:
        	    embed = discord.Embed(title="Poll",
        	                          description=question,
        	                          colour=discord.Colour.dark_gold(),
        	                          timestamp=datetime.utcnow())
        	    fields = [("Options", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False),
        	              ("Instructions", "React to cast a vote!", False)]
        	    for name, value, inline in fields:
        	        embed.add_field(name=name, value=value, inline=inline)
        	    message = await ctx.send(embed=embed)
        	    for emoji in numbers[:len(options)]:
        	        await message.add_reaction(emoji)
	
        	    self.polls.append((message.channel.id, message.id))
	
        	    self.client.scheduler.add_job(self.complete_poll, "date", run_date=datetime.now() + timedelta(seconds=hours),
                                          args=[message.channel.id, message.id])
       	except:
       		target = await self.bot.fetch_user(user_id)
            await target.send(f'Poll error.\nGuild Name: {ctx.guild.name} Guild ID: {ctx.guild.id}')
            await ctx.send(f'Unexpected Error. Try again later\nThe owner has been notified')

    @commands.Cog.listener()
    async def on_raw_reaction(self, payload):
        if self.client.ready and payload.message_id == self.reaction_message:
            await self.reaction_message.remove_reaction(payload.emoji, payload.member)

        elif payload.message_id in (poll[1] for poll in self.polls):

            message = await self.client.get_channel(payload.channel_id).fetch_message(payload.message_id)

            for reaction in message.reactions:

                if (not payload.member.bot

                        and payload.member in await reaction.users().flatten()

                        and reaction.emoji != payload.emoji.name):
                    await message.remove_reaction(reaction.emoji, payload.member)

    async def complete_poll(self, channel_id, message_id):
        message = await self.client.get_channel(channel_id).fetch_message(message_id)

        most_voted = max(message.reactions, key=lambda r: r.count)

        await message.channel.send(
            f"The results are in and option {most_voted.emoji} was the most popular with {most_voted.count - 1:,} votes!")
        self.polls.remove((message.channel.id, message.id))


def setup(client):
    client.add_cog(Example(client))