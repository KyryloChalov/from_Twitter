import sympy as sp

x = sp.Symbol("x")
f = input("Enter the function(in terms of x):")

F_indefinite = sp.integrate(f, x)
print("Indefinite integral ∫f(x) dx =", F_indefinite)

a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))

F_definite = sp.integrate(f, (x, a, b))
print(f"Definite integral ∫f(x) dx from {a} to {b} =", F_definite)
