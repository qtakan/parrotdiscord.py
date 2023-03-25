import discord
from discord.ext import commands
from utils import * 
from functions import *
import time
import asyncio


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)



@client.event
async def on_ready():
    print('BOT ÇALIŞIYOR!')

@client.command()
async def atakan(ctx):
    await ctx.send(f'deneme {ctx.author.mention}')

@client.command()
async def a(ctx, *, message):
    await ctx.send(message)



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.attachments:
        for attachment in message.attachments:
            # Download the attachment
            await attachment.save(attachment.filename)
            # Send the attachment back
            await message.channel.send(file=discord.File(attachment.filename))
            # Delete the original message
            try:
                await message.delete()
            except discord.errors.Forbidden:
                print("Bunu silmeye hakkım yok..")
    else:
        # Send message
        await message.channel.send(message.content)
        # Wait for 1 second before deleting the original message
        await asyncio.sleep(1)
        # Delete original message sent by the user
        try:
            await message.delete()
        except discord.errors.Forbidden:
            print("Bunu silmeye hakkım yok.")



client.run(TOKEN)
