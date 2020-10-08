def soma_vetor(vet):
    if(len(vet) == 1):
        return vet[0]
    else:
        return vet[0] + soma_vetor(vet[1:])


vet = [1,1,1,1]
print("Soma do vetor ", vet,":" , soma_vetor(vet))