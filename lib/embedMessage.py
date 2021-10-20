import json
import requests
from colorama import *

def core_embedMessage(token, channelID, embedTitle, embedDesc):
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
    
    data = { "content": None, "embeds": [ { "title": embedTitle, "description": embedDesc, "color": None } ] }
    
    embedReq = requests.post(f'https://canary.discord.com/api/v9/channels/{channelID}/messages', headers=headers, data=json.dumps(data))
    
    if embedReq.status_code == 200 or embedReq.status_code == 201 or embedReq.status_code == 204:
        print(Fore.GREEN + f'[{embedReq.status_code}] Successfully sent message')
    elif embedReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    else:
        print(Fore.RED + f'[{embedReq.status_code}] Error')
    print(Fore.RESET, end="")

def main_embedMessage(tokens):
    token = input('Your token (Requires MANAGE_CHANNELS permission in guild)\n>>> ')
    channelID = input('Channel ID\n>>> ')
    embedTitle = input('Embed title\n>>> ')
    embedDesc = input('Embed description\n>>> ')
    core_embedMessage(token, channelID, embedTitle, embedDesc)