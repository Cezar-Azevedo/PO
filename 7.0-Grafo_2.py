with open('/Users/cezar/Documents/PO/Atividade_de_Revisao_2/matriz_grafo', 'r') as f:
    matriz = [[int(num) for num in line.split(' ')] for line in f]

    print ("Matriz de adjacência: ", matriz)
    
    vertice = int(input('Vértice:'))
    for j in range(len(matriz)):
        if (matriz[vertice][j] != 0):
            print (j," é adjacente à ele")
