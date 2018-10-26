
import discord
import math
import os

client = discord.Client()

# Constant
DISCORDTOKEN = "NTA0NjMzOTMxMDQwMDMwNzIx.DrQpTw.T_iMHx1qHcd8InhUdxfmDMuT4hQ"

FORTNITE_API_KEY = '8a550d1d-d800-4b71-87b3-1281b9efc8f2'

LISTE = ['Common', 'Uncommon', 'Rare', 'Epic', 'Master', 'Legendary', 'Grandmaster', 'Demigod', 'God', 'Hacker', 'Pro']
COMMON_B = 0.00
COMMON_E = 0.49
UNCOMMON_B = 0.50
UNCOMMON_E = 0.99
RARE_B = 1.00
RARE_E = 1.49
EPIC_B = 1.50
EPIC_E = 1.99
MASTER_B = 2.00
MASTER_E = 2.99
LEGENDARY_B = 3.00
LEGENDARY_E = 3.49
GRANDMASTER_B = 3.50
GRANDMASTER_E = 3.99
DEMIGOD_B = 4.00
DEMIGOD_E = 4.99
GOD_B = 5.00
GOD_E = 5.99
HACKER_B = 6.00
HACKER_E = 7.99
PRO_B = 8.00
PRO_E = 100

# Return the overall K/D of the fortnite player pass in parameter
def get_ratio(username):
    print(username)
    link = 'https://api.fortnitetracker.com/v1/profile/pc/' + username
    response = requests.get(link, headers={'TRN-Api-Key': FORTNITE_API_KEY})
    if response.status_code == 200:
        collection = response.json()
        if 'error' in collection:
            return "-1"
        else:
            for data_item in collection['lifeTimeStats']:
                if data_item['key'] == 'K/d':
                    ratio = data_item['value']
                    return ratio
        print("Invalid username")
        return "-1"
    else:
        print("Error recovering fortnite data")
        return "-2"

def print_nextLvl(begin, end, ratio):
    rang = end - begin 
    if ratio >= rang * 0.00 + begin and ratio <= rang * 0.059999 + begin:
        return '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.06 + begin and ratio <= rang * 0.109999 + begin:
        return '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.11 + begin and ratio <= rang * 0.159999 + begin:
        return '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.16 + begin and ratio <= rang * 0.209999 + begin:
        return '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.21 + begin and ratio <= rang * 0.259999 + begin:
        return '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.26 + begin and ratio <= rang * 0.309999 + begin:
        return '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.31 + begin and ratio <= rang * 0.359999 + begin:
        return '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.36 + begin and ratio <= rang * 0.409999 + begin:
        return '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.41 + begin and ratio <= rang * 0.459999 + begin:
        return '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.46 + begin and ratio <= rang * 0.509999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.51 + begin and ratio <= rang * 0.559999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.56 + begin and ratio <= rang * 0.609999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.61 + begin and ratio <= rang * 0.659999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.66 + begin and ratio <= rang * 0.709999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.71 + begin and ratio <= rang * 0.759999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]'
    elif ratio >= rang * 0.76 + begin and ratio <= rang * 0.809999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]'
    elif ratio >= rang * 0.81 + begin and ratio <= rang * 0.859999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]'
    elif ratio >= rang * 0.86 + begin and ratio <= rang * 0.909999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□]'
    elif ratio >= rang * 0.91 + begin and ratio <= rang * 0.959999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]'
    elif ratio >= rang * 0.96 + begin and ratio <= rang * 1.00 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]'

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # The command /patch return a link withvthe lastest patch note
    if message.content.startswith('/patch'):
        await client.send_message(message.channel, 'Last patchnotes: https://www.epicgames.com/fortnite/en/news')
    # The command /rank return attribute a rank according to the K/D of the user
    if message.content.startswith("/rank"):
        for list in LISTE:
            roles = discord.utils.get(message.server.roles, name=list)
            await client.remove_roles(message.author, roles)
        username = '{0.author.display_name}'.format(message)
        ratio = float(get_ratio(username))
        print(ratio)
        if ratio >= COMMON_B and ratio <= COMMON_E:
            role = discord.utils.get(message.server.roles, name=LISTE[0])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(UNCOMMON_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(COMMON_B, COMMON_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= UNCOMMON_B and ratio <= UNCOMMON_E:
            role = discord.utils.get(message.server.roles, name=LISTE[1])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(RARE_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(UNCOMMON_B, UNCOMMON_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= RARE_B and ratio <= RARE_E:
            role = discord.utils.get(message.server.roles, name=LISTE[2])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(EPIC_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(RARE_B, RARE_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= EPIC_B and ratio <= EPIC_E:
            role = discord.utils.get(message.server.roles, name=LISTE[3])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(MASTER_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(EPIC_B, EPIC_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= MASTER_B and ratio <= MASTER_E:
            role = discord.utils.get(message.server.roles, name=LISTE[4])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(LEGENDARY_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(MASTER_B, MASTER_E, ratio))
            await client.add_roles(message.author, role)  
        elif ratio >= LEGENDARY_B and ratio <= LEGENDARY_E:
            role = discord.utils.get(message.server.roles, name=LISTE[5])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(GRANDMASTER_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(LEGENDARY_B, LEGENDARY_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= GRANDMASTER_B and ratio <= GRANDMASTER_E:
            role = discord.utils.get(message.server.roles, name=LISTE[6])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(DEMIGOD_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(GRANDMASTER_B, GRANDMASTER_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= DEMIGOD_B and ratio <= DEMIGOD_E:
            role = discord.utils.get(message.server.roles, name=LISTE[7])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(GOD_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(DEMIGOD_B, DEMIGOD_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= GOD_B and ratio <= GOD_E:
            role = discord.utils.get(message.server.roles, name=LISTE[8])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(HACKER_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(GOD_B, GOD_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= HACKER_B and ratio <= HACKER_E:
            role = discord.utils.get(message.server.roles, name=LISTE[9])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(PRO_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(HACKER_B, HACKER_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= PRO_B:
            role = discord.utils.get(message.server.roles, name=LISTE[10])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Your ratio: " + str(ratio) + " K/D \n Max level! ¯\_(ツ)_/¯ "
            await client.send_message(message.channel, msgRatio)
            await client.add_roles(message.author, role) 
        elif ratio == -1:
            msg = "Your discord name is not a fortnite username! Use the command ```/nick YOUR_FORTNITE_USERNAME``` first!".format(message)
            await client.send_message(message.channel, msg)
        elif ratio == -2:
            msg = "The fortnite servers are offline. Try again later!".format(message)
            await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

token = os.environ.get("DISCORDTOKEN")
client.run(token)

