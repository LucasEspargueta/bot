import DiscordJS, { CommandInteraction, GuildMember, Intents, TextChannel } from "discord.js";
import { ApplicationCommandOptionTypes } from "discord.js/typings/enums";
import dotenvflow from 'dotenv-flow';
import * as youtube from "youtube-random-video";
import { EMOTES } from "./dicts";

dotenvflow.config()
const canaisduvida = ["759883187508871188", "808348984053465118", "808347735580868688", "805416620049956875"]

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
let vitrine: DiscordJS.TextChannel
client.on('ready', async () => {
    console.log("Tou ligado bro siga siga!")
    const guildID = '759849368966004767'
    vitrine = (await client.channels.fetch("853354421165228052"))! as DiscordJS.TextChannel
    const guild = client.guilds.cache.get(guildID)
    let commands = guild?.commands ?? client.application?.commands;
    
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
                type: ApplicationCommandOptionTypes.STRING,
                required: true,
            },
        ]
    });
    // (await 
    commands?.create({
        name: "comm",
        description: "Admin only command",
        options: [
            {
                name: "role",
                description: "The role you want to send the message to",
                type: ApplicationCommandOptionTypes.ROLE,
                required: true,
            },
            {
                name: "message",
                description: "The message you want to send",
                type: ApplicationCommandOptionTypes.STRING,
                required: true,
            },
        ],
        defaultPermission: false

    })
    // )?.permissions.add({
    //     guild: guildID,
    //     permissions: [{
    //         id: "759882119799111681", type: "ROLE", permission: true,
    //     }]
    // });
    commands?.create({
        name: "members",
        description: "Lists all the members of the server",
    })
    commands?.create({
        name: "search",
        description: "Searches for a video on youtube",
    })
    commands?.create({
        name: "joined",
        description: "Tells you when you joined the server",
    })
    commands?.create({
        name: "cls",
        description: "Clears the screen",
    });

    //thing to send the emotes and trigger messages
    client.on("messageCreate", async (message) => {
        if (message.author.bot) return;
        const emotes: Set<string> = new Set();
        message.content?.split(" ").forEach(word => {
            if (word in EMOTES) {
                emotes.add(EMOTES[word])
            }
        });
        if (emotes.size)
            message.reply(`${[...emotes].join(" ")}`)
        //vitrine stuff
        if (/^\[.+\].*$/.test(message.content) && canaisduvida.includes(message.channel.id)) {
            const embed = new DiscordJS.MessageEmbed({
                title: (message.channel as TextChannel).name,
                description: '**' + message.content + '** \n[Vê aqui](' + message.url + ') <a:leftarrow15:853378234405486593> <a:leftarrow15:853378234405486593>',
                color: parseInt(randomColor().replace("#", "0x"), 16),
                timestamp: new Date(),
                image: message.attachments.size ? { url: message.attachments.first()!.url } : undefined,
                footer: {
                    text: "Copia a pergunta para a barra de pesquisas para ver se já tem resposta! ",
                    icon_url: message.author.avatarURL() ?? undefined,
                }
            })
            vitrine.send({ embeds: [embed] })
        }
        if (message.content.startsWith("poll: ")) {
            if (!message.content.includes("|")) {
                await message.react("👍")
                await message.react("👎")
            } else {
                const poll_react = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯']
                for (const emoji of poll_react.splice(0, message.content.split("|").length)) {
                    await message.react(emoji)
                }
            }
        }
    })

    const cls = () => {
        return String("‍‍‍‍\n");
    }

    const screenshotfn = () => {
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
        console.log(interaction.member?.user.username + " sent a message in the vent channel")
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

    //commands
    client.on('interactionCreate', async (interaction) => {
        if (!interaction.isCommand()) {
            return
        }
        const { commandName } = interaction
        switch (commandName) {
            case "screenshot":
                interaction.reply({
                    content: ('https://prnt.sc/' + screenshotfn()),
                    ephemeral: true
                })
                break;
            case "vent":
                ventfn(interaction)
                break;
            case "comm":
                commfn(interaction)
                break;
            case "cls":
                interaction.reply({
                    content: (cls().repeat(100)),
                })
                break;
            case "members":
                const guild = client.guilds.cache.get("759849368966004767")
                if (guild) {
                    const guildmembers = (await guild.members.fetch())
                    const members = guildmembers.filter(m => !m.user.bot).size
                    const mbots = guildmembers.filter(m => m.user.bot).size
                    interaction.reply({
                        content: `There are ${members} members in the server! And ${mbots} bots!`
                    })
                }
                break;
            case "search":
                youtube.getRandomVid(process.env.YOUTUBE_API_KEY, function (err, data) {
                    //data is a JSON object
                    if (err) {
                        console.error(err)
                        interaction.reply({
                            content: "Error",
                        })
                        return
                    }
                    const url = data.id.videoId
                    interaction.reply({
                        content: `https://www.youtube.com/watch?v=${url}`,
                    })
                })
                break;
            case "joined":
                const joined = (interaction.member as GuildMember).joinedAt
                const joineddate = new Date(joined ?? new Date())
                const now = new Date()
                const diff = now.getTime() - joineddate.getTime()
                const days = Math.floor(diff / (1000 * 60 * 60 * 24))
                const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
                const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))
                const seconds = Math.floor((diff % (1000 * 60)) / 1000)
                interaction.reply({
                    content: `${interaction.member?.user} joined the server ${days} days, ${hours} hours, ${minutes} minutes and ${seconds} seconds ago!`,
                    ephemeral: true
                })
                break;
            default:
                break;
        }
    })
})
client.login(process.env.MAMAS).then(() => {
    client.user?.setPresence({
        activities: [{
            name: 'Facebook Marketplace',
            type: 'STREAMING'
        }],
        status: 'online'
    });
});