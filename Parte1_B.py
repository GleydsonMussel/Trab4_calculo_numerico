import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Configuração das fontes
fonte_titulo={  
              "fontsize":14,
              "fontweight": 'bold',
              "fontname":'Times New Roman',
              }
fonte_labels={
            "fontsize":12,
            "fontweight":'bold',
            'fontname':'Times New Roman',
            }
fonte_legenda={
            "size":9,
            "weight":'normal',
            'family':'Times New Roman',
            }

# FUNÇÃO
def funcao(x):
    return 1/(1+25*x**2)

intervalo_de_teste_terceiro_grau = np.arange(-1,1+2/3,2/3)
intervalo_de_teste_quinto_grau = np.arange(-1,1+2/5,2/5)
intervalo_de_teste_decimo_grau = np.arange(-1,1+2/10,2/10)
intervalo_funcao_referencia = np.arange(-1, 1, 0.0001)
ys_terceiroGrau = [funcao(i) for i in intervalo_de_teste_terceiro_grau]
ys_quintoGrau = [funcao(i) for i in intervalo_de_teste_quinto_grau]
ys_decimoGrau = [funcao(i) for i in intervalo_de_teste_decimo_grau]
ys_referencia = [funcao(i) for i in intervalo_funcao_referencia]

# Contornando Fenômeno de Runge
x_pontos_equidistantes = np.linspace(-1, 1, 11)
y_pontos_equidistantes = [funcao(elemento) for elemento in x_pontos_equidistantes]

# Interpolação usando spline cúbica
spline_cubica = interp1d(x_pontos_equidistantes, y_pontos_equidistantes, kind='cubic')

plt.title("Gráfico Comparativo Contornando o Fenômeno de Runge", fontdict = fonte_titulo)
plt.xlabel("Eixo x", fontdict = fonte_labels)
plt.xlim(-1,1)
plt.ylabel("Eixo y", fontdict = fonte_labels)
plt.ylim(-0.5,2)
plt.grid()
# Descomentar para plotar o gráfico das spines
plt.plot(x_pontos_equidistantes, y_pontos_equidistantes, 'o', label='Pontos de Dados Equidistantes')
plt.plot(intervalo_funcao_referencia, spline_cubica(intervalo_funcao_referencia), '--', label='Spline Cúbica Interpolada')
plt.plot(intervalo_funcao_referencia, ys_referencia, label = "Função")
#plt.plot(intervalo_funcao_referencia, np.polyval(np.polyfit(intervalo_de_teste_terceiro_grau, ys_terceiroGrau, 3), intervalo_funcao_referencia), label = "Polinomio de Grau 3")
#plt.plot(intervalo_funcao_referencia, np.polyval(np.polyfit(intervalo_de_teste_quinto_grau, ys_quintoGrau, 5), intervalo_funcao_referencia), label = "Polinomio de Grau 5")
#plt.plot(intervalo_funcao_referencia, np.polyval(np.polyfit(intervalo_de_teste_decimo_grau, ys_decimoGrau, 10), intervalo_funcao_referencia), label = "Polinomio de Grau 10")
plt.legend(prop=fonte_legenda, loc='upper center', fancybox=False)
plt.savefig("./Graficos/GraficoParte1_B_2.png")