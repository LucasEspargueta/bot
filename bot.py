import random
from discord.ext import commands
from pretty_help import PrettyHelp
import discord
import os
import time
from datetime import datetime
from pytz import timezone
import asyncio
import re

#for time command
now = datetime.now(timezone('Europe/Lisbon'))
current_time = now.strftime("%H:%M:%S")

#important
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="gimme ", intents = intents)

#sexy help
color = 0xb317da
client.help_command = PrettyHelp(color=color)

TIMEZONES = {
	"GMTM12": "Pacific/Auckland",
    "EST": "Etc/GMT+4",
    "GMT": "Etc/GMT",
    "PST": "Etc/GMT+7",
    "GMTM10": "Etc/GMT+10",
    "WET":'Europe/Lisbon',
    "GMTP13": "US/Samoa",
    "CST": "Etc/GMT+5",
    "TUGA": "Europe/Lisbon",
    "CET": "Europe/Madrid",
    "GMTM9": "Etc/GMT+9",
    "GMTM8": "US/Alaska",
    "GMTM7": "Etc/GMT+7",
    "GMTM6": "Etc/GMT+6",
    "GMTM5": "Etc/GMT+5",
    "GMTM4": "Etc/GMT+4",
    "GMTM3": "Etc/GMT+3",
    "GMTM2": "Etc/GMT+2",
    "GMTM1": "Etc/GMT+1",
    "GMTP2": "Europe/Madrid",
    "GMTP3": "Europe/Helsinki",
    "GMTP4": "Asia/Dubai",
    "GMTP5": "Asia/Karachi",
    "GMTP6": "Asia/Dhaka",
    "GMTP7": "Asia/Bangkok",
    "GMTP8": "Asia/Hong_Kong",
    "GMTP9": "Asia/Tokyo",
    "GMTP10": "Australia/Sydney",
    "GMTP11": "Asia/Magadan",
    "GMTP12": "Pacific/Auckland"
}


