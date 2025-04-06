from googlesearch import search
from rich import print
from time import sleep
from bs4 import BeautifulSoup

import os
import sys
import requests

def googlesearch(vin):
	count = 0
	query = vin
	print(f"[blue]searching {vin}...[blue]")
	for url in search(query, num=50, stop=55, pause=5):
		try:
			req = requests.get(url)
			soup = BeautifulSoup(req.text, 'html.parser')
			title = soup.find('title').get_text()
			print(f"[bold white]INFO-TITLE: [/bold white]( {title} )")
			print(f"[bold white]INFO-URL: [bold white]( {url} )")
			count += 1
			sleep(0.1)
		except:
			pass
	print(f"found {count} results on {vin}")