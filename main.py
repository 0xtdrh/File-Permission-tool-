import colorama
from colorama import Back, Fore, Style
import os 

bannar = Fore.GREEN + """

 _____  ____  _        ___      ____   ___  ____   ___ ___  ____ _____ _____ ____  ___   ____      
|     ||    || |      /  _]    |    \ /  _]|    \ |   |   ||    / ___// ___/|    |/   \ |    \     
|   __| |  | | |     /  [_     |  o  )  [_ |  D  )| _   _ | |  (   \_(   \_  |  ||     ||  _  |    
|  |_   |  | | |___ |    _]    |   _/    _]|    / |  \_/  | |  |\__  |\__  | |  ||  O  ||  |  |    
|   _]  |  | |     ||   [_     |  | |   [_ |    \ |   |   | |  |/  \ |/  \ | |  ||     ||  |  |    
|  |    |  | |     ||     |    |  | |     ||  .  \|   |   | |  |\    |\    | |  ||     ||  |  |    
|__|   |____||_____||_____|    |__| |_____||__|\_||___|___||____|\___| \___||____|\___/ |__|__|    
                                                                                                   


"""
print (Fore.GREEN + bannar)


os.system("clear")
print (bannar)
b1 = int(input (Fore.WHITE + "Enter frist binary(read) number => "))
b2 = int(input (Fore.WHITE + "Enter second binary(write) number => "))
b3 = int(input (Fore.WHITE + "Enter third binary(execute) number => "))	
def op() : 
	global b1 
	global b2 
	global b3 
	b1 = b1 * 4 
	b2 = b2 * 2
	b3 = b3 * 1
	global total
	total = b1 + b2 + b3 
	
	print (f"Your permission number is {total} ")
	
op() 


# Copyright => Trojan 4x
