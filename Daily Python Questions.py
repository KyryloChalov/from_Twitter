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