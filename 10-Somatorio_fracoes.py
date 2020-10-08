def somatorio(n):
    if(n==1):
        return 1/4
    else:
        return somatorio(n-1) + ((2*n-1)/((-2)**(n+1)))


print (somatorio(3))