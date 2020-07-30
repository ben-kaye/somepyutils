import math
def exp(x):
    return sum ([
        x**n / math.factorial(n)
        for n in range(0,100)
    ])