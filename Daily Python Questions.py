# def fun(a, *args, s = '!') :
#     print(a, s)
#     for i in args :
#         print(i, s)
# fun(100)
# # >>> 100 !

# s = {1, 3, 7, 6, 5}
# s.discard(4)
# print(s)
# # >>> {1, 3, 5, 6, 7}

# s = { }
# t = {1, 4, 5, 2, 3}
# print(type(s), type(t))
# # >>> <class 'dict'> <class 'set'>

# msg = 'clcoding'
# ch = print(msg[-0])
# # >>> c

# print(3 % -2)
# # >>> -1

# msg = 'clcoding'
# s = list(msg[:4])[::-1]
# print(s)
# # >>> ['o', 'c', 'l', 'c']

# for i in range(4):
#     print(0.1 + i * 0.25)
# # >>> 0.1
# # >>> 0.35
# # >>> 0.6
# # >>> 0.85

# print(round(1 / 3, 2))
# # >>> 0.33

# lis = [[8, 7], [6, 5]]
# result = [p + q for p, q in lis]
# print(result)
# # >>> [15, 11]

# clcoding = '786'
# print(list(clcoding))
# # >>> ['7', '8', '6']

# num = [10, 20, 30, 40, 50]
# num[1:4] = [15, 25, 35]
# print(num)
# # >>> [10, 15, 25, 35, 50]

# print(1+True)
# # >>> 2

# a = (10, 20, 30)
# b = (40)
# print(a + b)
# # >>> TypeError: can only concatenate tuple (not "int") to tuple
# a = (10, 20, 30)
# b = (40, )
# print(a + b)
# # >>> (10, 20, 30, 40)

# a = "Hello"
# b = "Hello"
# print(f"a is b: {a is b}")
# print(f"a == b: {a == b}")
# # >>> a is b: True
# # >>> a == b: True

# s = set([1, 0, 2, 0, 3])
# s.remove(0)
# print(s)
# # >>> {1, 2, 3}

# my_list = [60, 70, 80, 90, 100]
# result = my_list[4::-1]
# print(result)
# # >>> [100, 90, 80, 70, 60]

# my_list = [1, 2, 3, 4, 5]
# result = my_list[1:4:2]
# print(result)
# # >>> [2, 4]

# list1 = [1, 2, 4, 3]
# list2 = [1, 2, 3, 4]
# print(list1 != list2)
# # >>> True

# tuple1 = (1, 2, 4, 3)
# tuple2 = (1, 2, 3, 4)
# print(tuple1 < tuple2)
# # >>> False

# i=j=[3]
# i+=j
# print(i,j)
# # >>> [3, 3] [3, 3]


# list1 = ["1.0", "a", "0.1", "1", "-1"]
# list2 = sorted(list1, key=lambda x: float(x) if x.isdigit() else float('inf'))
# print(list2)
# # >>> ['1', '1.0', 'a', '0.1', '-1']

# def key_(x):
#     # print('x: ', x, '   \t', 'x.isdigit(): ', x.isdigit())
#     return float(x) if x.isdigit() else float('inf')
# list1 = ["1.0", "a", "0.1", "1", "-1"]
# list2 = sorted(list1, key=key_)
# print(list2)
# # >>> ['1', '1.0', 'a', '0.1', '-1']


# import sys
# import getopt
# sys.argv =['C:\\a.py', '-h', 'word1', 'word2']
# options, arguments = getopt.getopt(sys.argv[1:], 's:t:h')
# print(options)
# # >>> [('-h', '')]
# # print(arguments)
# # >>> ['word1', 'word2']

# list1 = ["1.0", "a", "0.1", "1", "-1"]
# list2 = sorted(list1)
# print(list2)
# # >>> ['-1', '0.1', '1', '1.0', 'a']

# def fun(a, *args, s='!'):
#     print(a, s)
#     for i in args:
#         print(i, s)
# fun(10)
# # >>> 10 !

# def f1(a,b=[]):
#     b.append(a)
#     return b
# print (f1(2,[3,4]))
# # >>> [3, 4, 2]

# lst = [10, 25, 4, 12, 3, 8]
# sorted(lst)
# print(lst)
# # >>> [10, 25, 4, 12, 3, 8]
# lst = sorted(lst)
# print(lst)
# # >>> [3, 4, 8, 10, 12, 25]

