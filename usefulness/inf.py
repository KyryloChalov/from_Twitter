# Defining a positive infinite integer
positive_infinity = float("inf")
print("Positive Infinity: ", positive_infinity)
# Defining a negative infinite integer
negative_infinity = float("-inf")
print("Negative Infinity: ", negative_infinity)


import math

# Defining a positive infinite integer
positive_infinity = math.inf
print("Positive Infinity: ", positive_infinity)
# Defining a negative infinite integer
negative_infinity = -math.inf
print("Negative Infinity: ", negative_infinity)


from decimal import Decimal

# Defining a positive infinite integer
positive_infinity = Decimal("Infinity")
print("Positive Infinity: ", positive_infinity)
# Defining a negative infinite integer
negative_infinity = Decimal("-Infinity")
print("Negative Infinity: ", negative_infinity)


import numpy as np

# Defining a positive infinite integer
positive_infinity = np.inf
print("Positive Infinity: ", positive_infinity)
# Defining a negative infinite integer
negative_infinity = -np.inf
print("Negative Infinity: ", negative_infinity)


import numpy as np
import math

# Defining a positive infinite integer
a = np.inf
# Defining a negative infinite integer
b = -np.inf
# Define a finite integer
c = 300
# check if a in infinite
print(math.isinf(a))
# check if b in infinite
print(math.isinf(b))
# check if c in infinite
print(math.isinf(c))
