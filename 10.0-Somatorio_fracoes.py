def somatorio(n):
    if(n==1):
        return 1/4
    else:
        return somatorio(n-1) + ((2*n-1)/((-2)**(n+1)))

n = int(input("Digite um número para somar: "))
print ("Resultado:", somatorio(n))