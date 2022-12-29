# This example requires the 'message_content' intent.

import discord
import os
import asyncio
from dotenv import load_dotenv, find_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
load_dotenv(find_dotenv())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

async def main():
    async with client:
        await load()
        await client.start(os.getenv('DISCORD_TOKEN'))

asyncio.run(main())
