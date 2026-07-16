#importar a raiz quadradad para o seu valor ser usado sladskd
from math import sqrt

numero1 = int(input("Digite o primeiro valor positivo: "))
numero2 = int(input("Digite o segundo valor positivo"))

#o valor ao cubo do segundo numero
cubo = sqrt (numero1) ** 2

#calculando a média geométrica entre o rpimeiro e segundo número
media_geometrica = sqrt (numero1 * numero2)

print("a) O cubo do primeiro número: ", cubo)
print("b) A média geométrica entre o primeiro e o segundo número: ", media_geometrica)
