with open('/Users/cezar/Documents/PO/Atividade_de_Revisao_2/matriz_grafo', 'r') as f:
    matriz = [[int(num) for num in line.split(' ')] for line in f]

print ("Matriz de adjacência: ", matriz)

aux = 0
for i in range(len(matriz)):
    aux = 0
    for j in range(len(matriz)):
        if (matriz[i][j] != 0):
            aux += 1
    print ("Grau de", i,":", aux)
