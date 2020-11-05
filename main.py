import discord
import requests

TOKEN = 'token'


client = discord.Client()


@client.event
async def on_message(message):
    n = 0
    # we do not want the bot to reply to itself
    #test webhook
    if message.author == client.user:
        return

    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}, digita !info per maggiori info sul bot'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('!info'):
        msg = "Bot di esempio sviluppato da algorithm-net\nhttps://algorithm-net.com"
        await message.channel.send(msg)
    elif message.content.startswith('!killyourself'):
        msg = '{0.author.mention} ucciditi'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('!repeat'):
        msg = '{0.author.mention} ha detto:'.format(message)
        msg2list = message.content.split(" ")
        msg2list.remove('!repeat')
        msg2 = ""
        for n in msg2list:
            msg2 += (n + " ")
        await message.channel.send(msg)
        await message.channel.send(msg2)
    elif message.content.startswith("!infinitechat"):
        while True:
            try:
                await message.channel.send("cioa")
            except KeyboardInterrupt:
                break
    elif message.content.startswith("!chatmode"):
        print("")
        while True:
            msg = input("messaggio...")
            if msg == "stop mode":
                print("Stop mode")
                print("return to normal")
                print("")
                break
            else:
                await message.channel.send(msg)
    elif message.content.startswith("!server info"):
        api = requests.get(
            "https://discord.com/api/guilds/755397488772382791/widget.json").json()
        channels = [thing["name"] for thing in api["channels"]]
        channel = ""
        for name in channels:
            n += 1
            channel += f'''canale{str(n)}: {str(name)}'''
            if n != len(channels):
                channel += "\n"
        servername = api["name"]
        members = ""
        for people in api["members"]:
            stat = ""
            if people["status"] == "dnd":
                stat = "Non disturbare"
            elif people["status"] == "online":
                stat = "Online"
            else:
                stat = "Sconosciuto"
            username = people["username"]
            members += f"{str(username)}: {str(stat)}\n"
        memb_on = api["presence_count"]

        msg = f'''
Nome server: {str(servername)}
{str(channel)}
membri online: {str(memb_on)}
{str(members)}
        '''

        n = 0
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
