import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = "your_token_here"

@client.event
async def on_ready():
    print('Bot is working!')

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
                print("Bot does not have permission to delete messages.")
    else:
        # Send message
        await message.channel.send(message.content)
        # Wait for 1 second before deleting the original message
        await asyncio.sleep(1)
        # Delete original message sent by the user
        try:
            await message.delete()
        except discord.errors.Forbidden:
            print("Bot does not have permission to delete messages.")

client.run(TOKEN)