# fruits = {'Kiwi', 'Jack Fruit', 'Lichi'}
# fruits.clear( )
# print(fruits)
# # >>> set()

# i, j, k = 4, -1, 0
# w = i  or j  or k    #  4  or -1 =  4,  4  or  0 =  4
# x = i and j and k    #  4 and -1 = -1, -1 and  0 =  0
# y = i  or j and k    # -1 and  0 = -1,  4  or -1 =  4
# z = i and j  or k    #  4 and -1 = -1, -1  or  0 = -1
# print(w, x, y, z)
# # >>> 4 0 4 -1

# j = 1
# while j <= 2:
#     print(j)
#     j++
# # >>> Error
#     j += 1
# # >>> 1
# # >>> 2

# for index in range(20, 10, -3):
#     print(index, end=' ')
# # >>> 20 17 14 11

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# print(a == c)
# print(a is c)
# # >>> True
# # >>> False

# my_list = [1, 2, 3, 4, 5]
# my_list[1:3] = [7, 8, 9]
# print(my_list)
# # >>> [1, 7, 8, 9, 4, 5]

# my_list = [1, 2, 3, 4, 5]
# my_list[1:2] = [7, 8, 9]
# print(my_list)
# # >>> [1, 7, 8, 9, 3, 4, 5]

# print(3 * 2 ** 3)
# # >>> 24

# print(True*10)
# # >>> 10

# print(False*10)
# # >>> 0

# def add(a, b):
#     return a + 5 , b + 5
# print(add(10, 11))
# # >>> (15, 16)

# s = set()
# s.update('hello', 'how', 'are', 'you?')
# print(len(s))
# # Коли ви використовуєте метод update() для множини (set) з кількома рядками, кожен символ з цих рядків додається до множини як окремий елемент.
# # >>> 10

# l=[1, 0, 2, 0, 'hello', '', []]
# print(list(filter(bool, l)))
# # >>> [1, 2, 'hello']

# def multipliers():
#     return [lambda x, i=i: i * x for i in range(4)]
# result = [m(2) for m in multipliers()]
# print(result)
# # >>> [0, 2, 4, 6]

# cl = ('a',)
# print(cl)
# # >>> ('a',)

# a = [10]
# b = [10]
# print(a is b)
# print(a == b)
# # >>> False
# # >>> True
# print(a[0] is b[0])
# # >>> True
# print(a[-1] is b[-1])
# # >>> True
# print(a[0] is b[-1])
# # >>> True

# s = {1, 2, 3, 4, 1}
# s.discard(0)
# print(s)
# # >>> {1, 2, 3, 4}

# def add(a, b):
#     return a + b
# result = add(3, '2')
# print(result)
# # >>> TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print([]*3)
# # >>> []

# x = 1
# while x <= 10:
#     if x % 3 == 0:
#         print(x)
#     x += 1
# # >>> 3
# # >>> 6
# # >>> 9

# x = 10
# while x > 0:
#     print(x)
#     x -= 1
# # >>> 10
# # >>> 9
# # >>> 8
# # >>> 7
# # >>> 6
# # >>> 5
# # >>> 4
# # >>> 3
# # >>> 2
# # >>> 1

# roman = {1:'i',2:'ii'}
# d,r=roman
# print(d,r)
# # >>> 1 2
# d,r=roman.keys()
# print(d,r)
# # >>> 1 2
# d1,r1=roman.values()
# print(d1,r1)
# # >>> i ii
# d2,r2=roman.items()
# print(d2,r2)
# # >>> (1, 'i') (2, 'ii')
# print(roman)
# # >>> {1: 'i', 2: 'ii'}

# c = 'hello'
# print(c.center(10, '1'))
# # >>> 11hello111

# numbers = [1, 2, 3]
# for num in numbers:
#     print(num)
# # >>> 1
# # >>> 2
# # >>> 3

# r = [20, 40, 60, 80]
# r[1:4] = []
# print(r)
# # >>> [20]

# a = [1, 2, 3, 4, 5]
# print(a[:4].pop())
# # >>> 4

