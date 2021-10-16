import json
import requests
from colorama import *

def core_statusTextChanger(token, status):
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
    
    data = {"custom_status":{"text":status}}

    statusReq = requests.patch(f'https://canary.discord.com/api/v9/users/@me/settings', headers=headers, data=json.dumps(data))
    
    if statusReq.status_code == 200 or statusReq.status_code == 201 or statusReq.status_code == 204:
        print(Fore.GREEN + f'[{statusReq.status_code}] Successfully changed status')
    elif statusReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    else:
        print(Fore.RED + f'[{statusReq.status_code}] Error')
    print(Fore.RESET, end="")

def main_statusTextChanger(tokens):
    status = input('Account status\n>>> ')
    for x in range(len(tokens)):
        core_statusTextChanger(tokens[x], status)