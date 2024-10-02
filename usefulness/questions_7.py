# *__, a, b, *_ = [1, 2, 3, 4, 5, 6]
# print(__, _)

# 1
# @print
# def testing():
#     print('hello!!')
#     return 1000

# testing()

# #2
# a, b, *_ = [1, 2, 3, 4, 5]
# print(_)

# def add(symbol):
#     def wrapper1(func):
#         def wrapper2(*args, **kwargs):
#             return func(*args, **kwargs) + symbol
#     return wrapper1

# @add('!!')
# def hello(name):
#     return 'hello' + name

# print(hello('tom'))