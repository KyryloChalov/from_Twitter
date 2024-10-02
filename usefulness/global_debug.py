x = 10


def example():
    global x
    print(x)
    x = 5
    print(x)


example()


def calculate(x):
    print(f"Debug: x = {x}")
    return x * 2


result = calculate(5)

# Problem: Relying on print() statements for debugging can clutter code and is less efficient.
# Fix:


# def calculate(x):
#     return x * 2


# result = calculate(5)
# Use a debugger for inspection
# import pdb

# pdb.set_trace()
