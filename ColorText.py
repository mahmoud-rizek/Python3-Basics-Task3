import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)



while True:
    uText = input("Enter the texe: ")
    uStyle = int(input('''
We have 3 style:
    1. text:RED       Background:yellow     style:DIM
    2. text:YELLWO    Background:BLUE       style:NORMAL
    3. text:BLUE      Background:RED        style:BRIGHT

Enter your style: 
'''))
    if uStyle in (1,2,3):
        if uStyle == 1:
            print(f"{Fore.BLUE}{Back.YELLOW}{Style.DIM}{uText}")
            
        elif uStyle == 2:
            print(f"{Fore.RED}{Back.BLUE}{Style.NORMAL}{uText}")
            
        elif uStyle == 3 :
            print(f"{Fore.YELLOW}{Back.RED}{Style.BRIGHT}{uText}")
            
        else:
            print("Wrong choice! ")
    else:
        print("Wrong choice! ")
    
        