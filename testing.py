import discord
from discord.ext import tasks
import asyncio
from itertools import cycle
from pushsafer import Client
from datetime import datetime
from requests import get

push = Client('fkpEkezGV9NvqxmzVlCf')

key = '4fe777d7-b24e-4d31-a470-ad16d46f9e67'
guild = 'Gamer%20Buddies'

client = discord.Client()

@tasks.loop(seconds=20)
async def get_gexp():
    await client.wait_until_ready()

    testingchannel = client.get_channel(769996720557260850)
    await testingchannel.send('Updated')

    channel = client.get_channel(943465265902022686)

    while not client.is_closed:
        currentTime = datetime.now()
        if currentTime.weekday == 5 and currentTime.hour == 23 and currentTime.minute == 59:
            data = get(f'https://api.hypixel.net/guild?key={key}&name={guild}').json()
        for member in data['guild']['members']:
            temp = get(f'https://sessionserver.mojang.com/session/minecraft/profile/{member["uuid"]}').json()
            username = temp['name']
            tempgexp = 0
            for item in member['expHistory']:
                exp = member['expHistory'][item]
                tempgexp += exp
            if tempgexp >= 100000:
                rank = 'Mythical'
            elif tempgexp >= 40000:
                rank = 'Legendary'
            else:
                rank = 'Ordinary'
            channel.send(f'{username} got {tempgexp} exp in the past 7 days. They get {rank} rank')
        push.send_message("Task completed successfully", device=49210)

@client.event
async def on_ready():
    push.send_message("{0.user} has logged in at {1}".format(client, datetime.now()), device=49210)


@client.event
async def on_message(message):
    if message.content.startswith('&'):
        await message.reply('Lmao')


get_gexp.start()
client.run('OTEwMDg2NjcyMTY5OTY3NjQ4.YZNuQw.5Ccrj0UueR5iEkS7OTlNG-HYzis')