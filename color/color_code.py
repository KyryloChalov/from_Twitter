BACK_COLORS = [40, 100, 41, 101, 42, 102, 43, 103, 44, 104, 45, 105, 46, 106, 47, 107]
"""
4B - dark, 10B - light
B:
0 - black/gray, 1 - red, 2 - green, 3 - yellow, 4 - blue, 5 - magenta, 6 - cyan, 7 - white
"""
BLACK_BACK = "\33[40m"
RED_BACK = "\33[41m"
GREEN_BACK = "\33[42m"
YELLOW_BACK = "\33[43m"
BLUE_BACK = "\33[44m"
MAGENTA_BACK = "\33[45m"
CYAN_BACK = "\33[47m"
GRAY_BACK = "\33[100m"
LIGHTRED_BACK = "\33[101m"
LIGHTGREEN_BACK = "\33[102m"
LIGHTYELLOW_BACK = "\33[103m"
LIGHTBLUE_BACK = "\33[104m"
LIGHTMAGENTA_BACK = "\33[105m"
LIGHTCYAN_BACK = "\33[106m"
LIGHTWHITE_BACK = "\33[107m"


TEXT_COLORS = [30, 90, 31, 91, 32, 92, 33, 93, 34, 94, 35, 95, 36, 96, 37, 97]
"""
3T - dark, 9T - light
T:
0 - gray, 1 - red, 2 - green, 3 - yellow, 4 - blue, 5 - magenta, 6 - cyan, 7 - white
"""
BLACK = "\33[30m"
RED = "\33[31m"
GREEN = "\33[32m"
YELLOW = "\33[33m"
BLUE = "\33[34m"
MAGENTA = "\33[35m"
CYAN = "\33[37m"
GRAY = "\33[90m"
LIGHTRED = "\33[91m"
LIGHTGREEN = "\33[92m"
LIGHTYELLOW = "\33[93m"
LIGHTBLUE = "\33[94m"
LIGHTMAGENTA = "\33[95m"
LIGHTCYAN = "\33[96m"
LIGHTWHITE = "\33[97m"


STYLES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
0 - reset, 1 - bold, 2 - dark, 3 - italics, 4 - underline, 5,6 - normal, 7 - back, 8 - fill, 9 - cross
"""
RESET = "\33[0m"
BOLD = "\33[1m"
DARK = "\33[2m"
ITALIC = "\33[3m"
UNDERLINE = "\33[4m"
BLINK = "\33[5m"
NORMAL = "\33[6m"
REVERSE = "\33[7m"
FILL = "\33[8m"
CROSS = "\33[9m"

def table_head():
    print(140 * "-")
    head_string = [
        "RESET",
        "BOLD",
        "DARK",
        "ITALIC",
        "UNDERLINE",
        "BLINK?",
        "NORMAL?",
        "REVERSE",
        "FILL",
        "CROSS",
    ]
    # print("|")
    for text in head_string:
        print(f"{text.center(13, " ")}", end="|")
    print()
    print(140 * "-")


def color_print(to_print="", code="", end="\n"):
    print(f"{code}{str(to_print)}{RESET}", end=end)


def demo():
    table_head()
    for bc in BACK_COLORS:
        for tc in TEXT_COLORS:
            for st in STYLES:
                code_str = f'\33[{";".join((str(bc), str(tc), str(st)))}m'
                color_print(
                    f"{' ' if bc < 100 else ''}\\33{code_str[1:]}",
                    code=code_str,
                    end="",
                )
                print("|", end="")
            print()


if __name__ == "__main__":
    demo()
