import time
from Eye_arrays import standard_eyes, blink_eye, disgusting_face, looking_left, looking_right, closing_eyes

def idle_look(seconds):
    while True:
        mode = standard_eyes()
        for row in mode:
            print(row)
        time.sleep(seconds)
        mode = standard_eyes()
        for row in mode:
            print(row)
        time.sleep(seconds)
        mode = looking_left()
        for row in mode:
            print(row)
        time.sleep(seconds)
        mode = looking_right()
        for row in mode:
            print(row)
        time.sleep(seconds)
        mode = closing_eyes()
        for row in mode:
            print(row)
        time.sleep(seconds)
