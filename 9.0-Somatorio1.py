def somatorio(n):
    if(n==1):
        return 2
    else:
        return somatorio(n-1) + n*(n+1)


print (somatorio(5))