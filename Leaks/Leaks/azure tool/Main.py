import requests, threading, os, random, time
from colored import fg, attr
from AuthGG import *
import colorama 
import sys
import ctypes
import subprocess

from colorama import Fore, init
from capmonster_python import RecaptchaV2Task
import json

with open('settings.json') as config_file:
    data = json.load(config_file)
    CAPMONSTER = data['CAPMONSTER']
    
done = 0
retries = 0
a = fg('#ff009ds')
b = attr('reset')
bypass = 0

cmd = 'mode 120,30'
os.system(cmd)

ctypes.windll.kernel32.SetConsoleTitleW("Boost Market | discord.gg/boostmarket")





def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

def Auth():
    print("[>] Username: ", end='')
    username = str(input())
    print()
    print("[>] Password: ", end='')
    password = str(input())
    print()
    if AuthGG.Login(username, password):
        print("[>] Login Successfull")
        time.sleep(.1)
        


if __name__ == "__main__":
    #pass
    Auth()

def title():
    global done, retries, bypass
    while True:
        os.system(f'')

def finger():
    r = requests.get('https://discordapp.com/api/v9/experiments')
    if r.status_code == 200:
        fingerprint = r.json()['fingerprint']
        return fingerprint
    else:
        print('sum went wrong')

def cookies():
    r = requests.get('https://discord.com')
    if r.status_code == 200:
        cookies = r.cookies.get_dict()
        nig = cookies['__dcfduid']
        nig2 = cookies['__sdcfduid']
        lmao  = f"__dcfduid={nig}; __sdcfduid={nig2}; locale=en-US"
        return lmao
    else:
        print('sum went wrong')


def leave(line, invite):
    global done

    try:
        token = line.strip()

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me', 
            'sec-fetch-dest': 'empty', 
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
        }
        cookies = {
        '__cfruid': '5116972237e242dde168855bf5d88a6f49ec7a25-1636780527',
        '__stripe_mid': '448cbdac-228d-4521-8717-6055f8e7201b87c90c',
        '__dcfduid': '5ac867e0042f11ec84f201b16fed194d',
        }

        r = requests.delete(f'https://ptb.discord.com/api/v9/users/@me/guilds/{invite}', headers=headers, json={}, cookies=cookies)
        if r.status_code == 204:
            print(f'\n                               Unboosted ; {guidi}')
            done += 1
        else:
            print(r.text)

    except Exception as e:
        print(e)

def boost(line, invite):
    global done

    try:
        token = line.strip()

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me', 
            'sec-fetch-dest': 'empty', 
            'sec-fetch-mode': 'cors',
            'cookie': '__dcfduid=23a63d20476c11ec9811c1e6024b99d9; __sdcfduid=23a63d21476c11ec9811c1e6024b99d9e7175a1ac31a8c5e4152455c5056eff033528243e185c5a85202515edb6d57b0; locale=en-GB',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'te': 'trailers',
        }
        r = requests.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        print(f"\n                               Token Has No Boosts ; {token[:40]}")
        if r.status_code == 200:
            slots = r.json()
            if len(slots) != 0:
                guid = None
                joined = False
                headers["content-type"] = 'application/json'
                for i in range(15):
                    try:
                        join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                        })
                        print("\n                               ERROR | "+join_server.text)
                        if "captcha_sitekey" in join_server.text:
                            createTask = requests.post("https://api.capmonster.cloud/createTask", json={
                                "clientKey": CAPMONSTER,
                                "task": {
                                    "type": "HCaptchaTaskProxyless",
                                    "websiteURL": "https://discord.com/channels/@me",
                                    "websiteKey": join_server.json()['captcha_sitekey']
                                }
                            }).json()["taskId"]
                            print("CAPTCHA TASK ID: "+createTask)
                            getResults = {}
                            getResults["status"] = "processing"
                            while getResults["status"] == "processing":
                                getResults = requests.post("https://api.capmonster.cloud/getTaskResult", json={
                                    "clientKey": CAPMONSTER,
                                    "taskId": createTask
                                }).json()

                                time.sleep(1)

                            solution = getResults["solution"]["gRecaptchaResponse"]

                            print(f"\n                               Captcha Solved")

                            join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                                "captcha_key": solution
                            })

                        if join_server.status_code == 200:
                            join_outcome = True
                            guid = join_server.json()["guild"]["id"]
                            print("\n                               Joined Server")
                            break
                        else: 
                            print("\n                               Couldn't join server: "+str(join_server.json()))
                            return
                    except Exception as e:
                        print(e)
                        pass
            for slot in slots:
                slotid = slot['id']
                payload = {"user_premium_guild_subscription_slot_ids": [slotid]}
                r2 = requests.put(f'https://discord.com/api/v9/guilds/{guid}/premium/subscriptions', headers=headers, json=payload)
                if r2.status_code == 201:
                    print(f'\n                               Boosted ; {token[:40]}')
                    done += 1
                else:
                    print(r2.json())
        else:
            print(r.json())

    except Exception as e:
        retries += 1

