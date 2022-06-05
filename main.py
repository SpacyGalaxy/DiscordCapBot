import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


client = discord.Client()
load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    
    role = message.guild.get_role(982749129031708723)
    if message.author != client.user and role in message.author.roles:
        emoji = '\N{BILLED CAP}'
        await message.add_reaction(emoji)

#@client.event
#async def on_bruh(message)

client.run(TOKEN)