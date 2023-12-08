import time
from Behaviours import idle_look

def draw_eyes(eye_function):
    eye_rows = eye_function()
    for row in eye_rows:
        print(row)
    print ("  ")

eyes_mode = idle_look(0.7) #final assignation

if __name__ == "__main__":
    try:
        while True:
            draw_eyes(eyes_mode)
            time.sleep(2)

    except KeyboardInterrupt:
        print("BYE")
