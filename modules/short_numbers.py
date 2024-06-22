from modules import options
from modules import banner
import phonenumbers
from phonenumbers import shortnumberinfo
from rich.console import Console
from rich.table import Table
from colorama import Fore
import os,sys
def short_numbers_menu():
    console=Console()
    table=Table()
    table.add_column("Options",style='yellow')
    table.add_column("Descriptions",style='magenta')
    table.add_row("1.Check single short number","Specific short number availibity for a region")
    table.add_row("2.Bruteforce mode","Find short numbers for a region using a list of numbers")
    table.add_row("3.Clear","clear screen")
    table.add_row("4.Back","Return to tool's main menu")
    table.add_row("0.Exit","Exit Phone Infoga tool")
    console.print(table)
    print(f"{Fore.GREEN}================================================{Fore.RESET}")
    op=input(f"{Fore.YELLOW}Enter an options and continue: {Fore.RESET}")
    if str(op)=='1':
        print(f"{Fore.GREEN}=================================================================================={Fore.RESET}")
        number=input(f"{Fore.YELLOW}Enter a short number: {Fore.RESET}")
        print(f"{Fore.GREEN}=================================================================================={Fore.RESET}")
        region_code=input(f"{Fore.YELLOW}Enter a target region code: {Fore.RESET}")
        return s_short_num(number,region_code)
    elif str(op)=='2':
        print(f"{Fore.GREEN}=================================================================================={Fore.RESET}")
        region_code=input(f"{Fore.YELLOW}Enter a target region code: {Fore.RESET}")
        print(f"{Fore.GREEN}=================================================================================={Fore.RESET}")
        dic=input(f"{Fore.YELLOW}Enter path to per line numbers list: {Fore.RESET}")
        return short_numbers(region_code,dic)
    elif str(op)=='3' or str(op)=='clear':
        os.system("clear")
        banner.banner()
        return short_numbers_menu()
    elif str(op)=='4' or str(op)=='back':
        os.system("clear")
        return options.options()
    elif str(op)=='0' or str(op)=='exit':
        sys.exit()
    else:
        print(f"{Fore.RED}Invalid option !...{Fore.RESET}")
        return short_numbers_menu()
def short_menu_op():
    table=Table()
    console=Console()
    table.add_column("Options",style='yellow')
    table.add_column("Descriptions",style='magenta')
    table.add_row("1.Continue","Continue in Short Numbers Utility")
    table.add_row("2.Clear","clear screen")
    table.add_row("3.Back","Return to tool's main menu")
    table.add_row("0.Exit","Exit Phone Infoga tool")
    console.print(table)
    s=input(f"{Fore.YELLOW}Enter an option and continue: {Fore.RESET}")
    if str(s)=='1' or str(s)=='continue':
        return short_numbers_menu()
    elif str(s)=='2' or str(s)=='clear':
        os.system("clear")
        return short_menu_op()
    elif str(s)=='3' or str(s)=='back':
        return options.options()
    elif str(s)=='0' or str(s)=='exit':
        sys.exit()
    else:
        print(f"{Fore.RED}Invalid options !...{Fore.RESET}")
        return short_menu_op()
def short_numbers_result_s():
    table=Table()
    console=Console()
    table.add_column("SHORT NUMBERS FOUND ==> USING BRUTEFORCE MODE ")
    console.print(table)
def short_numbers_result_b():
    table=Table()
    console=Console()
    table.add_column("SHORT NUMBER AVAILIBILTY RESULT ==> SPECIFIC SHORT NUMBER FOR REGION  ")
    console.print(table)
def s_short_num(number,region_code):
    os.system("clear")
    print(f"{Fore.GREEN}================================================{Fore.RESET}")
    country_code=phonenumbers.country_code_for_region(region_code)
    #dic=input(f"{Fore.YELLOW}Enter path to per line short numbers list: {Fore.RESET}")
    phone=phonenumbers.parse("+"+str(country_code)+number,"en")
    rs=shortnumberinfo.is_valid_short_number_for_region(phone,str(region_code))
    if str(rs)=='True' or str(rs)=='true':
        sc=(str(shortnumberinfo.is_sms_service_for_region(phone,str(region_code))))
        os.system("clear")
        short_numbers_result_b()
        table=Table()
        console=Console()
        table.add_column("Region code",style='blue')
        table.add_column("Short Number",style='magenta')
        table.add_column("Valid for region ",style='yellow')
        table.add_column("Possible SMS Service",style='red')
        table.add_row(region_code,number,str(rs),str(sc))
        console.print(table)
    short_menu_op()

def short_numbers(region_code,dic):
    os.system("clear")
    short_numbers_result_s()
    print(f"{Fore.GREEN}================================================{Fore.RESET}")
    #region_code=input(f"{Fore.YELLOW}Enter a target region code: ")
    country_code=phonenumbers.country_code_for_region(region_code)
    #dic=input(f"{Fore.YELLOW}Enter path to per line short numbers list: {Fore.RESET}")
    f=open(dic).read().splitlines()
    for line in f:
        phone=phonenumbers.parse("+"+str(country_code)+line,"en")
        rs=shortnumberinfo.is_valid_short_number_for_region(phone,str(region_code))
        if str(rs)=='True' or str(rs)=='true':
            sc=(str(shortnumberinfo.is_sms_service_for_region(phone,str(region_code))))
            table=Table()
            console=Console()
            table.add_column("Region code",style='blue')
            table.add_column("Short Number",style='magenta')
            table.add_column("Valid for region ",style='yellow')
            table.add_column("Possible SMS Service",style='red')
            table.add_row(region_code,line,str(rs),str(sc))
            console.print(table)
    short_menu_op()
