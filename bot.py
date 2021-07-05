import random
from discord import message
from discord.ext import commands
from pretty_help import PrettyHelp
import discord
import os
import time
from datetime import datetime
from pytz import timezone
import asyncio
import re
import asyncpraw
import requests

#reddit

reddit = asyncpraw.Reddit(client_id = "E7ja3WGqt2ToJA",
                     client_secret = os.environ['client_secret'],
                     username = "GriloDaFCUP",
                     password = os.environ['password'],
                     user_agent = "GriloDaFCUP 1.0 by /u/GriloDaFCUP")

# for time command
now = datetime.now(timezone('Europe/Lisbon'))
current_time = now.strftime("%H:%M:%S")

# important
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="gimme ", intents=intents)

# sexy help
color = 0xb317da
client.help_command = PrettyHelp(color=color)

TIMEZONES = {
    "GMTM12": "Pacific/Auckland",
    "EST": "Etc/GMT+4",
    "GMT": "Etc/GMT",
    "PST": "Etc/GMT+7",
    "GMTM10": "Etc/GMT+10",
    "WET": 'Europe/Lisbon',
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
    "4Weird": "https://cdn.discordapp.com/attachments/837324450588393476/851618951367884830/4Weird.png",
    "5Head": 'https://cdn.discordapp.com/attachments/822774646981263360/847231713909801001/5Head.png',
    "AYAYA": 'https://cdn.discordapp.com/attachments/822774646981263360/847231719370653766/AYAYA.png',
    "BBoomer": "https://cdn.discordapp.com/attachments/786571345072357376/851588811137220639/BBoomer.gif",
    "blobDance": 'https://cdn.discordapp.com/attachments/822774646981263360/847231726790246410/blobDance.gif',
    "catJAM": 'https://cdn.discordapp.com/attachments/822774646981263360/847231735586619412/catJAM.gif',
    "Clap": 'https://cdn.discordapp.com/attachments/822774646981263360/847232785138974731/Clap.gif',
    "COCKA": "https://cdn.discordapp.com/attachments/786571345072357376/851585851929395230/COCKA.gif",
    "COGGERS": 'https://cdn.discordapp.com/attachments/822774646981263360/847232787504955509/COGGERS.gif',
    "COPIUM": "https://cdn.discordapp.com/attachments/837324450588393476/851621262840692736/COPIUM.png",
    "coronaS": "https://cdn.discordapp.com/attachments/786571345072357376/851587544876318720/coronaS.png",
    "D:": "https://cdn.discordapp.com/attachments/786571345072357376/851588276950401054/D.png",
    "Drake": "https://cdn.discordapp.com/attachments/786571345072357376/851585499708915712/Drake.gif",
    "EZ": 'https://cdn.discordapp.com/attachments/822774646981263360/847232790630236170/EZ.png',
    "FeelsGoodMan": "https://cdn.discordapp.com/attachments/822774646981263360/848672889733382184/FeelsGoodMan.png",
    "gachiHYPER": 'https://cdn.discordapp.com/attachments/822774646981263360/847232798863392808/gachiHYPER.gif',
    "GRUG": "https://cdn.discordapp.com/attachments/786571345072357376/851587814231375922/GRUG.png",
    "HACKERMANS": 'https://cdn.discordapp.com/attachments/822774646981263360/847233551007350864/HACKERMANS.gif',
    "HeyGuys": "https://cdn.discordapp.com/attachments/822774646981263360/848672900578803752/HeyGuys.png",
    "HOGGERS": "https://cdn.discordapp.com/attachments/837324450588393476/851618490178732062/HOGGERS.png",
    "Jebaited": "https://cdn.discordapp.com/attachments/822774646981263360/848672947980075008/Jebait.png",
    "KKomrade": "https://cdn.discordapp.com/attachments/837324450588393476/851620502463053854/KKomrade.png",
    "KKona": "https://cdn.discordapp.com/attachments/837324450588393476/851619733656174612/KKona.png",
    "Kreygasm": "https://cdn.discordapp.com/attachments/822774646981263360/848672894930255922/Kreygasm.png",
    "modCheck": 'https://cdn.discordapp.com/attachments/822774646981263360/847233559667671040/modCheck.gif',
    "monkaGUN": 'https://cdn.discordapp.com/attachments/822774646981263360/847233943233232956/monkaGUN.png',
    "monkaS": 'https://cdn.discordapp.com/attachments/822774646981263360/847233949301604422/monkaS.png',
    "monkaSHAKE": 'https://cdn.discordapp.com/attachments/822774646981263360/847233953475199016/monkaSHAKE.gif',
    "monkaStare": "https://cdn.discordapp.com/attachments/837324450588393476/851620024888066138/monkaStare.png",
    "monkaSTEER": 'https://cdn.discordapp.com/attachments/822774646981263360/847233563799453696/monhaSTEER.gif',
    "monkaTOS": 'https://cdn.discordapp.com/attachments/822774646981263360/847233957603180574/monkaTOS.gif',
    "monkaX": 'https://cdn.discordapp.com/attachments/822774646981263360/847234520536186911/monkaX.gif',
    "NODDERS": 'https://cdn.discordapp.com/attachments/822774646981263360/847234515558596628/NODDERS.gif',
    "NOPERS": 'https://cdn.discordapp.com/attachments/822774646981263360/847234529189298177/NOPERS.gif',
    "Okayge": "https://cdn.discordapp.com/attachments/837324450588393476/851617571223765052/Okayge.png",
    "OMEGALUL": 'https://cdn.discordapp.com/attachments/822774646981263360/847234902193209344/omegalul.png',
    "PagChomp": "https://cdn.discordapp.com/attachments/837324450588393476/851608969293725706/PagChomp.png",
    "PagMan": "https://cdn.discordapp.com/attachments/837324450588393476/851617590170222622/PagMan.png",
    "PainsChamp": "https://cdn.discordapp.com/attachments/837324450588393476/851620427541381120/PainsChamp.png",
    "peepoArrive": 'https://cdn.discordapp.com/attachments/822774646981263360/847234906551091211/peepoArive.gif',
    "peepoChat": "https://cdn.discordapp.com/attachments/837324450588393476/851621001472114719/peepoChat.gif",
    "peepoClap": 'https://cdn.discordapp.com/attachments/822774646981263360/847234911257624636/peepoClap.gif',
    "peepoG": "https://cdn.discordapp.com/attachments/786571345072357376/851587167326044190/peepoG.png",
    "peepoGiggles": "https://cdn.discordapp.com/attachments/786571345072357376/851586967068999690/peepoGiggles.gif",
    "peepoKiss": "https://cdn.discordapp.com/attachments/837324450588393476/851619224282857492/peepoKiss.png",
    "peepoLeave": 'https://cdn.discordapp.com/attachments/822774646981263360/847234915203809330/peepoLeave.gif',
    "peepoPooPoo": 'https://cdn.discordapp.com/attachments/822774646981263360/847235613144383508/peepoPooPoo.gif',
    "peepoRun": 'https://cdn.discordapp.com/attachments/822774646981263360/847235622355599360/peepoRun.gif',
    "peepoSIMP": 'https://cdn.discordapp.com/attachments/822774646981263360/847235629620527104/peepoSIMP.gif',
    "pepeD": 'https://cdn.discordapp.com/attachments/822774646981263360/847235635235913798/pepeD.gif',
    "Pepega": "https://cdn.discordapp.com/attachments/837324450588393476/851622139491647548/Pepega.png",
    "PepegaAim": 'https://cdn.discordapp.com/attachments/822774646981263360/847236463603220500/PepegaAim.gif',
    "PepeHands": 'https://cdn.discordapp.com/attachments/822774646981263360/847236478559846451/PepeHands.png',
    "pepeJAM": 'https://cdn.discordapp.com/attachments/822774646981263360/847236832940523520/pepeJAM.gif',
    "PepePls": 'https://cdn.discordapp.com/attachments/822774646981263360/847236838091259974/PepePls.gif',
    "PETTHEMODS": 'https://cdn.discordapp.com/attachments/822774646981263360/847236843338203186/PETTHEMODS.gif',
    "PJSalt": "https://cdn.discordapp.com/attachments/822774646981263360/848673908961837096/pjsalt.png",
    "POGGERS": 'https://cdn.discordapp.com/attachments/822774646981263360/847236849722064926/POGGERS.png',
    "PogO": "https://cdn.discordapp.com/attachments/786571345072357376/851588892490596352/PogO.png",
    "PogU": "https://cdn.discordapp.com/attachments/786571345072357376/851588957233872966/PogU.png",
    "popCat": 'https://cdn.discordapp.com/attachments/822774646981263360/847237862029393920/popCat.gif',
    "ratJAM": "https://cdn.discordapp.com/attachments/786571345072357376/851584604901212230/ratJAM.gif",
    "ricardoFlick": 'https://cdn.discordapp.com/attachments/822774646981263360/847237868921683978/ricardoFlick.gif',
    "SumSmash": 'https://cdn.discordapp.com/attachments/822774646981263360/847237869185794119/sumSmash.gif',
    "TriDance": 'https://cdn.discordapp.com/attachments/822774646981263360/847237873232511036/TriDance.gif',
    "WutFace": "https://cdn.discordapp.com/attachments/822774646981263360/848672943415361566/wutface-transparent-1.png",
    "xqcL": "https://cdn.discordapp.com/attachments/759882556744663040/851789059532652544/6e5.png",
}


