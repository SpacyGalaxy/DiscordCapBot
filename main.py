import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


bot = commands.Bot(command_prefix='=')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

# TOKEN = os.getenv('TOKEN')

@bot.event
async def on_message(message):
    
    if message.author.id != bot.user.id:
    
        role = discord.utils.get(message.guild.roles,name="capper")
        if role in message.author.roles:
            emoji = '\N{BILLED CAP}'
            await message.add_reaction(emoji)
        else: 
            #await message.channel.send("Nice you not capping")
            return
        #discord.utils.get(guild.roles,name="capper")
bot.run(TOKEN)
