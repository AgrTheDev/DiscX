import json
import requests
from colorama import *
import time

def core_massChannelDeleter(token, guildID):
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

    channelReq = requests.get(f'https://canary.discord.com/api/v9/guilds/{guildID}/channels', headers=headers)
    
    if channelReq.status_code == 200 or channelReq.status_code == 201 or channelReq.status_code == 204:
        print(Fore.GREEN + f'[{channelReq.status_code}] Successfully fetched channels')
    else:
        print(Fore.RED + f'[{channelReq.status_code}] Couldn\'t fetch channels... Exiting (4)')
        time.sleep(4)
        exit()
    print(Fore.RESET, end="")
    
    channelData = channelReq.json()
    
    for x in range(len(channelData)):
        channelDelReq = requests.delete(f'https://canary.discord.com/api/v9/channels/{channelData[x]["id"]}', headers=headers)
        if channelDelReq.status_code == 200 or channelDelReq.status_code == 201 or channelDelReq.status_code == 204:
            print(Fore.GREEN + f'[{channelDelReq.status_code}] Successfully deleted channel')
        elif channelDelReq.status_code == 304:
            print(Fore.YELLOW + '[304] Not modified')
        else:
            print(Fore.RED + f'[{channelDelReq.status_code}] Error')
        print(Fore.RESET, end="")

def main_massChannelDeleter(tokens):
    token = input('Your token (Requires MANAGE_CHANNELS permission in guild)\n>>> ')
    guildID = input('Guild ID\n>>> ')
    core_massChannelDeleter(token, guildID)