# rich presence
async def status():
    a = random.randint(1, 4)
    if a == 1:
        await client.change_presence(activity=discord.Game(name="Among Us"))
    if a == 2:
        await client.change_presence(
            activity=discord.Streaming(name="Cute animals", url='https://www.twitch.tv/marinemammalrescue'))
    if a == 3:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                               name="https://open.spotify.com/playlist/5RZQwNffu3pWAWiLc5yrfM"))
    if a == 4:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Cars"))
    await asyncio.sleep(0)


@client.event
async def on_ready():
    print('Vim-me!')
    global guild
    guild = client.get_guild(int(759849368966004767))
    print(guild)
    await status()


@client.command(help="Gives you a random screenshot from the www, if you see anything inappropriate, please report it!")
async def prnt(ctx):
    lista = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    await ctx.reply("https://prnt.sc/" + "".join(list(random.choices(lista, k=6))))


@client.command(help='Gives you a random video from the www, if you see anything inappropriate, please report it!')
async def video(ctx):
    lista = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    await ctx.reply("https://streamable.com/" + "".join(list(random.choices(lista, k=6))))


@client.command(help='Gives you the time in different timezones. Try EST, PST, GMT, WET, CST & CET')
async def time(ctx, command="TUGA"):
    newtime = datetime.now(timezone(TIMEZONES[command.upper()])) if command.upper() in TIMEZONES.keys() else None

    if newtime:
        current_time = newtime.strftime("%H:%M:%S")
        print(str(timezone), current_time)
        await ctx.reply(current_time)


