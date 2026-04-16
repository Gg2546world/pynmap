import sys
import tty
import termios

def get_cursor_row():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:

        tty.setraw(sys.stdin.fileno())

        sys.stdout.write("\033[6n")
        sys.stdout.flush()


        res = ""
        while True:
            char = sys.stdin.read(1)
            res += char
            if char == "R":
                break

        row = int(res.split("[")[1].split(";")[0])
        return row
    finally:

        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

