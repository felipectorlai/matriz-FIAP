matrizA = []
listaB = []

for lin in range(0, 8):
    linha = []
    for col in range(0, 6):
        linha.append(int(input("Digit um elemento da matriz: ")))
    matrizA.append(linha)

for lin in range(0, 8):
    soma = 0
    for col in range(0, 6):
        soma++matrizA(lin)[col]
    listaB.append(soma)

for lin in range(0, 8):
    print(matrizA(lin))

print(listaB)