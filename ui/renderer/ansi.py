import sys
import time

class ANSIAnimator:
    # ==============================
    # أساسي
    # ==============================
    ESC = "\033["
    OSC = "\033]"
    BEL = "\007"

    RESET = ESC + "0m"
    HIDE_CURSOR = ESC + "?25l"
    SHOW_CURSOR = ESC + "?25h"
    SAVE_CURSOR = ESC + "s"
    RESTORE_CURSOR = ESC + "u"

    # ==============================
    # أنماط النص
    # ==============================
    BOLD = ESC + "1m"
    DIM = ESC + "2m"
    ITALIC = ESC + "3m"
    UNDERLINE = ESC + "4m"
    BLINK = ESC + "5m"
    REVERSE = ESC + "7m"
    HIDDEN = ESC + "8m"
    STRIKE = ESC + "9m"

    # ==============================
    # ألوان النص الأساسية
    # ==============================
    BLACK = ESC + "30m"
    RED = ESC + "31m"
    GREEN = ESC + "32m"
    YELLOW = ESC + "33m"
    BLUE = ESC + "34m"
    MAGENTA = ESC + "35m"
    CYAN = ESC + "36m"
    WHITE = ESC + "37m"

    BRIGHT_BLACK = ESC + "90m"
    BRIGHT_RED = ESC + "91m"
    BRIGHT_GREEN = ESC + "92m"
    BRIGHT_YELLOW = ESC + "93m"
    BRIGHT_BLUE = ESC + "94m"
    BRIGHT_MAGENTA = ESC + "95m"
    BRIGHT_CYAN = ESC + "96m"
    BRIGHT_WHITE = ESC + "97m"

    # ==============================
    # ألوان الخلفية
    # ==============================
    BG_BLACK = ESC + "40m"
    BG_RED = ESC + "41m"
    BG_GREEN = ESC + "42m"
    BG_YELLOW = ESC + "43m"
    BG_BLUE = ESC + "44m"
    BG_MAGENTA = ESC + "45m"
    BG_CYAN = ESC + "46m"
    BG_WHITE = ESC + "47m"

    BG_BRIGHT_BLACK = ESC + "100m"
    BG_BRIGHT_RED = ESC + "101m"
    BG_BRIGHT_GREEN = ESC + "102m"
    BG_BRIGHT_YELLOW = ESC + "103m"
    BG_BRIGHT_BLUE = ESC + "104m"
    BG_BRIGHT_MAGENTA = ESC + "105m"
    BG_BRIGHT_CYAN = ESC + "106m"
    BG_BRIGHT_WHITE = ESC + "107m"

    # ==============================
    # دمج تأثيرات
    # ==============================
    @staticmethod
    def style(text, *effects):
        """دمج عدة تأثيرات مثل اللون والخلفية والنمط"""
        return "".join(effects) + text + ANSIAnimator.RESET

    # ==============================
    # 256 لون و RGB
    # ==============================
    @staticmethod
    def color256(text, code):
        return f"\033[38;5;{code}m{text}{ANSIAnimator.RESET}"

    @staticmethod
    def bg256(text, code):
        return f"\033[48;5;{code}m{text}{ANSIAnimator.RESET}"

    @staticmethod
    def rgb(text, r, g, b):
        return f"\033[38;2;{r};{g};{b}m{text}{ANSIAnimator.RESET}"

    @staticmethod
    def bg_rgb(text, r, g, b):
        return f"\033[48;2;{r};{g};{b}m{text}{ANSIAnimator.RESET}"

    # ==============================
    # تحريك المؤشر
    # ==============================
    @staticmethod
    def up(n=1): return f"\033[{n}A"
    @staticmethod
    def down(n=1): return f"\033[{n}B"
    @staticmethod
    def right(n=1): return f"\033[{n}C"
    @staticmethod
    def left(n=1): return f"\033[{n}D"
    @staticmethod
    def move(row, col): return f"\033[{row};{col}H"

    # ==============================
    # مسح الشاشة والسطر
    # ==============================
    CLEAR_SCREEN = ESC + "2J"
    CLEAR_LINE = ESC + "2K"
    CLEAR_FROM_CURSOR = ESC + "0J"

    # ==============================
    # الشاشة البديلة وتغيير العنوان
    # ==============================
    ALT_SCREEN_ENABLE = ESC + "?1049h"
    ALT_SCREEN_DISABLE = ESC + "?1049l"
    @staticmethod
    def set_title(title):
        return f"\033]0;{title}\007"

    # ==============================
    # أنيميشن: سبينر
    # ==============================
    @staticmethod
    def spinner(symbols=None, duration=3, interval=0.1, color=None):
        if symbols is None:
            symbols = ["|", "/", "-", "\\"]
        end_time = time.time() + duration
        sys.stdout.write(ANSIAnimator.HIDE_CURSOR)
        i = 0
        while time.time() < end_time:
            s = symbols[i % len(symbols)]
            sys.stdout.write("\r" + (f"{color}{s}{ANSIAnimator.RESET}" if color else s))
            sys.stdout.flush()
            time.sleep(interval)
            i += 1
        sys.stdout.write("\r \r")
        sys.stdout.write(ANSIAnimator.SHOW_CURSOR)

    # ==============================
    # أنيميشن نص أفقي
    # ==============================
    @staticmethod
    def move_text_horizontal(text, start_col=0, end_col=40, row=5, interval=0.05, color=None, ping_pong=False):
        sys.stdout.write(ANSIAnimator.HIDE_CURSOR)
        positions = list(range(start_col, end_col + 1))
        if ping_pong:
            positions += list(range(end_col - 1, start_col, -1))
        for pos in positions:
            sys.stdout.write(ANSIAnimator.move(row, pos) + ANSIAnimator.CLEAR_LINE)
            output = f"{color}{text}{ANSIAnimator.RESET}" if color else text
            sys.stdout.write(output)
            sys.stdout.flush()
            time.sleep(interval)
        sys.stdout.write(ANSIAnimator.SHOW_CURSOR)

    # ==============================
    # أنيميشن نص رأسي
    # ==============================
    @staticmethod
    def move_text_vertical(text, col=10, start_row=0, end_row=10, interval=0.1, color=None, ping_pong=False):
        sys.stdout.write(ANSIAnimator.HIDE_CURSOR)
        positions = list(range(start_row, end_row + 1))
        if ping_pong:
            positions += list(range(end_row - 1, start_row, -1))
        for row in positions:
            sys.stdout.write(ANSIAnimator.move(row, col) + ANSIAnimator.CLEAR_LINE)
            output = f"{color}{text}{ANSIAnimator.RESET}" if color else text
            sys.stdout.write(output)
            sys.stdout.flush()
            time.sleep(interval)
        sys.stdout.write(ANSIAnimator.SHOW_CURSOR)

    # ==============================
    # تحريك عدة نصوص معًا (multi-object)
    # ==============================
    @staticmethod
    def move_multiple(objects, interval=0.05):
        """
        objects = قائمة من القواميس
        كل عنصر: {"text": str, "row": int, "start_col": int, "end_col": int, "color": str, "ping_pong": bool}
        """
        sys.stdout.write(ANSIAnimator.HIDE_CURSOR)
        max_len = max(obj["end_col"] - obj["start_col"] for obj in objects)
        for step in range(max_len + 1):
            for obj in objects:
                positions = list(range(obj["start_col"], obj["end_col"] + 1))
                if obj.get("ping_pong", False):
                    positions += list(range(obj["end_col"] - 1, obj["start_col"], -1))
                pos = positions[step % len(positions)]
                sys.stdout.write(ANSIAnimator.move(obj["row"], pos) + ANSIAnimator.CLEAR_LINE)
                output = f'{obj.get("color","")}{obj["text"]}{ANSIAnimator.RESET}'
                sys.stdout.write(output)
            sys.stdout.flush()
            time.sleep(interval)
        sys.stdout.write(ANSIAnimator.SHOW_CURSOR)