EMOTES = {
    "5Head" : 'https://cdn.discordapp.com/attachments/822774646981263360/847231713909801001/5Head.png',
    "AYAYA" : 'https://cdn.discordapp.com/attachments/822774646981263360/847231719370653766/AYAYA.png',
    "blobDance" :'https://cdn.discordapp.com/attachments/822774646981263360/847231726790246410/blobDance.gif',
    "catJAM" : 'https://cdn.discordapp.com/attachments/822774646981263360/847231735586619412/catJAM.gif',
    "Clap" : 'https://cdn.discordapp.com/attachments/822774646981263360/847232785138974731/Clap.gif',
    "COGGERS" : 'https://cdn.discordapp.com/attachments/822774646981263360/847232787504955509/COGGERS.gif',
    "EZ" : 'https://cdn.discordapp.com/attachments/822774646981263360/847232790630236170/EZ.png',
    "gachiHYPER" : 'https://cdn.discordapp.com/attachments/822774646981263360/847232798863392808/gachiHYPER.gif',
    "HACKERMANS" : 'https://cdn.discordapp.com/attachments/822774646981263360/847233551007350864/HACKERMANS.gif',
    "modCheck": 'https://cdn.discordapp.com/attachments/822774646981263360/847233559667671040/modCheck.gif',
    "monkaSTEER" :'https://cdn.discordapp.com/attachments/822774646981263360/847233563799453696/monhaSTEER.gif',
    "monkaTOS":'https://cdn.discordapp.com/attachments/822774646981263360/847233957603180574/monkaTOS.gif',
    "monkaSHAKE":'https://cdn.discordapp.com/attachments/822774646981263360/847233953475199016/monkaSHAKE.gif',
    "monkaS":'https://cdn.discordapp.com/attachments/822774646981263360/847233949301604422/monkaS.png',
    "monkaGUN":'https://cdn.discordapp.com/attachments/822774646981263360/847233943233232956/monkaGUN.png',
    "NOPERS":'https://cdn.discordapp.com/attachments/822774646981263360/847234529189298177/NOPERS.gif',
    "NODDERS":'https://cdn.discordapp.com/attachments/822774646981263360/847234515558596628/NODDERS.gif',
    "monkaX":'https://cdn.discordapp.com/attachments/822774646981263360/847234520536186911/monkaX.gif',
    "peepoLeave":'https://cdn.discordapp.com/attachments/822774646981263360/847234915203809330/peepoLeave.gif',
    "peepoArrive":'https://cdn.discordapp.com/attachments/822774646981263360/847234906551091211/peepoArive.gif',
    "peepoClap":'https://cdn.discordapp.com/attachments/822774646981263360/847234911257624636/peepoClap.gif',
    "OMEGALUL":'https://cdn.discordapp.com/attachments/822774646981263360/847234902193209344/omegalul.png',
    "pepeD":'https://cdn.discordapp.com/attachments/822774646981263360/847235635235913798/pepeD.gif',
    "peepoRun":'https://cdn.discordapp.com/attachments/822774646981263360/847235622355599360/peepoRun.gif',
    "peepoPooPoo":'https://cdn.discordapp.com/attachments/822774646981263360/847235613144383508/peepoPooPoo.gif',
    "peepoSIMP":'https://cdn.discordapp.com/attachments/822774646981263360/847235629620527104/peepoSIMP.gif',
    "PepeHands":'https://cdn.discordapp.com/attachments/822774646981263360/847236478559846451/PepeHands.png',
    "PepegaAim":'https://cdn.discordapp.com/attachments/822774646981263360/847236463603220500/PepegaAim.gif',
    "POGGERS":'https://cdn.discordapp.com/attachments/822774646981263360/847236849722064926/POGGERS.png',
    "PETTHEMODS":'https://cdn.discordapp.com/attachments/822774646981263360/847236843338203186/PETTHEMODS.gif',
    "PepePls":'https://cdn.discordapp.com/attachments/822774646981263360/847236838091259974/PepePls.gif',
    "pepeJAM":'https://cdn.discordapp.com/attachments/822774646981263360/847236832940523520/pepeJAM.gif',
    "TriDance":'https://cdn.discordapp.com/attachments/822774646981263360/847237873232511036/TriDance.gif',
    "SumSmash":'https://cdn.discordapp.com/attachments/822774646981263360/847237869185794119/sumSmash.gif',
    "ricardoFlick":'https://cdn.discordapp.com/attachments/822774646981263360/847237868921683978/ricardoFlick.gif',
    "popCat":'https://cdn.discordapp.com/attachments/822774646981263360/847237862029393920/popCat.gif',
    "FeelsGoodMan":"https://cdn.discordapp.com/attachments/822774646981263360/848672889733382184/FeelsGoodMan.png",
    "Kreygasm":"https://cdn.discordapp.com/attachments/822774646981263360/848672894930255922/Kreygasm.png",
    "HeyGuys": "https://cdn.discordapp.com/attachments/822774646981263360/848672900578803752/HeyGuys.png",
    "PJSalt":"https://cdn.discordapp.com/attachments/822774646981263360/848673908961837096/pjsalt.png",
    "Jebaited":"https://cdn.discordapp.com/attachments/822774646981263360/848672947980075008/Jebait.png",
    "WutFace":"https://cdn.discordapp.com/attachments/822774646981263360/848672943415361566/wutface-transparent-1.png"
    }

#rich presence
async def status():
    a = random.randint(1, 4)
    if a==1:
      await client.change_presence(activity=discord.Game(name="Among Us"))
    if a==2:
      await client.change_presence(activity=discord.Streaming(name="Cute animals", url='https://www.twitch.tv/marinemammalrescue'))
    if a==3:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="https://open.spotify.com/playlist/5RZQwNffu3pWAWiLc5yrfM"))
    if a==4:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Cars"))
    await asyncio.sleep(0)

@client.event
async def on_ready():
    print('Vim-me!')
    global guild
    guild = client.get_guild(int(759849368966004767))
    print(guild)
    await status()

@client.command(help = "Gives you a random screenshot from the www, if you see anything inappropriate, please report it!")
async def prnt(ctx):
    lista = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    await ctx.reply("https://prnt.sc/" + "".join(list(random.choices(lista, k=6))))
    
