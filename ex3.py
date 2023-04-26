matrizA = []
listaB = []
listaC = []

for lin in range(0, 4):
    linha = []
    for col in range(0, 5):
        linha.append(int(input("Digite um elemento da matriz: ")))
    matrizA.append(linha)

for lin in range(0, 4):
    soma_linha = 0
    for col in range(0, 5):
        soma_linha+=matrizA[lin][col]
    listaB.append(soma_linha)

print("/n")
print(listaB)
print(listaC)