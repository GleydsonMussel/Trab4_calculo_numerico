import numpy as np
import matplotlib.pyplot as plt

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

# EXERCÍCIO 1

idades_frangos = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
pesos_fetos_frangos = [0.029, 0.052, 0.079, 0.125, 0.181, 0.261, 0.425, 0.738, 1.130, 1.882, 2.812]
valores_idades_plot = [i+5 for i in range(15)]

# Polinomios
poliGrau1 = np.polyfit(idades_frangos, pesos_fetos_frangos, 1)
funcao_aproximada1 = np.poly1d(poliGrau1)  
y_aproximado1 = funcao_aproximada1(idades_frangos)
erro1 = np.linalg.norm(pesos_fetos_frangos - y_aproximado1)

poliGrau2 = np.polyfit(idades_frangos, pesos_fetos_frangos, 2)
funcao_aproximada2 = np.poly1d(poliGrau2)
y_aproximado2 = funcao_aproximada2(idades_frangos)
erro2 = np.linalg.norm(pesos_fetos_frangos - y_aproximado2)

poliGrau3 = np.polyfit(idades_frangos, pesos_fetos_frangos, 3)
funcao_aproximada3 = np.poly1d(poliGrau3)
y_aproximado3 = funcao_aproximada3(idades_frangos)
erro3 = np.linalg.norm(pesos_fetos_frangos - y_aproximado3)

poliGrau4 = np.polyfit(idades_frangos, pesos_fetos_frangos, 4)
funcao_aproximada4 = np.poly1d(poliGrau4)
y_aproximado4 = funcao_aproximada4(idades_frangos)
erro4 = np.linalg.norm(pesos_fetos_frangos - y_aproximado4)

poliGrau5 = np.polyfit(idades_frangos, pesos_fetos_frangos, 5)
funcao_aproximada5 = np.poly1d(poliGrau5)
y_aproximado5 = funcao_aproximada5(idades_frangos)
erro5 = np.linalg.norm(pesos_fetos_frangos - y_aproximado5)

poliGrau6 = np.polyfit(idades_frangos, pesos_fetos_frangos, 6)
funcao_aproximada6 = np.poly1d(poliGrau6)
y_aproximado6 = funcao_aproximada6(idades_frangos)
erro6 = np.linalg.norm(pesos_fetos_frangos - y_aproximado6)

plt.title("Gráfico Comparativo", fontdict = fonte_titulo)
plt.xlabel("Idade (dias)", fontdict = fonte_labels)
plt.xticks(np.arange(5,20,1))
plt.xlim(5,19)

plt.ylabel("Peso (g)", fontdict = fonte_labels)
plt.yticks(np.arange(-1,10,1))
plt.ylim(-1,9)
plt.grid()
plt.plot(idades_frangos, pesos_fetos_frangos, label = "Original")
plt.plot(valores_idades_plot, np.polyval(poliGrau1, valores_idades_plot), label = "Polinomio de Grau 1")
plt.plot(valores_idades_plot, np.polyval(poliGrau2, valores_idades_plot), label = "Polinomio de Grau 2")
plt.plot(valores_idades_plot, np.polyval(poliGrau3, valores_idades_plot), label = "Polinomio de Grau 3")
plt.plot(valores_idades_plot, np.polyval(poliGrau4, valores_idades_plot), label = "Polinomio de Grau 4")
plt.plot(valores_idades_plot, np.polyval(poliGrau5, valores_idades_plot), label = "Polinomio de Grau 5")
plt.plot(valores_idades_plot, np.polyval(poliGrau6, valores_idades_plot), label = "Polinomio de Grau 6")
plt.legend(prop=fonte_legenda, loc='upper left', fancybox=False)
plt.savefig("./Graficos/GraficoParte1_A.png")

print("Erro p1: ")
print(erro1)
print("Erro p2: ")
print(erro2)
print("Erro p3: ")
print(erro3)
print("Erro p4: ")
print(erro4)
print("Erro p5: ")
print(erro5)
print("Erro p6: ")
print(erro6)







