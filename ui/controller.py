from .renderer.ansi import ANSIAnimator as a
from .renderer import cursore
import sys

def display(output,color=False,animation=False):

    def setup():

        for _ in range(len(output)):
            print("")
        sys.stdout.write(f"\033[{len(output)}A") 
        sys.stdout.flush()

    def colore_and_animation():

        setup()
        count= cursore.get_cursor_row()

        for i in output:
            count += 1

            a.move_text_horizontal(i, start_col=0, end_col=30, row=count, interval=0.05, color=a.GREEN)

        print ("\n")

    def only_colore():

        for i in output:

            print (a.GREEN+i+a.RESET)

    def only_animation():

        setup()

        count = cursore.get_cursor_row()

        for i in output:
            count += 1

            a.move_text_horizontal(i, start_col=0, end_col=30, row=count, interval=0.05)
        print ("\n")

    def normal():

        for i in output:
            print (i)

    if color and animation:
        colore_and_animation()

    elif color:
        only_colore()

    elif animation:
        only_animation()

    else:
        normal()



if __name__ == "__main__":

    display(['🔒 192.168.0.113 : IS EXIST', '✅ 192.168.0.1 : IS EXIST', '🔒 192.168.0.105 : IS EXIST', '🔒 192.168.0.106 : IS EXIST', '🔒 192.168.0.103 : IS EXIST'],color=False,animation=True)
