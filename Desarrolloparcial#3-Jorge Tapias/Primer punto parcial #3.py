
##Presentado por Jorge Enrique Tapias Barragan
import sys
A = [
    [2, 1, 4,-4],
    [5, 5, 3,-2],
    [2, 2, -1,0],
    [5,-2,1,0]
]
B = [-1,3,9,11]
for x in range(len(A)):
    check = 0
    for i in range(len(A[x])):
        if A[x][i] == 0 or A[i][x] == 0: 
            check += 1
    if check >= len(A):
        print(" ")
        sys.exit('Vuelva a intentarlo <<<')
New = A
for i in range(len(New)):
    New[i].append(B[i])
def mostrar():
    for i in range(len(New)):
        for x in range(len(A[i])):
            if x != len(A[i])-1:
                print("{:.3f}".format(A[i][x]), end="\t")
            else: print("| \t {:.3f}".format(A[i][x]), end="\t")
        print(" ")
    print(" ")
def col1(i):
    verificador = i+1
    while verificador != len(A):
        pivote = A[verificador][i]
        print("Cambio de columnas")
        print("")
        for x in range(len(A[i])):
            print("{} - ( {} * {} ) = {}".format(A[verificador][x], pivote, A[i][x], A[verificador][x] - pivote * A[i][x]))
            A[verificador][x] = A[verificador][x] - pivote * A[i][x]
            mostrar()
        verificador += 1
print("")
print("[La Matriz original]")
print("")
mostrar()

for i in range(len(A)):
    pivote = A[i][i]

    if pivote == 0:
        print("[0]------------------[0]")
        print("")
        temp = A[i]
        A[i] = A[i+1]
        A[i+1] = temp
        pivote = A[i][i]
        if pivote != 1 or pivote != 0:
            for x in range(len(A[i])):
                A[i][x] = A[i][x]/pivote  
        col1(i)

    elif pivote == 1: 
        print("[1]------------------[1]")
        print("")
        col1(i)

    elif pivote != 1:
        print("[!1]------------------[!1]")
        print("")
        for x in range(len(A[i])):
            A[i][x] = A[i][x]/pivote            
            mostrar()
        col1(i)
def col2(i):
    verificador = i
    while verificador != -len(A)-1:
        pivote = A[verificador][i]
        print("Cambio de columnas")
        print("")
        print("range:",range(len(A[i])-1))
        for x in range(len(A[i])):
            print("x:",x)
            print("{} - ( {} * {} ) = {}".format(A[verificador][x], pivote, A[i+1][x], A[verificador][x] - pivote * A[i+1][x]))
            A[verificador][x] = A[verificador][x] - pivote * A[i+1][x]
            mostrar()
        verificador -= 1
for i in range(-2, -len(A)-1, -1):
    col2(i)
print("")
print("La respuesta del sistema de ecuaciones resuelta por Gauss Jordan es :")
mostrar()
