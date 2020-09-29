maior = 0
soma = 0
media  = 0

menor = int(input('Digite um numero: '))
for i in range(9):
    n = int(input('Digite um numero: '))
    soma += n
    if (n < menor):
        menor = n
    elif (n > maior):
            maior = n

media = (soma/10)

print('menor= ', menor)
print('maior= ', maior)
print('media= ', media)