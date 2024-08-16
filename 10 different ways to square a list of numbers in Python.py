#!/usr/bin/env python
# coding: utf-8

# # 10 Different ways to square a list in Python

# # Method 1: Using a for loop

# In[1]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print(squared_numbers)

#clcoding.com


# # Method 2: Using a list comprehension

# In[2]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

#clcoding.com


# # Method 3: Using the map() function with lambda

# In[3]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

#clcoding.com


# # Method 4: Using the map() function with a defined function

# In[4]:


numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers)

#clcoding.com


# # Method 5: Using the numpy library

# In[5]:


import numpy as np
numbers = [1, 2, 3, 4, 5]
squared_numbers = np.square(numbers)
print(squared_numbers)

#clcoding.com


# # Method 6: Using a generator expression

# In[6]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = (num ** 2 for num in numbers)
squared_numbers = list(squared_numbers)
print(squared_numbers)

#clcoding.com


# # Method 7: Using a list comprehension with zip()

# In[7]:


numbers = (1, 2, 3, 4, 5)
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

#clcoding.com


# # Method 8: Using the math library

# In[8]:


import math
numbers = [1, 2, 3, 4, 5]
squared_numbers = [math.pow(x, 2) for x in numbers]
print(squared_numbers)

#clcoding.com


# # Method 9: Using the operator module

# In[9]:


import operator
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(operator.mul, numbers, numbers))
print(squared_numbers)

#clcoding.com


# # Method 10: Using a loop with enumeration

# In[10]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for i, num in enumerate(numbers):
    # squared_numbers.append(numbers[i] ** 2)
    squared_numbers.append(num ** 2)
print(squared_numbers)

#clcoding.com


# In[ ]:




