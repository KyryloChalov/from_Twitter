from termcolor import colored

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])

print(text)

print(colored('Hello, World!', 'red', 'on_black', ['bold', 'blink']))
print(colored('Hello, World!', 'green'))
