import requests
import datetime
import time
import discord_automessage

key = '4fe777d7-b24e-4d31-a470-ad16d46f9e67'
guild = 'Gamer%20Buddies'

while True:
    day = datetime.datetime.now()
    if day.weekday() == 5 and day.hour == 23 and day.minute == 59:
        discord_automessage.sendMessage('943465265902022686', '!clear 100')
        data = requests.get(f'https://api.hypixel.net/guild?key={key}&name={guild}').json()
        for member in data['guild']['members']:
            temp = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{member["uuid"]}').json()
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
            discord_automessage.sendMessage('943465265902022686',f'{username} got {tempgexp} exp in the past 7 days. They get {rank} rank')
            print(username,'done')
        time.sleep(30)