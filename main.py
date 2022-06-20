import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


bot = commands.Bot(command_prefix='=')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('with cappers since \'22')) # Status
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.event
async def on_message(message): 
    
    if message.author.id != bot.user.id: #Makes sure that the bot doesn't react to their own messages
    
        role = discord.utils.get(message.guild.roles,name="capper") #will search for a role named "capper" in the server
        if role in message.author.roles: #If a user has the specific role in the server, then react their messages with a billed cap
            emoji = '\N{BILLED CAP}'
            await message.add_reaction(emoji)
        else: #else return
            return
    await bot.process_commands(message)

@bot.command()
async def servers(ctx):
  servers = list(bot.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in bot.guilds))

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

TOKEN = os.environ('TOKEN')


bot.run(TOKEN) #bot token
