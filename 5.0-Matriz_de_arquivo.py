with open('matriz.txt', 'r') as f:
    matriz = [[int(num) for num in line.split(' ')] for line in f]
    
    '''for line in f:
         if (line.strip() == ""):
            print (entrou)
            matriz2 = [[int(num) for num in line.split(' ')]for line in f]
    '''
print(matriz)
print(matriz2)
    