@client.command(help = 'Gives you a random video from the www, if you see anything inappropriate, please report it!')
async def video(ctx):
    lista = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    await ctx.reply("https://streamable.com/" + "".join(list(random.choices(lista, k=6))))
    
@client.command(help = 'Gives you the time in different timezones. Try EST, PST, GMT, WET, CST & CET')
async def time(ctx, command="TUGA"):
    newtime = datetime.now(timezone(TIMEZONES[command.upper()])) if command.upper() in TIMEZONES.keys() else None

    if newtime:    
        current_time = newtime.strftime("%H:%M:%S")
        print(str(timezone), current_time)
        await ctx.reply(current_time)

@client.event
async def on_message(msg):
    if msg.author == client.user:
       return
    a = [EMOTES[s] for s in msg.content.split() if s in EMOTES]
    if a:
        await msg.channel.send("\n".join(a[:10]))
    if msg.author == msg.guild.get_member(331231536106176512):
        mention = f'<@!{client.user.id}>'
        if "amo-te" in msg.content.lower() and mention in msg.content.lower(): 
            await msg.reply('também te amo')
    if re.search(r"\btoni\b", msg.content, flags=re.I) is not None:
       await msg.reply("Tony")
    if "booba gif" in msg.content.lower():
        await msg.reply('https://i1.wp.com/media.tenor.com/images/3634fc2d789bdb041ec2d3088100ba7e/tenor.gif')
    if "big homies" in msg.content.lower():
       await msg.reply("https://cdn.discordapp.com/attachments/786571345072357376/843609641078620220/homies.png")
    if re.search(r"\bsimp\b", msg.content, flags=re.I) is not None:
       await msg.reply("https://cdn.discordapp.com/attachments/759903575748640798/843586394642317352/tEYCU9Ew.png")	
    if "ahegao gigante" in msg.content.lower():
       await msg.reply("https://cdn.discordapp.com/attachments/786571345072357376/842871472418193408/81376121441170228311.png")
    if "peraschamp" in msg.content.lower():
       await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/842518533888147486/unknown-2.jpg")
    if "letroll gigante" in msg.content.lower():
       await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/842824588042698762/IMG-20210505-WA0018_1.jpg")
    if re.search(r"\bwoo+\b", msg.content, flags=re.I) is not None:
       await msg.reply("https://tenor.com/view/pop-smoke-dance-nyc-dance-move-smile-gif-16391422")
    if "this gigante" in msg.content.lower():
       await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/838739007415386112/this.png")
    if "among us" in msg.content.lower() or "amogus" in msg.content.lower():
       await msg.reply('among us')
    if "pedro ramalho" in msg.content.lower():
       await msg.reply('Pedro Ramalho \n https://cdn.discordapp.com/attachments/759882556744663040/818850186754785310/unknown.png')
    if "dababy" in msg.content.lower() or "less go" in msg.content.lower():
       await msg.reply("https://cdn.discordapp.com/attachments/379034825304178712/822505085820862494/IMG_20210318_233715.jpg")
    elif "balta" in msg.content.lower():
       num = random.randint(0, 100000)
       if num == 69420:
         await msg.reply('https://cdn.discordapp.com/attachments/759882556744663040/822255453677289482/SPOILER_unknown.png')
         print('racismo')
    await client.process_commands(msg)
    
@client.command(help='AWOOOOOOOOOOOO AND THE CUM WONT STOP')
async def cum(ctx):
   await ctx.reply('https://www.youtube.com/watch?v=uJ_1HMAGb4k')
@client.command(help="i mean")
async def gangnamstyle(ctx):
   await ctx.reply('https://www.youtube.com/watch?v=9bZkp7q19f0')
@client.command(help="PUSH TO THE GITHUB")
async def git(ctx):
   await ctx.reply('https://media.giphy.com/media/OOXp2e1gCnfj6jGxN9/giphy.gif')
@client.command(help="it's me")
async def creator(ctx):
    await ctx.reply('https://github.com/LucasSexo/')
@client.command(help="it's domking")
async def domking(ctx):
    await ctx.reply('https://media.discordapp.net/attachments/759882556744663040/848589067305091102/makesweet-a1gvuu.gif')
    
client.run(os.environ["token"])
