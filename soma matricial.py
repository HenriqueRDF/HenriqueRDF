import time
A = [[2,-1,3],[0,4,6],[-6,10,-5]]
B = [[4,7,-8],[9,3,5],[1,-1,2]]
C = [[0,0,0],[0,0,0],[0,0,0]]

tempo_inicial = time.time()
for i in range(1):
    for i in range(0,3):
        for j in range(0,3):
            C[i][j] = A[i][j] + B[i][j]
tempo_final = time.time()
print("Soma Matricial: \nMatriz C = ",C,"\nTempo de execução = ",tempo_final - tempo_inicial)