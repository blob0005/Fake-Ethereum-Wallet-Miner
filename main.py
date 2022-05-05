import time
import sys
import random
import colorama
import os
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
    while True:
        for u in range(150):
            clr()
            print(colorama.Fore.RED + """
        ________  __       _____ __             __         
       / ____/ /_/ /_     / ___// /____  ____ _/ /__  _____
      / __/ / __/ __ \    \__ \/ __/ _ \/ __ `/ / _ \/ ___/
     / /___/ /_/ / / /   ___/ / /_/  __/ /_/ / /  __/ /    
    /_____/\__/_/ /_/   /____/\__/\___/\__,_/_/\___/_/     
                                                           
                                    #MADE BY blob#0005""")
            rc = random.choices(choice, k=64)
            print(colorama.Fore.RED + "Generated Code - " + "".join(rc) + " - 0.00$")
            time.sleep(0.075)
        clr()
        r1 = random.randint(1644, 9856)
        rc = random.choices(choice, k=64)

        print(colorama.Fore.GREEN + """
        ________  __       _____ __             __         
       / ____/ /_/ /_     / ___// /____  ____ _/ /__  _____
      / __/ / __/ __ \    \__ \/ __/ _ \/ __ `/ / _ \/ ___/
     / /___/ /_/ / / /   ___/ / /_/  __/ /_/ / /  __/ /    
    /_____/\__/_/ /_/   /____/\__/\___/\__,_/_/\___/_/     
                                                           
                                    #MADE BY blob#0005""")
        print(colorama.Fore.GREEN + "Generated Code - " + "".join(rc) + " - " + str(r1) + "$")
        time.sleep(1)
        print(colorama.Fore.GREEN + "Sending Money To Main Address")
        time.sleep(1)
        print(colorama.Fore.GREEN + "Enough For Today, CYA")
        time.sleep(5)
        return
while True:
    print(colorama.Fore.CYAN + """
    1. Credits
    2. Change Address
    3. Etherium Stealer""")
    main = input("> ")
    if main == "3":
        eth()
    if main == "1":
        print("Program Was Fully Coded By blob#0005")
        input("")
    if main == "2":
        main = input("Enter Ur Crypto Address: ")
    
