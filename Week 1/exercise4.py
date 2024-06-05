import math

def sin(x, n):
    sum = 0
    for i in range(n + 1):
        sum += ((-1) ** i) * (x ** (2*i + 1)) / math.factorial(2 * i + 1)
    return sum

def cos(x, n):
    sum = 0
    for i in range(n + 1):
        sum += ((-1) ** i) * (x ** (2*i)) / math.factorial(2*i)
    return sum

def sinh(x, n):
    sum = 0
    for i in range(n + 1):
        sum += (x ** (2*i + 1)) / math.factorial(2*i + 1)
    return sum

def cosh(x, n):
    sum = 0
    for i in range(n + 1):
        sum += (x ** (2 * i)) / math.factorial(2*i)
    return sum

print(cosh(3.14, 10))