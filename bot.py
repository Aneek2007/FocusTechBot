import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Hello':
        await message.channel.send("Technophiles")


client.run('TOKEN')
