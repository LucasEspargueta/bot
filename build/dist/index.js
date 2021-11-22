import DiscordJS from "discord.js";
import dotenv from 'dotenv';
dotenv.config();
const client = new DiscordJS.Client({
    intents: [
        DiscordJS.Intents.FLAGS.GUILDS,
        DiscordJS.Intents.FLAGS.GUILD_MESSAGES,
        DiscordJS.Intents.FLAGS.GUILD_MEMBERS
    ]
});
client.on('ready', () => {
    var _a;
    console.log(DiscordJS.Intents, "Tou ligado bro siga siga!");
    const guildID = '759849368966004767';
    const guild = client.guilds.cache.get(guildID);
    let commands;
    if (guild) {
        commands = guild.commands;
    }
    else {
        commands = (_a = client.application) === null || _a === void 0 ? void 0 : _a.commands;
    }
    commands === null || commands === void 0 ? void 0 : commands.create({
        name: "ping",
        description: "responde pong ajaj xd. ri-te :gun:",
    });
});
client.on('interactionCreate', async (interaction) => {
    if (!interaction.isCommand()) {
        return;
    }
    const { commandName } = interaction;
    if (commandName === "ping") {
        interaction.reply({
            content: "pong",
        });
    }
    switch (commandName) {
        case "ping":
            interaction.reply({
                content: "pong",
            });
            break;
        case "print":
            interaction.reply({
                content: "pong",
            });
        default:
            break;
    }
});
client.login(process.env.TOKEN);
//# sourceMappingURL=index.js.map