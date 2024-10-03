# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import requests
    import time
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Status Changer")

try:
    Slow(discord_banner)
    token = Choice1TokenDiscord()
    try:
        statue_number = int(input(f"{color.RED}{INPUT} How many statues do you want to cycle (max 4) -> {color.RESET}"))
    except:
        ErrorNumber()

    statues = []

    headers = {'Authorization': token, 'Content-Type': 'application/json'}

    if statue_number >= 1 and statue_number <= 4:
        for loop in range(0, statue_number):
            choice = str(input(f"{color.RED}{INPUT} Custom Status {loop+1} -> {color.RESET}"))
            statues.append(choice)
    else:
        ErrorNumber()

    while True:
        for i in range(len(statues)):
            CustomStatus = {"custom_status": {"text": statues[i]}}
            try:
                r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{statues[i]}{color.RED}")
                i += 1
                time.sleep(5)
            except Exception as e:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{statues[i]}{color.RED}")
                time.sleep(5)
except Exception as e:
    Error(e)