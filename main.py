import colorama, time, random
colorama.init(autoreset=True)
delay = 0.5
def eth():
	print(colorama.Fore.CYAN + """
	    ________  __       _____ __             __         
	   / ____/ /_/ /_     / ___// /____  ____ _/ /__  _____
	  / __/ / __/ __ \    \__ \/ __/ _ \/ __ `/ / _ \/ ___/
	 / /___/ /_/ / / /   ___/ / /_/  __/ /_/ / /  __/ /    
	/_____/\__/_/ /_/   /____/\__/\___/\__,_/_/\___/_/     
	                                                       
									#MADE BY blob#0005""")
	print(colorama.Fore.CYAN + "LOADING | 10%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 20%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 30%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 40%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 50%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 60%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 70%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 80%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 90%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 100%")
	time.sleep(delay)
	print(colorama.Fore.GREEN + "CRACKING API DONE")
	time.sleep(delay)
	choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	while True:
		r1 = random.choices(choice, k=128)
		r2 = random.randint(1000, 10000)
		r3 = random.randrange(1, 17)
		r2 = str(r2)
		if "345763" not in r2:
			print(colorama.Fore.RED + "Private Key Invalid | " + "".join(r1) + " |")
		if "345763" in r2:
			print(colorama.Fore.GREEN + "\n\n\nPrivate Key Valid | " + "".join(r1) + f" | {r3} Etherium In Account")
			time.sleep(5)
			print(colorama.Fore.GREEN + "Etherium Being Sent...")
			time.sleep(5)
			print(colorama.Fore.GREEN + f"Etherium Succsesfully Sent To Main Address ({r3} Etherium Was Sent)")
			time.sleep(5)
		time.sleep(0.01)
def btc():
	print(colorama.Fore.CYAN + """
    ____  __          _____ __             __         
   / __ )/ /______   / ___// /____  ____ _/ /__  _____
  / __  / __/ ___/   \__ \/ __/ _ \/ __ `/ / _ \/ ___/
 / /_/ / /_/ /__    ___/ / /_/  __/ /_/ / /  __/ /    
/_____/\__/\___/   /____/\__/\___/\__,_/_/\___/_/     
                                                      
									#MADE BY blob#0005""")
	print(colorama.Fore.CYAN + "LOADING | 10%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 20%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 30%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 40%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 50%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 60%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 70%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 80%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 90%")
	time.sleep(delay)
	print(colorama.Fore.CYAN + "LOADING | 100%")
	time.sleep(delay)
	print(colorama.Fore.GREEN + "CRACKING API DONE")
	time.sleep(delay)
	choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	while True:
		r1 = random.choices(choice, k=128)
		r2 = random.randint(1000, 10000)
		r3 = random.randrange(1, 17)
		r2 = str(r2)
		if "345763" not in r2:
			print(colorama.Fore.RED + "Private Key Invalid | " + "".join(r1) + " |")
		if "345763" in r2:
			print(colorama.Fore.GREEN + "\n\n\nPrivate Key Valid | " + "".join(r1) + f" | {r3} Bitcoin(s) In Account")
			time.sleep(5)
			print(colorama.Fore.GREEN + "Bitcoin(s) Being Sent...")
			time.sleep(5)
			print(colorama.Fore.GREEN + f"Bitcoin Succsesfully Sent To Main Address ({r3} Etherium Was Sent)")
			time.sleep(5)
		time.sleep(0.01)
		
print("""Pick One
1. Etherium Stealer
2. Bitcoin Stealer""")
while True:
	main = input("> ")
	if main == "1" or main == "2":
		break
	else:
		print("Enter A Valid Choice")
if main == "1":
	eth()
if main == "2":
	btc()