@client.event
async def on_message(msg):
    m = msg.content.lower()
    if msg.author == client.user:
        return
    a = [EMOTES[s] for s in msg.content.split() if s in EMOTES]
    if a:
        await msg.channel.send("\n".join(a[:10]))
    if "booba gif" in msg.content.lower():
        await msg.reply('https://i1.wp.com/media.tenor.com/images/3634fc2d789bdb041ec2d3088100ba7e/tenor.gif')
    if "peras actually" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/851501480317026304/caption.png")
    if "big homies" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/786571345072357376/843609641078620220/homies.png")
    if re.search(r"\bsimp\b", msg.content, flags=re.I) is not None:
        await msg.reply("https://cdn.discordapp.com/attachments/759903575748640798/843586394642317352/tEYCU9Ew.png")
    if "ahegao gigante" in msg.content.lower():
        await msg.reply(
            "https://cdn.discordapp.com/attachments/786571345072357376/842871472418193408/81376121441170228311.png")
    if "peraschamp" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/842518533888147486/unknown-2.jpg")
    if "letroll gigante" in msg.content.lower():
        await msg.reply(
            "https://cdn.discordapp.com/attachments/759882556744663040/842824588042698762/IMG-20210505-WA0018_1.jpg")
    if "this gigante" in msg.content.lower():
        await msg.reply("https://cdn.discordapp.com/attachments/759882556744663040/838739007415386112/this.png")
    elif "balta" in msg.content.lower():
        num = random.randint(0, 100000)
        if num == 69420:
            await msg.reply(
                'https://cdn.discordapp.com/attachments/759882556744663040/822255453677289482/SPOILER_unknown.png')
            print('racismo')
    if m.startswith('[') and (
            msg.channel.name == '❓│1º_ano' or msg.channel.name == '❓│2º_ano' or msg.channel.name == '❓│3º-ano' or msg.channel.name == '❔│duvidas') and (
            ']' in m):
        vitrine = client.get_channel(853354421165228052)
        cores = [0x38d42a, 0x1fd1e1, 0x1dda8b, 0x2f55d8, 0xe191e3, 0x6919e7, 0xc949a6]
        duvida = discord.Embed(title=msg.channel.name,
                               description='**' + msg.content + '** \n[Vê aqui](' + msg.jump_url + ') <a:leftarrow15:853378234405486593> <a:leftarrow15:853378234405486593>',
                               color=random.choice(cores))
        if msg.attachments:
            image = msg.attachments[0].url
            duvida.set_image(url=image)
        duvida.set_footer(icon_url=msg.author.avatar_url,
                          text=f"Copia a pergunta para a barra de pesquisas para ver se já tem resposta! ")
        await vitrine.send(embed=duvida)
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
    await ctx.reply(
        'https://media.discordapp.net/attachments/759882556744663040/848589067305091102/makesweet-a1gvuu.gif')

