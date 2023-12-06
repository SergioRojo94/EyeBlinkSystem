import time

def draw_eyes():
    eye_char = "O"
    space_char = " "

    # Standard/left eye
    chris_and_serch = [
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"                                                                             "
    ]

    # Definition of left eye row
    eye_rows = chris_and_serch

    # blink
    blink_eye_rows = [
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 13}",
        f"{space_char * 2}{eye_char * 1}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"                                                                             "
    ]

    # Select expression (standard or blinking)
    true_eyes = eye_rows
    for row in true_eyes:
        print(row)

if __name__ == "__main__":
    try:
        while True:
            draw_eyes()
            time.sleep(0.1) 

    except KeyboardInterrupt:
        print("Saliendo del programa.")
