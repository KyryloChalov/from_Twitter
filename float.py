a = 0.3
b = 0.6
c = 0.9
def float_equal(a, b, c):
    print(f'{a} + {b} == {c} - {round(a + b, 3) == c} \t>>> {a} + {b} = {a + b}')

float_equal(a = 0.1, b = 0.2, c = 0.3)
float_equal(a = 0.1, b = 0.3, c = 0.4)
float_equal(a = 0.1, b = 0.4, c = 0.5)
float_equal(a = 0.1, b = 0.5, c = 0.6)

float_equal(a = 0.2, b = 0.4, c = 0.6)
float_equal(a = 0.3, b = 0.6, c = 0.9)
float_equal(a = 0.3, b = 0.5, c = 0.8)
float_equal(a = 0.4, b = 0.5, c = 0.9)