@client.command(help = "sends nudes")
async def nudes(ctx):
    subreddit = await reddit.subreddit("gonewild")
    all_subs = []

    top = subreddit.top("month", limit = 70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.utcnow())
    emb.set_image(url = url)
    emb.color = 0xc4ffed

    mp = await ctx.message.author.create_dm()
    await mp.send(embed = emb)
    print('O {} tá down bad'.format(ctx.message.author.name))
    
    
#desabafo stuff
@client.command()
async def anon(ctx, *, arg):
    if isinstance(ctx.channel, discord.channel.DMChannel):#isto está aqui puramente 
        desabafo = client.get_channel(796509327997403156)#por segurança e evitar spam
        print('O {} desabafou'.format(ctx.message.author.name)) #nao irei nunca divulgar quem usou o comando!
        desembed= discord.Embed(title="Anon says:", color= 0x2e69ff)
        desembed.description = arg
        
        await desabafo.send(embed = desembed)                                

vaccination_max_age, vaccination_last_updated = None, None

@client.command(help="Checks the current max age of vaccination")
async def vacina(ctx):
    global vaccination_max_age, vaccination_last_updated
    now = datetime.now()
    update_interval_secs = 60

    if not vaccination_last_updated or (now - vaccination_last_updated).seconds >= update_interval_secs:
        # Update the stored info
        url = 'https://covid19.min-saude.pt/pedido-de-agendamento/'
        res = requests.get(url)
        regexp_match = re.search('Tem (\d+) ou mais anos e ainda não foi vacinado\(a\)?', res.text)
        vaccination_max_age = regexp_match.group(1)
        vaccination_last_updated = datetime.now()

    colourcaralho = [0x38d42a, 0x1fd1e1, 0x1dda8b, 0x2f55d8, 0xe191e3, 0x6919e7, 0xc949a6, 0x2e69ff]
    vacinaembed= discord.Embed(color= random.choice(colourcaralho))
    vacinaembed.description = (f"Idade max de vacinação atual: **{vaccination_max_age}**. Última atualização: {vaccination_last_updated}\n\n" 
                                   "Para mais informação visita:  [DGS](https://covid19.min-saude.pt/pedido-de-agendamento/)")
    vacinaembed.set_footer(text=f"Vacina-te!")
    await ctx.reply(embed = vacinaembed)

client.run(os.environ["token"])
