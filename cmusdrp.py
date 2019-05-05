#!/usr/bin/python
import os, time, logging
from pypresence import Presence

def discord():
	client_id = "574334562201501696"
	RPC = Presence(client_id)
	RPC.connect()

	while True:
		time.sleep(1)
		if os.popen("cmus-remote -Q | grep \"status \"").read() == "status stopped\n":
			artist = "  "
			title = "  "
			current_time = "IDLE"
		else:
			artist = os.popen("cmus-remote -Q | grep \"tag artist\" | sed s/\"tag artist \"//").read()
			title = os.popen("cmus-remote -Q | grep \"tag title\" | sed s/\"tag title \"//").read()
			
			if os.popen("cmus-remote -Q | grep \"status \"").read() == "status paused\n":
				current_time = "(paused)"
			else:
				position = int(os.popen("cmus-remote -Q | grep \"position\" | sed s/\"position \"//").read())
				duration = int(os.popen("cmus-remote -Q | grep \"duration\" | sed s/\"duration \"//").read())
				current_time = " (" + str(position) + "/" + str(duration) + ")"

		RPC.update(details=artist, state=title + current_time, large_image="logo")

if __name__ == "__main__":
	discord()
