import numpy as np
from scipy.integrate import quad

# A trapezio
def trapezio_func(f, a, b, m):
    h = (b - a) / m
    x = np.linspace(a, b, m + 1)
    y = f(x)
    resultado = (h/2) * (y[0] + 2 * np.sum(y[1:m]) + y[m])
    return resultado


# B simpson 1/3
def simpson13_func(f, a, b, m):
    h = (b - a) / m
    x = np.linspace(a, b, m + 1)
    y = f(x)
    resultado = (h/ 3) * (y[0] + 4 * np.sum(y[1:m:2]) + 2 * np.sum(y[2:m-1:2]) + y[m]) 
    return resultado


# C simpson 3/8
def simpson38_func(f, a, b, m):
    h = (b - a) / m
    x = np.linspace(a, b, m + 1)
    y = f(x)
    resultado = ((3 * h)/ 8) * (y[0] + 3 * np.sum(y[1:m-2:3]) + 3 * np.sum(y[2:m-1:3]) + 2 * np.sum(y[3:m-3:3]) + y[m]) 
    return resultado



# função integral:
def integral(x):
    return x**2 * np.log((x**2) + 1)
    #return x**2


# calcula o erro
def calcula_erro(resultado, referencia):
    return np.abs(resultado - referencia)


# faz uma estimativa de qual sera o valor do m de acordo com o valor do erro
def estima_subintervalos(method, f, a, b, erro_final):
    m = 1
    while True:
        resultado = method(f, a, b, m)
        erro = calcula_erro(resultado, quad(f, a, b)[0])
        if erro < erro_final:
            return m
        m *= 2


# Valores iniciais
erro_final = 1e-4
a = 0
b = 2

# valores de m para cada
m_trapezio = estima_subintervalos(trapezio_func, integral, a, b, erro_final)
m_simpson13 = estima_subintervalos(simpson13_func, integral, a, b, erro_final)
m_simpson38 = estima_subintervalos(simpson38_func, integral, a, b, erro_final)

# Calcular os resultados finais
resultado_trapezio = trapezio_func(integral, a, b, m_trapezio)
resultado_simpson13 = simpson13_func(integral, a, b, m_simpson13)
resultado_simpson38 = simpson38_func(integral, a, b, m_simpson38)

# Comparar os resultados com a função quad
result_quad, _ = quad(integral, a, b)

# Mostrando os valores
# 2 - A
print(f"Resultado usando regra do Trapézio com {m_trapezio} subintervalos: {resultado_trapezio}")
print(f"Resultado usando regra 1/3 de Simpson com {m_simpson13} subintervalos: {resultado_simpson13}")
print(f"Resultado usando regra 3/8 de Simpson com {m_simpson38} subintervalos: {resultado_simpson38}")

#2 - B
print(f"Resultado usando função quad: {result_quad}")