# k = [2, 1, 0, 3, 0, 2, 1]
# print(k.count(k.index(0)))
# # Давайте розглянемо цей код крок за кроком:
# # k.index(0): Ця функція повертає індекс першого входження значення 0 в списку k. У вашому випадку, перше входження 0 знаходиться на індексі 2.
# # k.count(k.index(0)): Тепер цей вираз виглядає як k.count(2). Функція count() повертає кількість входжень значення 2 в списку k.
# # У списку k = [2, 1, 0, 3, 0, 2, 1] значення 2 зустрічається двічі.
# # Таким чином, результатом виконання print(k.count(k.index(0))) буде 2.
# # >>> 2

# q = [47, 28, 33, 54, 15]
# q.reverse()
# print(q[:3])
# # >>> [15, 54, 33]

# n = [76, 24]
# p = n.copy()
# n.pop()
# print(p, n)
# # >>> [76, 24] [76]

# g = [1, 2, 3, 2, 5]
# g.remove(2)
# print(g)
# # >>> [1, 3, 2, 5]

# lis = [10, 20, 30, 40]
# for m in lis:
#     print(m, end=' ')
#     if m >= 30:
#         break
# # >>> 10 20 30 

# for x in range(3):
#     print(x, end=' ')
# # >>> 0 1 2 

# a = 10
# while a > 8:
#     print(a, end=' ')
#     a = a - 1
# # >>> 10 9 

# for i in range(1):
#     print(i, end=' ')
# # >>> 0 

# for k in range(3, 9, 2):
#     print(k, end=' ')
# # >>> 3 5 7 

# lis = [[8, 7], [6, 5]]
# for p, q in lis:
#     print(p + q, end='&')
# # >>> 15&11&

# cl = 4
# while cl < 9:
#     cl = cl + 1
#     print(cl, end='-')
# # >>> 5-6-7-8-9-

# py = 2 + 3
# print('py')
# # >>> py # )))

# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])
# # >>> 3 44

# print('cd'.partition('cd'))
# # >>> ('', 'cd', '')

# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print(0)
# # >>> 0
# # >>> 1
# # >>> 2
# # >>> 0

# print('{0:.2f}'.format(1.0 / 3))
# # >>> 0.33

# def myfunc(a):
#     a = a + 2
#     a = a * 2
#     return a
# print(myfunc(2))
# # >>> 8

# i = 0
# while i < 3:
#     print(i)
#     i += 1
#     print(i + 1)
# # >>> 0
# # >>> 2
# # >>> 1
# # >>> 3
# # >>> 2
# # >>> 4

# y = 8
# z = lambda x : x * y
# print (z(6))
# # >>> 48

# L = ['a','b','c','d']
# print("".join(L))
# # >>> abcd

# cl = [2, 3, 1]
# print(cl.pop(2))
# # >>> 1
# print(cl)
# # >>> [2, 3]

# a = [2, 5, 3, 4]
# a[2:2] = [2]
# print(a)
# # >>> [2, 5, 2, 3, 4]

# x = ['1']
# x.extend('234')
# print(x)
# # >>> ['1', '2', '3', '4']

# s = 'clcoding'
# x = slice(1,4)
# print(s[x])
# print(s[1:4])
# # >>> lco

# r = '123'
# print(r.split( ))
# # >>> ['123']

# st1 = {1, 2, 3}
# st2 = {2, 3, 4}
# print(st2 - st1)
# # результатом буде нова множина, яка містить елементи, що є в першій множині, але відсутні в другій.
# # >>> 4

# a = [10]
# b = [10]
# print(a is b)
# # >>> False
# print(a[0] is b[0])
# # >>> True
# print(a == b)
# # >>> True

# my_list = [1, 2, 3]
# my_list.append([4, 5])
# print(len(my_list))
# # >>> 4
# print('my_list: ', my_list)
# # >>> my_list:  [1, 2, 3, [4, 5]]

# cl = [ ]
# print(cl * 2)
# # >>> []

# my_tuple = (1, 2, 3)
# my_tuple[1] = 4
# print(my_tuple)
# # >>> TypeError: 'tuple' object does not support item assignment

# my_list = [1, 2, 3]
# my_list[1] = 4
# print(my_list)
# # >>> [1, 4, 3]

# a = 18.5
# b = int(a)
# print(float(b))
# # >>> 18.0

