import color_code as cc

print(cc.YELLOW, "Yellow text")
print("Next string without RESET")

print(cc.RED, "Red text", cc.RESET)
print("Next string after RESET")

print(cc.BLUE, "Blue text", cc.RESET, " - note the leading space")
print(f"{cc.BLUE}Blue text{cc.RESET} - use f-string")

# 
print(
    cc.RED,
    "Red text",
    cc.LIGHTRED,
    "Lightred text",
    cc.BOLD,
    "Bold LightRed text",
    cc.ITALIC,
    "Italic Bolt LightRed text",
    cc.BLUE,
    "Italic Bolt Blue text",
    cc.MAGENTA,
    "Italic Bolt Magenta text",
    cc.RESET,
)

print(
    cc.YELLOW_BACK, cc.BLUE, cc.ITALIC, cc.BOLD, "Blu Italic text on Yellow", cc.RESET
)
cc.color_print(
    "Blu Italic text on Yellow - use 'cc.color_print' function",
    cc.YELLOW_BACK + cc.BLUE + cc.ITALIC + cc.BOLD,
)


cc.color_print(
    " Dark Yellow Bold Underline Cross Italic on Blue - use cc.color_print function",
    cc.YELLOW + cc.DARK + cc.BOLD + cc.UNDERLINE + cc.BLUE_BACK + cc.ITALIC + cc.CROSS,
)

print(
    cc.YELLOW,
    "Yellow text",
    cc.RED,
    "Red text",
    cc.BLUE,
    "Blue text",
    cc.RESET,
    "- 'extra' spaces",
)
print(f"{cc.YELLOW}Yellow text {cc.RED}Red text {cc.BLUE}Blue text {cc.RESET}")
cc.color_print("Yellow text", cc.YELLOW, end=" ")
cc.color_print("Red text", cc.RED, end=" ")
cc.color_print("Blue text", cc.BLUE)

# cc.demo()

bc = 40  # black background only - if you want to see all the options, use cc.demo()
print(131 * "-")
head_string = ['RESET','BOLD','DARK','ITALIC','UNDERLINE','BLINK?','NORMAL?','REVERSE','FILL','CROSS']
for text in head_string:
    print(f'|{text.center(12, ' ')}', end='')
print('|')
print(131 * "-")
for tc in cc.TEXT_COLORS:
    print(end="|")
    for st in cc.STYLES:
        code_str = f'\33[{";".join((str(bc), str(tc), str(st)))}m'
        cc.color_print(
            f"\\33{code_str[1:]}",
            code=code_str,
            end="",
        )
        print("|", end="")
    print()
