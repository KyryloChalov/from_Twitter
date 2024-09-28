BACK_COLORS = [40, 100, 41, 101, 42, 102, 43, 103, 44, 104, 45, 105, 46, 106, 47, 107]
"""
4B - dark, 10B - light
B:
0 - black/gray, 1 - red, 2 - green, 3 - yellow, 4 - blue, 5 - magenta, 6 - cyan, 7 - white
"""
TEXT_COLORS = [30, 90, 31, 91, 32, 92, 33, 93, 34, 94, 35, 95, 36, 96, 37, 97]
"""
3T - dark, 9T - light
T:
0 - gray, 1 - red, 2 - green, 3 - yellow, 4 - blue, 5 - magenta, 6 - cyan, 7 - white"""
STYLES = [0, 1, 2, 3, 4, 5, 6, 7]
"""
0 - reset, 1 - bold, 2 - dark, 3 - italics, 4 - underline, 5,6 - normal, 7 - back"""


RESET = "\033[0m"


class ANSI:
    def background(code):
        return "\33[{code}m".format(code=code)

    def color_text(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)


for bc in BACK_COLORS:
    for tc in TEXT_COLORS:
        for st in STYLES:
            color_code = ANSI.background(bc) + ANSI.color_text(tc) + ANSI.style_text(st)
            print(
                f"|{color_code} b:{'  ' if bc<100 else ' '}{bc} t: {tc} s: {st} {RESET}",
                end="",
            )
        # print(50 * "=")
        print()
