from googlesearch import search
from rich import print
from time import sleep
from bs4 import BeautifulSoup
from rich.console import Console                                                                                                                                        
from rich.table import Table

import os
import sys
import requests

def googlesearch(vin):
	count = 0
	query = vin
	print(f"[blue]searching {vin}...[blue]")
	console = Console()
	table = Table()
	for url in search(query, num=20, stop=25, pause=5):
		req = requests.get(url)
		soup = BeautifulSoup(req.text, 'html.parser')
		title = soup.find('title').get_text()
		table.add_row(f"{title}", f"{url}")
		count += 1
		sleep(0.1)
	console.print(table)
	print(f"[bold white]found {count} results on {vin}[/bold white]")