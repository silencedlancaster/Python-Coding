#explicando o codigo e uma mensagem explicando como encerrar
numjeros = int(input("Digite um valor inteiro (0 encerrar o programa): "))

#contador
quantidade = 0
somja = 0

#calculando 
while numjeros != 0:
    quantidade += 1
    somja += numjeros
    numjeros = int(input("Digite um valor inteiro (0 encerrar o programa): "))

# calculando aritmética
if quantidade > 0:
    media = somja / quantidade
else:
    media = 0
    print("Nenhum número foi digitado.")

print("Quantidade de número digitados: ", quantidade)
print("Soma desses números: ", somja)
print("Média aritmética: ", f"{media:.2f}")