tokensAmount = len(open('data/tokens.txt', encoding='utf-8').read().splitlines())

banner2 = f"""{Fore.WHITE}                                   
        █████╗ ███████╗██╗   ██╗██████╗ ███████╗    ███████╗███████╗██████╗ ██╗   ██╗██╗ ██████╗███████╗███████╗
       ██╔══██╗╚══███╔╝██║   ██║██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██╔════╝██╔════╝
       ███████║  ███╔╝ ██║   ██║██████╔╝█████╗      ███████╗█████╗  ██████╔╝██║   ██║██║██║     █████╗  ███████╗
       ██╔══██║ ███╔╝  ██║   ██║██╔══██╗██╔══╝      ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██║     ██╔══╝  ╚════██║
       ██║  ██║███████╗╚██████╔╝██║  ██║███████╗    ███████║███████╗██║  ██║ ╚████╔╝ ██║╚██████╗███████╗███████║
       ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝╚══════╝                                                                                                    
                                               discord.gg/boostmarket                                                                                   
                                       ╔════════════════════════════════════════╗
                                       ║ 1. Boost         ║  4. Token Checker   ║
                                       ║ 2. Unboost       ║  5. Reload Stock    ║
                                       ║ 3. Check Stock   ║  6. Setup           ║
                                       ╚════════════════════════════════════════╝
"""

threading.Thread(target=title).start()

def menu():
    global done
    while True:
        option = input(f'\n                                                   Option ; ')
        if option == "1":
            inv = input(f'                                                   Invite ; ')
            amount = int(input("                                                   Boosts ; "))
            with open('data/tokens.txt', 'r') as f:
                for line in f.readlines():
                    try:
                        boost(line, inv)
                    except Exception as e:
                        print(e)
                        pass
                    if done >= amount:
                        print(f"\n                                            Boosted {inv} {amount}x")
                        done = 0
                        break
            time.sleep(20)
            os.system('cls')
            print(banner2)
            done = 0
        if option == "2":
            invite = input(f'                                                 Guild ID ; ')
            threads = int("8")
            with open('data/tokens.txt', 'r') as f:
                for line in f.readlines():
                    run = True
                    while run:
                        if threading.active_count() <= threads:
                            threading.Thread(target = leave, args = (line,invite,)).start()
                            run = False
            time.sleep(2)
            os.system('cls')
            print(banner2)
            completed = 0

        if option == "3":
            invite = input(f'\n                                                 {tokensAmount * 2} Boosts Ready')
            time.sleep(2)
            os.system('cls')
            print(banner2)
            done = 0

def nigganigga123():
    print()



if __name__ == '__main__':
    nigganigga123()
    os.system('cls')
    print(banner2)
    menu()