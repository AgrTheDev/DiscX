import json
import requests
from colorama import *

def core_channelSpammer(token, channelID, msg):
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
    
    data = { "content": msg, "tts": False }
    
    spamReq = requests.post(f'https://canary.discord.com/api/v9/channels/{channelID}/messages', headers=headers, data=json.dumps(data))
    
    if spamReq.status_code == 200 or spamReq.status_code == 201 or spamReq.status_code == 204:
        print(Fore.GREEN + f'[{spamReq.status_code}] Successfully sent message')
    elif spamReq.status_code == 304:
        print(Fore.YELLOW + '[304] Not modified')
    else:
        print(Fore.RED + f'[{spamReq.status_code}] Error')
    print(Fore.RESET, end="")

def main_channelSpammer(tokens):
    print('Note: This will run forever, Ctrl-C to quit')
    channelID = input('Channel ID\n>>> ')
    msg = input('Spam message\n>>> ')
    while True:
        for x in range(len(tokens)):
            core_channelSpammer(tokens[x], channelID, msg)