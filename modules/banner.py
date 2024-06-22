from rich.table import Table
from rich.console import Console
table,console=Table(),Console()
def banner():
    table=Table()
    console=Console()
    table.add_column("Tool",style='red')
    table.add_column("Description",style='cyan')
    table.add_column("Author",style='yellow')
    table.add_column("Version",style='blue')
    table.add_row('Phone Inoga','Phone Number Information Gathering Tool','Ghostman','1.0')
    console.print(table)