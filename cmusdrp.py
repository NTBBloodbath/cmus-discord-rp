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
		duration = os.popen("cmus-remote -Q | grep \"duration\" | sed s/\"duration \"//").read()
		position = os.popen("cmus-remote -Q | grep \"position\" | sed s/\"position \"//").read()
		current_time = " (" + position + "/" + duration + ")"

		RPC.update(details=artist, state=title + current_time, large_image="logo")

if __name__ == "__main__":
	discord()
