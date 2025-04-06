import requests
import json
import os
import sys

from rich import print
from time import sleep

def vindecode(vin):
	print("[blue]searching...[/blue]")
	url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json"
	req = requests.get(url)

	if req.status_code == 200:
		data = req.json()
		items = data['Results']
		count = 0
		for item in items:
			src1 = item['Value']
			src2 = item["ValueId"]
			src3 = item["Variable"]
			src4 = item["VariableId"]
			count += 1
			print(f"[bold white]INFO-ID: [/bold white]( {src4} ) [bold white]INFO-DATA: [/bold white]( {src3} ) [bold white]INFO-DATA: [/bold white]( {src2} ) [bold white]INFO-DATA: [/bold white]( {src1} )")
			sleep(0.1)
		print(f"[bold green]found ({count}) results on the VIN number {vin}[bold green]")
	else:
		print("[blue]unable to receive data[/blue]")