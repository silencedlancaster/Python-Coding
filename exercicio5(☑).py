#importando o valor da raiz quadrada para ser possivel usar o seu valor
from math import sqrt

#os valores do primeiro ponto
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))

#os valores do segundo ponto

x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

#calculando a distância
distancia = sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2)

#mostrando o resultado na tela
print("O valor da distância entre esses pontos: ", f"{distancia:.2f}")
