import time
from Eye_arrays import standard_eyes, blink_eye, disgusting_face

def draw_eyes(eye_function):
    eye_rows = eye_function()
    for row in eye_rows:
        print(row)
    print (f"  ")

eyes_mode = blink_eye #final assignation

if __name__ == "__main__":
    try:
        while True:
            draw_eyes(eyes_mode)
            time.sleep(2)

    except KeyboardInterrupt:
        print("BYE")
