a = 1
b = 5
print('Before swapping: a = ', a, ', b = ', b)

# # 1. Using a Temporary Variable:
# temp = a
# a = b
# b = temp

# # 2. Without Using a Temporary Variable :
# a = a + b
# b = a - b
# a = a - b

# # 3. Using Tuple Unpacking:
# a, b = b, a

# # 4. Using XOR bitwise operation:
# a = a ^ b
# b = a ^ b
# a = a ^ b

# 5. Using Arithmetic Operators in a Single Line:
a, b = b, a + b - a

print(' After swapping: a = ', a, ', b = ', b)
