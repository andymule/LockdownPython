# bot.py
import os
import discord
from discord.ext import commands
import random

TOKEN = "Njk3NzI2MjYxMzA0MzYwOTcx.Xo7oRw.VLl1VBKADA2VGK9M18y8qPOJ2FI"
GUILD = "Church"

client = discord.Client()
# bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'Praise HIM.',
        'Glory be to HIM.',
        "To HIM be the glory.",
    ]

    if "him" in message.content:
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

client.run(TOKEN)
