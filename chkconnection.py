import requests
import socket
import os

from time import sleep
from rich import print

def chkinternet():
	os.system('clear')
	try:
	    socket.create_connection(("www.google.com", 80), timeout=5)
	    print("internet [bold green]connected[/bold green]")
	    sleep(1)
	except OSError:
	    print("Unable to [bold red]connection[/bold red]")
	    sleep(1)
	    