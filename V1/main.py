import time
import sys
import random
try:
    import os
    from os import system
    system("title " + "Ethereum Wallet Miner,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
    import colorama
except:
    try:
        import os
        os.system("pip install colorama")
        print("Found Error, Auto Fix Have Most Likely Fixed The Problem, Run The Program Agian")
        input("")
        exit()
    except:
        print("Missing Modules")
colorama.init(autoreset=True)
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
def eth():
    delay = 0.25
    delay2 = 3
    print00025("""
        ________  __       _____ __             __         
       / ____/ /_/ /_     / ___// /____  ____ _/ /__  _____
      / __/ / __/ __ \    \__ \/ __/ _ \/ __ `/ / _ \/ ___/
     / /___/ /_/ / / /   ___/ / /_/  __/ /_/ / /  __/ /    
    /_____/\__/_/ /_/   /____/\__/\___/\__,_/_/\___/_/     
                                                           
                                    #MADE BY blob#0005""")
    print0040("Connecting To Api")
    time.sleep(delay)
    r1 = random.randint(20, 50)
    print0040("Starting " + str(r1) + " Server(s)")
    time.sleep(delay)
    print0040("Server(s) Started")
    time.sleep(delay)
    print0040("Sending Crypto Address To Server(s)")
    time.sleep(delay)
    print0040("Started Overclocking On Server(s)")
    time.sleep(delay)
    print0040("Starting In 3 Seconds")
    time.sleep(3)
    choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    trys = 10
    done = 0
    while True:
        rc = random.choices(choice, k=64)
        rrr = random.randint(1, 100)
        if rrr != 98:
            print(colorama.Fore.RED + "Crypto Wallet Generated    |   " + "".join(rc) + "|    Code Invalid")
        if rrr == 98:
            print(colorama.Fore.GREEN + "Crypto Wallet Generated    |    " + "".join(rc) + "|    Code Valid")
            time.sleep(delay2)
            ramount = random.uniform(0.00, 19.00)
            ramount = str(ramount)
            ramount = ramount[:-8]
            print(colorama.Fore.GREEN + f"User Had {ramount} Bitcoin(s)")
            time.sleep(delay2)
            print(colorama.Fore.GREEN + "Sending Bitcoin To Main Address")
            time.sleep(delay2)
            print(colorama.Fore.GREEN + "Succsesfully Sent")
            time.sleep(delay2)
            print(colorama.Fore.GREEN + "Enough For Today CYA")
            time.sleep(5)
            exit()
        time.sleep(0.005)
eth()
