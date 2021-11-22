import { ApplicationCommandOptionType } from "discord-api-types"
import DiscordJS, { CommandInteraction, Intents } from "discord.js"
import dotenvflow from 'dotenv-flow'
dotenvflow.config()

const client = new DiscordJS.Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.GUILD_MEMBERS
    ]
})

client.on('ready', () =>{
    console.log("Tou ligado bro siga siga!")
    const guildID = '759849368966004767'
    const guild = client.guilds.cache.get(guildID)
    let commands
    if (guild) {
        commands = guild.commands
    } else {
        commands = client.application?.commands
    }
    commands?.create({
        name: "ping",
        description: "responde pong ajaj xd. ri-te :gun:",
    })
    commands?.create({
        name: "screenshot",
        description: "Shows you a random screenshot from the web, if you see anything inappropriate please report it.",
    })
    commands?.create({
        name: "vent",
        description: "Lets you use the vent channel while maintaining anonymity.",
        options: [
            {
                name: "message",
                description: "The message you want to send",
                type: ApplicationCommandOptionType.String,
                required: true,
            },
        ] 
    })
})

function screenshotfn() {
    const lista=["a", "b", "c", "d", "e", "f",
    "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r",
    "s", "t", "u", "v", "x", "y", "z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    return lista.sort(() => Math.random() - Math.random()).slice(0, 6).join("")
}
//random color generator
const randomColor = () => {
    const letters = '0123456789ABCDEF'
    let color = '#'
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)]
    }
    return color
}

const ventfn=async(interaction: CommandInteraction)=>{
    const desabafo = await client.channels.fetch("796509327997403156")
    const embed= new DiscordJS.MessageEmbed({
        title: "Anon says",
        description: interaction.options.getString("message",true),
        color: parseInt(randomColor().replace("#", "0x"), 16),
        timestamp: new Date(),
    })
    if (desabafo?.isText()) {
        desabafo.send({embeds: [embed]})
    }
    interaction.reply({
        ephemeral: true,
        content: "Message sent!"
    })
}

client.on('interactionCreate', async (interaction) =>{
    if (!interaction.isCommand()) {
        return
    }
    const { commandName} = interaction
    switch (commandName) {
        case "ping":
            interaction.reply({
                content: "pong",
            })
            break;
        case "screenshot":
            interaction.reply({
                content: ('https://prnt.sc/' + screenshotfn()),
            })
            break;
        case "vent":
            ventfn(interaction)
            break;
        default:
            break;
    }
})

client.login(process.env.MAMAS)