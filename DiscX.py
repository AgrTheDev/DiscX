import requests, time
from colorama import *
from lib.core import *

init()

try:
    tokens = open('input/tokens.txt', 'r').read().splitlines()
except:
    print(Fore.RED + 'Paste your tokens into input/tokens.txt')
    time.sleep(3)
    quit()
    
if len(tokens) == 0:
    print(Fore.RED + 'Paste your tokens into input/tokens.txt')
    time.sleep(3)
    quit()

def main():
    logo = '''                                                                                  
                  .=-.-.  ,-,--.    _,.----.          ,-.--, 
      _,..---._  /==/_ /,-.'-  _\ .' .' -   \.--.-.  /=/, .' 
    /==/,   -  \|==|, |/==/_ ,_.'/==/  ,  ,-'\==\ -\/=/- /   
    |==|   _   _\==|  |\==\  \   |==|-   |  . \==\ `-' ,/    
    |==|  .=.   |==|- | \==\ -\  |==|_   `-' \ |==|,  - |    
    |==|,|   | -|==| ,| _\==\ ,\ |==|   _  , |/==/   ,   \   
    |==|  '='   /==|- |/==/\/ _ |\==\.       /==/, .--, - \  
    |==|-,   _`//==/. /\==\ - , / `-.`.___.-'\==\- \/=/ , /  
    `-.`.____.' `--`-`  `--`---'              `--`-'  `--`   

    '''
    options = '''
    [1]: Server Join Bot / [2]: Server Leave Bot / [3]: Status Text Changer
    [4]: Status Type Changer / [5]: Message Spammer
    '''
    print(Fore.BLUE + "Welcome to...")
    time.sleep(2)
    print(logo)
    time.sleep(1)
    print(Fore.GREEN + "~" * 75)
    print(options)
    print(Fore.GREEN + "~" * 75)
    print(Fore.RESET, end="")
    option = input('>>> ')
    features = [main_joinServer, main_leaveServer, main_statusTextChanger, main_statusTypeChanger, main_messageSpammer]
    cls()
    features[int(option) - 1](tokens)
    print(Fore.BLUE + "Finished the task! Returning to menu (4)" + Fore.RESET)
    time.sleep(4)
    cls()
    main()

main()