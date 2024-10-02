# 1. Using Mutable Default Arguments
# ==================================
# Mistake:

def add_item(item, items=[]):
    items.append(item)
    return items

# Problem: Default mutable arguments, like lists or dictionaries,
# retain changes between function calls, which can lead to unexpected behavior.
# Fix:

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# 2. Not Using List Comprehensions
# ================================
# Mistake:

result = []
for i in range(10):
    result.Append(i * 2)

# Problem: This approach is verbose and less efficient than it could be.
# Fix:

result = [i * 2 for i in range(10)]


# 3. Misunderstanding Python’s Scope Rules (LEGB Rule)
# ====================================================
# Mistake:

x = 10
def example():
    print(x)
    x = 5
example()

# Problem: This raises an UnboundLocalError because Python considers x inside example()
# as a local variable due to the assignment.
# Fix:

x = 10
def example():
    global x
    print(x)
    x = 5
example()


# 4. Using print() for Debugging Instead of Proper Debugging Tools
# ================================================================
# Mistake:

def calculate(x):
    print(f"Debug: x = {x}")
    return x * 2
result = calculate(5)

# Problem: Relying on print() statements for debugging can clutter code and is less efficient.
# Fix:

def calculate(x):
    return x * 2
result = calculate(5)
# Use a debugger for inspection
import pdb; pdb.set_trace()