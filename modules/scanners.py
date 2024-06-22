from modules import options
from modules import Functions
from modules import banner
from rich.table import Table
from rich.console import Console
from colorama import Fore
import os
def result_msg():
    table=Table()
    console=Console()
    table.add_column("TARGET PHONE NUMBER INFORMATIONS ==> OFFLINE INFORMATIONS  ")
    console.print(table)
def mass_result_msg():
    table=Table()
    console=Console()
    table.add_column("TARGETS PHONES NUMBERS INFORMATIONS ==> OFFLINE INFORMATIONS  ")
    console.print(table)
def get_phone_info(number):
    try:
        os.system("clear")
        banner.banner()
        os.system("clear")
        table=Table()
        console=Console()
        car=str(Functions.Info.get_carrier(number))
        con=str(Functions.Info.get_country(number))
        tz=str(Functions.Info.get_time_zone(number))
        rg=str(Functions.Info.get_region_code(number))
        vld=str(Functions.Info.check_number(number))
        result_msg()
        table.add_column("Phone Number",style='red')
        table.add_column("Operator",style="magenta")
        table.add_column("Country Name",style="green")
        table.add_column("Timezone",style='blue')
        table.add_column("Region Code",style='yellow')
        table.add_column("Validity Status",style='red')
        table.add_row(number,car,con,tz,rg,vld)
        console.print(table)
        options.continue_exit()
    except KeyboardInterrupt:
        print(f"{Fore.RED} Keyboard Interruption detcted !{Fore.RESET}")
        return options.options()
def masscan(num_list):
    try:
        os.system("clear")
        banner.banner()
        os.system("clear")
        mass_result_msg()
        f=open(num_list).read().splitlines()
        for number in f:
            table=Table()
            console=Console()
            car=str(Functions.Info.get_carrier(number))
            con=str(Functions.Info.get_country(number))
            tz=str(Functions.Info.get_time_zone(number))
            rg=str(Functions.Info.get_region_code(number))
            vld=str(Functions.Info.check_number(number))
            table.add_column("Phone Number",style='red')
            table.add_column("Operator",style="magenta")
            table.add_column("Country Name",style="green")
            table.add_column("Timezone",style='blue')
            table.add_column("Region Code",style='yellow')
            table.add_column("Validity Status",style='red')
            table.add_row(number,car,con,tz,rg,vld)
            console.print(table)
        options.continue_exit()
    except KeyboardInterrupt:
        print(f"{Fore.RED} Keyboard Interruption detcted !{Fore.RESET}")
        return options.options()
