#Colocando valores para a variável "copo1" e "copo2"
copo1 = "laranja"
copo2 = "acerola"

#Fazer aparecer uma mensagem mostrando as variáveis antes da troca
#Mostrando o valor da variável de "copo1" e "copo2" originalmente
print("Os sucos antes da troca de copos: ")
print("O suco do primeiro copo: ", copo1)
print("O suco do segundo copo: ", copo2)

#O valor da troca vai receber o valor que está em "copo1"
#O "copo1", que está sem valor, recebera o valor da variável "copo2"
#A variável "copo2", que está sem valor, vai receber o valor da variável troca
troca = copo1
copo1 = copo2
copo2 = troca

#Aparecerá uma mensagem na tela mostrando o valor atual da variáveis depois da troca
print("Os sucos depois da troca: ")
print("O suco do primeiro copo: ", copo1)
print("O suco do segundo copo: ", copo2)