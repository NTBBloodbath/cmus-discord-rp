#!/usr/bin/python
import os, time, logging
from pypresence import Presence

def discord():
	old_timestamp = '0:00'
	client_id = "574334562201501696"
	RPC = Presence(client_id)
	RPC.connect()

	while True:
		time.sleep(1)
		artist = os.popen("cmus-remote -Q | grep \"tag artist\" | sed s/\"tag artist \"//").read()
		title = os.popen("cmus-remote -Q | grep \"tag title\" | sed s/\"tag title \"//").read()

		RPC.update(details=artist, state=title, large_image="logo")

if __name__ == "__main__":
	discord()
