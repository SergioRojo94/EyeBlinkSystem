eye_char = "O"
space_char = " "

def standard_eyes():  
    return [
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
    ]

def disgusting_face():
    return [
        f"{space_char * 2}{eye_char * 5}{space_char * 13}",
        f"{space_char * 2}{eye_char * 5}{space_char * 13}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",                                                                          
    ]

def blink_eye():
    num_rows = 4  # l2c screen number of rows

    left_eye_closed = f"{space_char * 2}{eye_char * 5}{space_char * 13}"
    closed_eye = []
    for _ in range(num_rows):
        closed_eye.append(left_eye_closed)

        true_eyes = closed_eye
    return true_eyes
