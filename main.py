import requests
import os
import sys
import json

from rich import print
from time import sleep
from chkconnection import chkinternet
from banner import Banner

import src.vinsearch as searchvin
import src.googlesearch as searchgoogle
import src.carsearch as searchcar

chkinternet()
Banner()

def vin_set(vin):
    return len(vin) > 1

def main():
	vin = ''

	_exit = False
	while not _exit:
		try:
			data = str(input("(thatvin): ")).strip()
		except KeyboardInterrupt:
		            print('[dark_orange]\nExiting...[/dark_orange]')
		            sleep(0.3)
		            exit()
		if data=="help":
			print("""
 options             descriptions
---------           --------------
 exit                exit script
 set.vin             type "set.vin" to set the vin number
 show.vin            type "show.vin" to view the set options for the VIN number
 help                show this help screen

 vin                 type "vin" to run a search aginst the VIN number
 google              type "google" to search the VIN number on google
 cardesc             type "cardesc" to get a description of the car you are looking
                     for from the VIN number
			""")
		elif data=="set.vin":
			print("set a valid Vehicle indentification number")
			vin = str(input("(Thatvin)(vin): ")).strip()
			print(f"vin: {vin}")
		elif data=="show.vin":
			if vin_set(vin):
				print(f"vin number {vin}")
			else:
				print(f"vin number: N/A")
		elif data=="vin":
			if not vin_set(vin):
				print("[bold blue][*][/bold blue] No VIN set.")
				continue
			searchvin.vindecode(vin)
		elif data=="google":
			if not vin_set(vin):
				print("[bold blue][*][/bold blue] No VIN set.")
				continue
			searchgoogle.googlesearch(vin)
		elif data=="cardesc":
			if not vin_set(vin):
				print("[bold blue][*][/bold blue] No VIN set.")
				continue
			searchcar.cardesc(vin)
		elif data=="exit":
			print('[dark_orange]\nExiting...[/dark_orange]')
			exit()
		else:
			print(f"wrong command [bold blue]{data}[/bold blue]?")
main()