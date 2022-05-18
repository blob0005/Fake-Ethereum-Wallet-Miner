testcatch = False
import time
import sys
import random

# module required
try:
    import colorama
except Exception:
    print("You are missing colorama")
    testcatch = True

import os

# Ran after exception
if testcatch:
    while True:
        fix = input("Install Colorama? (y/n): ")
        if fix == "y" or fix == "n":
            break
        else:
            print("Please enter a valid choice!")
    # if yes then
    if fix == "y":
        try:
            os.system("py -m pip install colorama")
        except Exception:
            print("There was an error whilst trying to download the module!")
            print("Please try to manually download or contact a developer for support.")
            exit()
        print("Module successfully installed!")
        print("Restart program.")
        input("")
        exit()
    # if no then
    if fix == "n":
        print("Alright!")
        print("Press 'Enter' to continue.")
        input("")
        exit()
colorama.init(autoreset=False)


def clr():
    _ = os.system("cls")
    return


def print00025(text):
    for c in text:
        sys.stdout.write(colorama.Fore.CYAN + c)
        sys.stdout.flush()
        time.sleep(0.0025)
    sys.stdout.write("\n")


def print0040(text):
    for c in text:
        sys.stdout.write(colorama.Fore.CYAN + c)
        sys.stdout.flush()
        time.sleep(0.040)
    sys.stdout.write("\n")


def miner():
    delay = 0.25
    delay2 = 3
    print00025("""
 _______  _______  _______    _     _  _______  ___      ___      _______  _______    __   __  ___   __    _  _______  ______   
|  _    ||       ||       |  | | _ | ||   _   ||   |    |   |    |       ||       |  |  |_|  ||   | |  |  | ||       ||    _ |  
| |_|   ||_     _||       |  | || || ||  |_|  ||   |    |   |    |    ___||_     _|  |       ||   | |   |_| ||    ___||   | ||  
|       |  |   |  |       |  |       ||       ||   |    |   |    |   |___   |   |    |       ||   | |       ||   |___ |   |_||_ 
|  _   |   |   |  |      _|  |       ||       ||   |___ |   |___ |    ___|  |   |    |       ||   | |  _    ||    ___||    __  |
| |_|   |  |   |  |     |_   |   _   ||   _   ||       ||       ||   |___   |   |    | ||_|| ||   | | | |   ||   |___ |   |  | |
|_______|  |___|  |_______|  |__| |__||__| |__||_______||_______||_______|  |___|    |_|   |_||___| |_|  |__||_______||___|  |_|

                                    # Check out the credits!""")
    print0040("Testing proxies...")
    time.sleep(delay)
    r1 = random.randint(20, 50)
    print0040("Starting " + str(r1) + " Server(s)")
    time.sleep(delay)
    print0040("Server(s) have started")
    time.sleep(delay)
    print0040("Pushing update to Server(s)")
    time.sleep(delay)
    print0040("Starting program...")
    time.sleep(3)
    choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
              "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    while True:
        for u in range(150):
            clr()
            print(colorama.Fore.RED + """
 _______  _______  _______    _     _  _______  ___      ___      _______  _______    __   __  ___   __    _  _______  ______   
|  _    ||       ||       |  | | _ | ||   _   ||   |    |   |    |       ||       |  |  |_|  ||   | |  |  | ||       ||    _ |  
| |_|   ||_     _||       |  | || || ||  |_|  ||   |    |   |    |    ___||_     _|  |       ||   | |   |_| ||    ___||   | ||  
|       |  |   |  |       |  |       ||       ||   |    |   |    |   |___   |   |    |       ||   | |       ||   |___ |   |_||_ 
|  _   |   |   |  |      _|  |       ||       ||   |___ |   |___ |    ___|  |   |    |       ||   | |  _    ||    ___||    __  |
| |_|   |  |   |  |     |_   |   _   ||   _   ||       ||       ||   |___   |   |    | ||_|| ||   | | | |   ||   |___ |   |  | |
|_______|  |___|  |_______|  |__| |__||__| |__||_______||_______||_______|  |___|    |_|   |_||___| |_|  |__||_______||___|  |_|

                                    # Check out the credits!""")
            rc = random.choices(choice, k=64)
            print(colorama.Fore.RED + "Generated Code - " + "".join(rc) + " - 0.00$")
            time.sleep(0.075)
        clr()
        r1 = random.randint(1644, 9856)
        rc = random.choices(choice, k=64)

        print(colorama.Fore.GREEN + """
 _______  _______  _______    _     _  _______  ___      ___      _______  _______    __   __  ___   __    _  _______  ______   
|  _    ||       ||       |  | | _ | ||   _   ||   |    |   |    |       ||       |  |  |_|  ||   | |  |  | ||       ||    _ |  
| |_|   ||_     _||       |  | || || ||  |_|  ||   |    |   |    |    ___||_     _|  |       ||   | |   |_| ||    ___||   | ||  
|       |  |   |  |       |  |       ||       ||   |    |   |    |   |___   |   |    |       ||   | |       ||   |___ |   |_||_ 
|  _   |   |   |  |      _|  |       ||       ||   |___ |   |___ |    ___|  |   |    |       ||   | |  _    ||    ___||    __  |
| |_|   |  |   |  |     |_   |   _   ||   _   ||       ||       ||   |___   |   |    | ||_|| ||   | | | |   ||   |___ |   |  | |
|_______|  |___|  |_______|  |__| |__||__| |__||_______||_______||_______|  |___|    |_|   |_||___| |_|  |__||_______||___|  |_|

                                    # Check out the credits!""")
        print(colorama.Fore.GREEN + "Generated Code - " + "".join(rc) + " - " + str(r1) + "$")
        time.sleep(1)
        print(colorama.Fore.GREEN + "We are sending money to your address!")
        time.sleep(1)
        print(colorama.Fore.GREEN + ":)")
        time.sleep(5)
        return


while True:
    print(colorama.Fore.CYAN + """
--------------------------------------
    Fake BTC Wallet Miner
--------------------------------------
    [1] Credits - Get Creators & Source Code
    
    [2] Change Wallet Address - Change your BTC Wallet Address
    
    [3] Crypto Wallet Miner - Mine some crypto wallets :)
--------------------------------------""")
    print(colorama.Fore.GREEN + "")
    main = input("> ")
    if main == "3":
        miner()
    if main == "1":
        print("Source Code: https://github.com/Xeify0/Wallet-Miner")
        print("Original Source Code: https://github.com/blob0005/Fake-Ethereum-Wallet-Miner")
        print("")
        print(colorama.Fore.GREEN + "Original program by: blob#0005")
        print(colorama.Fore.RED + "Fork created by: Xeify#9155 ")
        print("")
        input("")
    if main == "2":
        main = input("Please enter your wallet address: ")
            
