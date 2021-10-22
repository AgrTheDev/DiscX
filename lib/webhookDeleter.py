import json
import requests
from colorama import *

def core_webhookDeleter(webHook):
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
    }
    
    deleteReq = requests.delete(webHook, headers=headers)
    
    if deleteReq.status_code == 200 or deleteReq.status_code == 201 or deleteReq.status_code == 204:
        print(Fore.GREEN + f'[{deleteReq.status_code}] Successfully deleted webhook')
    elif deleteReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    else:
        print(Fore.RED + f'[{deleteReq.status_code}] Error')
    print(Fore.RESET, end="")

def main_webhookDeleter(tokens):
    webHook = input('Webhook URL\n>>> ')
    core_webhookDeleter(webHook)