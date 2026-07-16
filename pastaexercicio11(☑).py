#pedindo o valor da variável
cpf = input("Digite o seu CPF: ")

#variaveis para tentar calcular o cpf

#verificando se é digito ou letras ou se escreveu mais ou menos de 11 números
if len (cpf) != 11 or not cpf.isdigit():
    print("CPF válido.")
elif cpf == cpf [0] * 11: 
    print("CPF invalido.")
else: 
    numeros = [int(digito) for digito in cpf]
    soma = 0 
    peso = 10

#calculando o primeiro digito
    for numero in numeros [:9]: 
        soma += numero * peso
        peso -= 1
        resto = soma % 11
        if resto < 2: 
         digito1 = 0
        else:
            digito1 = 11 - resto

    # calculando o segundo dígito
    soma = 0
    peso = 11
    for numero in numeros[:10]:
        soma += numero * peso
        peso -= 1

    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if digito1 == numeros[9] and digito2 == numeros[10]:
        print("CPF válido.")
    else:
        print("CPF inválido.")
