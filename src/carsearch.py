import requests
import os
import sys

from rich import print
from time import sleep
from googlesearch import search
from bs4 import BeautifulSoup

def cardesc(vin):
	print("[blue]searching...[blue]")
	count = 0
	query = vin
	url = 'https://www.vinfreecheck.com/vin/'+vin.upper()+'/vehicle-specification'
	r = requests.get(url)
	html = BeautifulSoup(r.text, "html.parser")
	tag1 = html.find(["p"], class_="h2 subtitle-2")
	print(f"[bold white]INFO-CAR/TYPE: [/bold white]{tag1.string}")
	car = tag1.string
	for urlimg in search(f"{car}", num=50, stop=55, pause=5):
		try:
			req = requests.get(urlimg)
			soup = BeautifulSoup(req.text, 'html.parser')
			title = soup.find('title').get_text()
			print(f"[bold white]INFO-TITLE: [/bold white]( {title} )")
			print(f"[bold white]INFO-URL: [bold white]( {urlimg} )")
			count += 1
			sleep(0.1)
		except:
			pass
	print(f"found {count} results on {car}")
