import discord
import os
import logging
import datetime as dt

logging.basicConfig(filename='bot.log', encoding='utf-8', level=logging.DEBUG)

intents = discord.Intents().all()
client = discord.Client(intents=intents)
welcome =  lambda member: f"""
Hey {member.name} welcome to our server! We hope you have a great stay here :) 
Make sure to check out some important channels :-
• #📜︱code-of-conduct - Rules of our server.
• #📿︱roles - Get your roles here.
• #💬︱main-quad - Talk with new peoples and make new freinds.
• Fill out the form if you want to join our team - https://airtable.com/shrKny0ewLRxFvidc

"""

"""
def check_time():
    time = dt.dt.now()
    nft = date.strftime("%H:%M:%S")
    return nft
"""

def check_date():
    date = dt.date.today()
    return date


@client.event
async def on_ready():
    logging.info(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Hello' or message.content == 'hello':
        await message.channel.send("Technophiles")

    if message.content == 'date' or message.content == 'Date':
        d_res = check_date()
        await message.channel.send(d_res)

@client.event
async def on_member_join(member):
    print(f'Recognised that a member called {member.name} joined')
    try:
        await member.send(welcome(member))
        print(f'mesaage sent to {member.name}')
    except:
        print(f'Couldn\'t message {member.name}')

    embed=discord.Embed(
        title = f'Welcome {member.name}',
        description = f'We\'re so glad you\'re here!',
        color = discord.Color.blue()
    )

@client.event
async def on_member_leave(member):
    print(f'Recognised that a member called {member.name} left')
    await member.send(f"{member.name} why you left the group")
    print(f"{member.name} left")
    embed = discord.Embed(
        title = f'Goodbye {member.name}!',
        description = 'Until we meet again old friend.',
        color=discord.Color.red()
    )

client.run('TOKEN')
