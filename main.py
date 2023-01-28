import discord
import asyncio
import requests as rq
from discord.ext import commands,tasks
import datetime

## Setup
client =commands.Bot(intents=discord.Intents.all() , command_prefix= "/" )
client.remove_command('help')

## Config
class config:
    serverIP = "" #server ip
    guildID = "" #Your Discord Server ID, must be int. | Example: 721939142455459902
    Token = "" #Your Discord Bot Token

## Events
@client.event
async def on_ready():
    print('Bot Is Ready!')
    client.my_current_task = live_status.start()

## Players Count Function // Callable Everywhere, returns number
def pc():
    try:
        resp = rq.get('http://'+config.serverIP+'/players.json').json()
        return(len(resp))
    except:
        return('N/A')

##embed message
@client.command()
async def say(ctx,*,arg):
    embed = discord.Embed(title=f"{arg}", color=0x62ecfd)
    time = datetime.datetime.now()
    x=time.strftime("%x")
    y='Sky Comunity'
    embed.set_footer(text=f'{y}│{x}',
    icon_url="https://cdn.discordapp.com/attachments/1062405560684793906/1067348287318921247/20230124_031223_0000.png")
    await ctx.message.delete()
    await ctx.send("||@evetyone||",embed=embed)


## Live Status
@tasks.loop()
async def live_status(seconds=75):
    pcount = pc()
    Dis = client.get_guild(config.guildID) #Int

    activity = discord.Activity(type=discord.ActivityType.watching, name=f'for {pcount} citizen')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)

    mc = Dis.member_count
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="" + str(mc) + " discord member!"))
    await asyncio.sleep(15)


    activity = discord.Activity(type=discord.ActivityType.watching, name=f'anything that you want')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)



client.run(config.Token)