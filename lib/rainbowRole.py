import json, time
import requests
from colorama import *

def core_rainbowRole(token, guildID, roleID, color):
    
    headers = {
        'authority': 'canary.discord.com',
        'accept-language': 'en-US',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.34 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
        'accept': '*/*',
        'origin': 'https://canary.discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://canary.discord.com/channels/^@me',
        'content-type': 'application/json',
        'authorization': token
    }
    
    roleInfoReq = requests.get(f'https://canary.discord.com/api/v9/guilds/{guildID}', headers=headers)
    
    if roleInfoReq.status_code == 200 or roleInfoReq.status_code == 201 or roleInfoReq.status_code == 204:
        print(Fore.GREEN + f'[{roleInfoReq.status_code}] Successfully fetched roles')
    else:
        print(Fore.RED + f'[{roleInfoReq.status_code}] failed to fetch roles... Exiting (4)')
        time.sleep(4)
        exit()
    print(Fore.RESET, end="")
    
    roles = roleInfoReq.json()["roles"]
    currentRole = None
    
    for x in range(len(roles)):
        if roles[x]['id'] == roleID:
            currentRole = roles[x]
            
    if not currentRole:
        print(Fore.RED + 'Role not found... Exiting (4)' + Fore.RESET)
        time.sleep(4)
        exit()
    
    data = { "name":currentRole['name'],"permissions":currentRole['permissions'],"color":color,"hoist":currentRole['hoist'],"mentionable":currentRole['mentionable'],"icon":currentRole['icon'],"unicode_emoji":currentRole['unicode_emoji'] }
    
    roleReq = requests.patch(f'https://canary.discord.com/api/v9/guilds/{guildID}/roles/{roleID}', headers=headers, data=json.dumps(data))
    
    if roleReq.status_code == 200 or roleReq.status_code == 201 or roleReq.status_code == 204:
        print(Fore.GREEN + f'[{roleReq.status_code}] Successfully changed role color')
    elif roleReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    else:
        print(Fore.RED + f'[{roleReq.status_code}] Error')
    print(Fore.RESET, end="")

def main_rainbowRole(tokens):
    print('Note: This will run forever, Ctrl-C to quit')
    token = input('Your token (Requires MANAGE_ROLES permission in guild)\n>>> ')
    guildID = input('Guild ID\n>>> ')
    roleID = input('Role ID\n>>> ')
    colors = [16711680, 15158332, 15844367, 3066993, 3447003, 10181046]
    while True:
        for x in range(len(colors)):
            core_rainbowRole(token, guildID, roleID, colors[x])