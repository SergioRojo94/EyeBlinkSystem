eye_char = "O"
space_char = " "
num_rows = 4

def standard_eyes():  
    return [
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 2}{space_char * 1}{eye_char * 2}{space_char * 6}{eye_char * 2}{space_char * 1}{eye_char * 2}{space_char * 2}",
        f"{space_char * 2}{eye_char * 2}{space_char * 1}{eye_char * 2}{space_char * 6}{eye_char * 2}{space_char * 1}{eye_char * 2}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
    ]

def looking_left():  
    return [
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 1}{space_char * 2}{eye_char * 2}{space_char * 6}{eye_char * 1}{space_char * 2}{eye_char * 2}{space_char * 2}",
        f"{space_char * 2}{eye_char * 1}{space_char * 2}{eye_char * 2}{space_char * 6}{eye_char * 1}{space_char * 2}{eye_char * 2}{space_char * 2}",
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
    ]

def looking_right():  
    return [
        f"{space_char * 2}{eye_char * 5}{space_char * 6}{eye_char * 5}{space_char * 2}",
        f"{space_char * 2}{eye_char * 2}{space_char * 2}{eye_char * 1}{space_char * 6}{eye_char * 2}{space_char * 2}{eye_char * 1}{space_char * 2}",
        f"{space_char * 2}{eye_char * 2}{space_char * 2}{eye_char * 1}{space_char * 6}{eye_char * 2}{space_char * 2}{eye_char * 1}{space_char * 2}",
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
      # l2c screen number of rows

    left_eye_closed = f"{space_char * 2}{eye_char * 5}{space_char * 13}"
    closed_eye = []
    for _ in range(num_rows):
        closed_eye.append(left_eye_closed)

        true_eyes = closed_eye
    return true_eyes

def closing_eyes():
    closing_eyes_array = []
    for _ in range(num_rows):
        closing_eyes_array.append(f"{space_char *20}")
        
    return closing_eyes_array