import requests
from colorama import *

def core_tokenChecker(token):
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
    tokenReq = requests.get(f'https://canary.discord.com/api/v9/users/@me', headers=headers)
    
    if tokenReq.status_code == 200 or tokenReq.status_code == 201 or tokenReq.status_code == 204:
        print(Fore.GREEN + f'[{tokenReq.status_code}] Valid token')
        open('output/checked_tokens.txt', 'a').write(f'{token} | Valid\n')
    elif tokenReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    elif tokenReq.status_code == 401:
        print(Fore.RED + '[401] Invalid token')
        open('output/checked_tokens.txt', 'a').write(f'{token} | Invalid\n')
    else:
        print(Fore.RED + f'[{tokenReq.status_code}] Error')
        open('output/checked_tokens.txt', 'a').write(f'{token} | Checking Error\n')
    print(Fore.RESET, end="")

def main_tokenChecker(tokens):
    for x in range(len(tokens)):
        core_tokenChecker(tokens[x])