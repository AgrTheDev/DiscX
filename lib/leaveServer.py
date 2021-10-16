import requests
from colorama import *

def core_leaveServer(token, serverID):
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
        'authorization': token
    }

    leaveReq = requests.delete(f'https://canary.discord.com/api/v9/users/@me/guilds/{serverID}', headers=headers)
    
    if leaveReq.status_code == 200 or leaveReq.status_code == 201 or leaveReq.status_code == 204:
        print(Fore.GREEN + f'[{leaveReq.status_code}] Successfully left server')
    elif leaveReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    else:
        print(Fore.RED + f'[{leaveReq.status_code}] Error')
    print(Fore.RESET, end="")

def main_leaveServer(tokens):
    invite = input('Server ID (17-18 digits)\n>>> ')
    for x in range(len(tokens)):
        core_leaveServer(tokens[x], invite)