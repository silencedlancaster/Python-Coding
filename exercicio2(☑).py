#exportando o pi para ser possivel usar seu número
import math

raio = float(input("Digite o valor da raio da circunferência: "))

#calculando o valor da circunferência
comprimento = (2 * math.pi * raio)

print("O valor da circunferência é: ", f"{comprimento:.2f}")