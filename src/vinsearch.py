import requests
import json
import os
import sys

from rich import print
from time import sleep
from rich.console import Console                                                                                                                                        
from rich.table import Table

def vindecode(vin):
	print("[blue]searching...[/blue]")
	url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json"
	req = requests.get(url)
	console = Console()
	if req.status_code == 200:
		data = req.json()
		items = data['Results']
		count = 0
		table = Table()
		for item in items:
			src1 = item['Value']
			src2 = item["ValueId"]
			src3 = item["Variable"]
			src4 = item["VariableId"]
			count += 1
			table.add_row(f"{src4}", f"{src3}", f"{src2}", f"{src1}")
			sleep(0.1)
		console.print(table)
		print(f"[bold green]found ({count}) results on the VIN number {vin}[bold green]")
	else:
		print("[blue]unable to receive data[/blue]")