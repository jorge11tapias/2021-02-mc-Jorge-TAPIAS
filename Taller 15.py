import sys

A = [
    [3, 1, 1],
    [1, 0, -3],
    [5, 2, -5]
]

B = []

for i in range(len(A)):
    B.append([0])


for i in range(len(A)):
    for x in range(len(A[i])-1):
        B[i].append(0)


for i in range(len(A)):
    for x in range(len(A[i])):
        if i == x:
            B[i][x] = 1
        else:
            B[i][x] = 0

for x in range(len(A)):
    check = 0
    for i in range(len(A[x])):
        if A[x][i] == 0 or A[i][x] == 0: 
            check += 1
    if check >= len(A):
        print(" ")
        sys.exit('[Error] Fila/columna de ceros!\n\t>>>"No existe solucion"<<<')

New = A
for i in range(len(New)):
    for x in range(len(New[i])):
        New[i].append(B[i][x])

def mostrar():
    for i in range(len(New)):
        for x in range(len(A[i])):
            if x != len(A[i])-(len(B[i])):
                print("{:.3f}".format(A[i][x]), end="\t")
            else: print("| \t {:.3f}".format(A[i][x]), end="\t")
        print(" ")
    print(" ")

def col1(i):
    verificador = i+1
    while verificador != len(A):
        #print("verificador:", verificador, "len(A):", len(A))
        pivote = A[verificador][i]
        print("Cambiar columnas.")
        print("")
        for x in range(len(A[i])):
            print("{} - ( {} * {} ) = {}".format(A[verificador][x], pivote, A[i][x], A[verificador][x] - pivote * A[i][x]))
            A[verificador][x] = A[verificador][x] - pivote * A[i][x]
            mostrar()
        verificador += 1
    #print("!!!!!!!!!")
    


print("")
print("[Matriz original]")
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
        pivote = A[verificador][uwu]
        print("verificador:", verificador,"i:",i, "uwu:",uwu, "pivote:",pivote, "len(A):", len(A))
        print("Cambiar columnas.")
        print("")
        for x in range(-len(A[i]), 0):
            var1 = A[verificador][x]
            var2 = pivote
            var3 = A[i+1][x]
            var4 = var1 - (var2 * var3)
            print("{} - ( {} * {} ) = {}".format(var1, var2, var3, var4))
            A[verificador][x] = var4
            mostrar()
        #print("uwu")
        verificador -= 1

uwu = len(A)
print("!!!uwu:",uwu)
for i in range(-2, -len(A)-1, -1):
    uwu -= 1
    col2(i)


print("")
print("RESPUESTA:")
mostrar()
