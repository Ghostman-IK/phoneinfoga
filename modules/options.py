from modules import short_numbers,scanners,banner
import os,sys
from rich.table import Table
from rich.console import Console
from colorama import Fore
def options():
    os.system("clear")
    banner.banner()
    table=Table()
    console=Console()
    table.add_column("Options",style='yellow')
    table.add_column("Description",style='magenta')
    table.add_row("Scan","Get a Phone number information offline")
    table.add_row("Masscan","Get Mutiple Phone number information ")
    table.add_row("SOS","Short Numbers Utility Option")
    table.add_row("Clear","Clear Screen")
    table.add_row("Exit","Exit Phone Infoga Tool")
    console.print(table)
    choice=input(f"{Fore.YELLOW}Enter an option and continue: {Fore.RESET}")
    if str(choice)=='Scan' or str(choice)=='scan':
        print(f"{Fore.GREEN}=================================================================================={Fore.RESET}")
        number=input(f"{Fore.YELLOW}Enter a target phone number with country code: {Fore.RESET}")
        return scanners.get_phone_info(number)
    elif str(choice)=='Masscan' or str(choice)=='masscan':
        print(f"{Fore.GREEN}=================================================================================={Fore.RESET}")
        num_list=input(f"{Fore.YELLOW}Enter path to per line list of targets numbers: {Fore.RESET}")
        return scanners.masscan(num_list)
    elif str(choice)=='SOS' or str(choice)=='sos':
        os.system("clear")
        banner.banner()
        return short_numbers.short_numbers_menu()
    elif str(choice)=='Clear' or str(choice)=='clear':
        os.system("clear")
        banner.banner()
        return options.options()
    elif str(choice)=='Exit' or str(choice)=='exit':
        os.system("clear")
        banner.banner()
        sys.exit()
    else:
        print(f"{Fore.RED}Invalid option !...{Fore.RESET}")
        return options.options()
def continue_exit():
    table=Table()
    console=Console()
    table.add_column("Options",style='yellow')
    table.add_column("Descriptions",style='magenta')
    table.add_row("Contine","Continue scanning another Phone number")
    table.add_row("Clear","clear Screen")
    table.add_row("Exit","Exit Phone Infoga Tool")
    table.add_row("Back","Return to tool's main menu")
    console.print(table)
    ch=input(f"{Fore.YELLOW}Enter an option and continue: {Fore.RESET}")
    if str(ch)=="Continue" or str(ch)=='continue':
        os.system("clear")
        banner.banner()
        print(f"{Fore.GREEN}=================================================================================={Fore.RESET}")
        number=input(f"{Fore.YELLOW}Enter a target phone number with country code: {Fore.RESET}")
        return scanners.get_phone_info(number)
    if str(ch)=="Clear" or str(ch)=='clear':
        os.system("clear")
        banner.banner()
        return continue_exit()
    if str(ch)=="Exit" or str(ch)=="exit":
        os.system("clear")
        banner.banner()
        sys.exit()
    if str(ch)=='Back' or str(ch)=='back':
        return options()
    else:
        print(f"{Fore.RED}Invalid option !.{Fore.RESET}")
        os.system("clear")
        banner.banner()
        return continue_exit()
