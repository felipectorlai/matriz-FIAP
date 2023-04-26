listaA = []
matrizC = []

for i in range(10):
    listaA.append(int(input("Digite um elemento da lista: ")))

for i in range(10):
    matrizC[i][0] = listaA[i] + 5
    matrizC[i][1] = listaA[i] + 3
    matrizC[i][2] = listaA[i]++5

for i in range(10):
    print(matrizC[i])