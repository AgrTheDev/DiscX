import requests
from colorama import *

def core_joinServer(token, invite):
    headers = {
        'authority': 'canary.discord.com',
        'content-length': '0',
        'accept-language': 'en-US',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.34 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
        'accept': '*/*',
        'origin': 'https://canary.discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://canary.discord.com/channels/^@me',
        'authorization': token
    }
    joinReq = requests.post(f'https://canary.discord.com/api/v9/invites/{invite}', headers=headers)
    
    if joinReq.status_code == 200 or joinReq.status_code == 201 or joinReq.status_code == 204:
        print(Fore.GREEN + f'[{joinReq.status_code}] Successfully joined server')
    elif joinReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    else:
        print(Fore.RED + f'[{joinReq.status_code}] Error')
    print(Fore.RESET, end="")

def main_joinServer(tokens):
    invite = input('Invite code (7-10 characters/vanity)\n>>> ')
    for x in range(len(tokens)):
        core_joinServer(tokens[x], invite)