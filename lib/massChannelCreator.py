import json
import requests
from colorama import *

def core_massChannelCreator(token, guildID, channelName):
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
    
    data = {"type":0,"name":channelName,"permission_overwrites":[]}

    channelReq = requests.post(f'https://canary.discord.com/api/v9/guilds/{guildID}/channels', headers=headers, data=json.dumps(data))
    
    if channelReq.status_code == 200 or channelReq.status_code == 201 or channelReq.status_code == 204:
        print(Fore.GREEN + f'[{channelReq.status_code}] Successfully created channel')
    elif channelReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    else:
        print(Fore.RED + f'[{channelReq.status_code}] Error')
    print(Fore.RESET, end="")

def main_massChannelCreator(tokens):
    print('Note: This will run forever, Ctrl-C to quit')
    token = input('Your token (Requires MANAGE_CHANNELS permission in guild)\n>>> ')
    guildID = input('Guild ID\n>>> ')
    channelName = input('Channel name\n>>> ')
    while True:
        core_massChannelCreator(token, guildID, channelName)