# x = "PythonCoding"
# y = False
# z = (x[2:6] == "thon")
# z = int(z)
# print(z)
# # >>> 1

# print('Hello!2@#World'.istitle())
# >>> True

# a = [1, 2, 3]
# b = a.copy()
# print(a is b)
# # >>> False
# print(a == b)
# # >>> True

# x = [1, 2, 3]
# y = x
# print(x is y)
# # # >>> True
# print('x: ', x)
# print('y: ', y)
# x[1] = x[0] = x[2] = 0
# print('x: ', x)
# print('y: ', y)
# # # >>>x:  [1, 2, 3]
# # # >>>y:  [1, 2, 3]
# # # >>>x:  [0, 0, 0]
# # # >>>y:  [0, 0, 0]

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# result = set1.difference(set2)
# print('result: ', result)
# # >>> result:  {1, 2, 3}

# my_tuple = (1, 2, 3)
# my_tuple[0] = 4
# print(my_tuple)
# # >>> TypeError: 'tuple' object does not support item assignment

# my_list = [1, 2, 3]
# my_list.append([4, 5])
# print(my_list)
# # >>> [1, 2, 3, [4, 5]]

# my_dict = {"a": 1, "b": 2, "c": 3}
# result = my_dict.popitem()
# print(result)
# # # >>> ('c', 3)
# print('type(result): ', type(result))
# print('result[0]: ', result[0])
# print('result[0]: ', result[1])
# # >>> type(result):  <class 'tuple'>
# # >>> result[0]:  c
# # >>> result[0]:  3

# my_dict = {"a": 1, "b": 2, "c": 3}
# my_dict.clear()
# print(my_dict)
# # >>> {}

# my_list = [1, 2, 3, 4, 5]
# result = my_list[1:4:2]
# print(result)
# # >>> [2, 4]

# my_list = [1, 2, 3, 4, 5]
# result = my_list[-3:-1]
# print(result)
# # >>> [3, 4]

# my_dict = {"a": 1, "b": 2, "c": 3}
# result = my_dict.get("d", 0)
# print(result)
# # >>> 0
# result = my_dict.get("d", 5)
# print(result)
# # >>> 5

# def subtract(a, b):
#     return a - b
# result = subtract(7, subtract(4, 2))
# print(result)
# >>> 5

# my_set = {1, 2, 3}
# result = my_set.union({3, 4, 5})
# print(result)
# # >>> {1, 2, 3, 4, 5}

# def multiply(a, b):
#     return a * b
# result = multiply(3, multiply(2, 4))
# print(result)
# # >>> 24

# def uppercase_text(text):
#     return text.upper()
# result = uppercase_text("Hello, world!")
# print(result)
# # >>> HELLO, WORLD!

my_dict = {"a": 1, "b": 2, "c": 3}
result = (my_dict.values())
print(result)
# >>> dict_values([1, 2, 3])
print(20*'*')
print('my_dict: ', my_dict)
print('my_dict.values(): ', my_dict.values())
print('type(my_dict.values()): ', type(my_dict.values()))
print('list(my_dict.values()): ', list(my_dict.values()))
print('list(my_dict.values())[0]: ', list(my_dict.values())[0])
# >>> my_dict:  {'a': 1, 'b': 2, 'c': 3}
# >>> my_dict.values():  dict_values([1, 2, 3])
# >>> type(my_dict.values()):  <class 'dict_values'>
# >>> list(my_dict.values()):  [1, 2, 3]
# >>> list(my_dict.values())[0]:  1
print(20*'*')
print('my_dict.items(): ', my_dict.items())
print('dict(my_dict.items()): ', dict(my_dict.items()))
print('list(my_dict.items()): ', list(my_dict.items()))
# >>> my_dict.items():  dict_items([('a', 1), ('b', 2), ('c', 3)])
# >>> dict(my_dict.items()):  {'a': 1, 'b': 2, 'c': 3}
# >>> list(my_dict.items()):  [('a', 1), ('b', 2), ('c', 3)]
print(20*'*')
print('my_dict.keys(): ', my_dict.keys())
print('list(my_dict.keys()): ', list(my_dict.keys()))
# >>> my_dict.keys():  dict_keys(['a', 'b', 'c'])
# >>> list(my_dict.keys()):  ['a', 'b', 'c']