import { ApplicationCommandOptionType } from "discord-api-types"
import DiscordJS, { CommandInteraction, Intents } from "discord.js"
import dotenvflow from 'dotenv-flow'
dotenvflow.config()

const client = new DiscordJS.Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.GUILD_MEMBERS,
        Intents.FLAGS.GUILD_BANS,
        Intents.FLAGS.GUILD_EMOJIS_AND_STICKERS,
        Intents.FLAGS.GUILD_INTEGRATIONS,
        Intents.FLAGS.GUILD_WEBHOOKS,
        Intents.FLAGS.GUILD_INVITES,
        Intents.FLAGS.GUILD_VOICE_STATES,
        Intents.FLAGS.GUILD_PRESENCES,
        Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
        Intents.FLAGS.GUILD_MESSAGE_TYPING,
        Intents.FLAGS.DIRECT_MESSAGES,
        Intents.FLAGS.DIRECT_MESSAGE_REACTIONS,
        Intents.FLAGS.DIRECT_MESSAGE_TYPING,
    ]
})

client.on('ready', async () => {
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
    });
    (await commands?.create({
        name: "comm",
        description: "Admin only command",
        options: [
            {
                name: "role",
                description: "The role you want to send the message to",
                type: ApplicationCommandOptionType.Role,
                required: true,
            },
            {
                name: "message",
                description: "The message you want to send",
                type: ApplicationCommandOptionType.String,
                required: true,
            },
        ],
        defaultPermission: false

    }))?.permissions.add({
        guild: guildID,
        permissions: [{
            id: "759882119799111681", type: "ROLE", permission: true,
        }]
    });
})

function screenshotfn() {
    const lista = ["a", "b", "c", "d", "e", "f",
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

const ventfn = async (interaction: CommandInteraction) => {
    const desabafo = await client.channels.fetch("796509327997403156")
    const embed = new DiscordJS.MessageEmbed({
        title: "Anon says",
        description: interaction.options.getString("message", true),
        color: parseInt(randomColor().replace("#", "0x"), 16),
        timestamp: new Date(),
    })
    if (desabafo?.isText()) {
        desabafo.send({ embeds: [embed] })
    }
    interaction.reply({
        ephemeral: true,
        content: "Message sent!"
    })
}

const commfn = async (interaction: CommandInteraction) => {
    const role = interaction.options.getRole("role", true)

    if (role instanceof DiscordJS.Role) {
        role.members.forEach(member => {
            member.send(interaction.options.getString("message", true))
        });
        interaction.reply({
            ephemeral: true,
            content: "Message sent!"
        })
        return

    }
    interaction.reply({
        ephemeral: true,
        content: "Message not sent!"
    })
}

client.on('interactionCreate', async (interaction) => {
    if (!interaction.isCommand()) {
        return
    }
    const { commandName } = interaction
    switch (commandName) {
        case "screenshot":
            interaction.reply({
                content: ('https://prnt.sc/' + screenshotfn()),
            })
            break;
        case "vent":
            ventfn(interaction)
            break;
        case "comm":
            commfn(interaction)
            break;
        default:
            break;
    }
})

client.login(process.env.MAMAS).then(() => {
    client.user?.setPresence({
        activities: [{
            name: 'FEUPers behaviour',
            type: 'WATCHING'
        }],
        status: 'idle'
    });
});