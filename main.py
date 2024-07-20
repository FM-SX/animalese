from pynput.keyboard import Listener
from playsound import playsound
def on_press(key):
    key = key.char
    playsound(f'audio/english/{key}.wav')
with Listener(on_press=on_press) as listener:
    listener.join()
