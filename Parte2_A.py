import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d



def integrate_repeated(f, a, b, n, rule_func):
    result = 0
    subinterval_width = (b - a) / n

    for i in range(n):
        subinterval_a = a + i * subinterval_width
        subinterval_b = a + (i + 1) * subinterval_width
        result += rule_func(f, subinterval_a, subinterval_b, 100)

    return result

def trapezio_func(f, x0, x1, n = 1):
    h = (x1 - x0)/ n
    result = (h / 2) * (f(x0) + f(x1))
    return result

def simpson13_func(f, x0, x1,x2,n = 1):
    h = (x1 - x0)/ n
    result = (h / 3) * (f(x0) + (4 * f(x1)) + f(x2))
    return result

def simpson38_func(f, x0, x1, x2, x3, n):
    h = (x1 - x0)/ n
    result = (h / 3) * (f(x0) + (3 * f(x1)) + (3 * f(x2)) +f(x3))
    return result

# Exemplo de uso:
def example_function(x):
    return x**2

a, b = 0, 1
n = 4

trap_result, _ = quad(lambda x: example_function(x), a, b)
trap_repeated_result = integrate_repeated(lambda x: example_function(x), a, b, n, trapezio_func)
print(f"Resultado usando regra do trapézio: {trap_result}, Resultado repetido: {trap_repeated_result}")

simpson_one_third_result, _ = quad(lambda x: example_function(x), a, b)
simpson_one_third_repeated_result = integrate_repeated(lambda x: example_function(x), a, b, n, simpson13_func)
print(f"Resultado usando regra de 1/3 de Simpson: {simpson_one_third_result}, Resultado repetido: {simpson_one_third_repeated_result}")

simpson_three_eighth_result, _ = quad(lambda x: example_function(x), a, b)
simpson_three_eighth_repeated_result = integrate_repeated(lambda x: example_function(x), a, b, n, simpson38_func)
print(f"Resultado usando regra de 3/8 de Simpson: {simpson_three_eighth_result}, Resultado repetido: {simpson_three_eighth_repeated_result}")