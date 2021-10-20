import sys

A = [
    [2, 2, 0],
    [3, 3, 4],
    [4, 0, 1]
]

B = [6, 9, 8]



for x in range(len(A)):
    check = 0
    for i in range(len(A[x])):
        if A[x][i] == 0 or A[i][x] == 0: #Revisa que no haya una fila/columna de 0.
            check += 1

        #print("check:",check) #Revisa que no hayan más de cierta cantidad de 0.
    if check >= len(A):
        print(" ")
        sys.exit('[Error] Fila/columna de ceros!\n\t>>>"No existe solucion"<<<')

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
        #print("verificador:", verificador, "len(A):", len(A))
        pivote = A[verificador][i]
        print("Cambiar columnas.")
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
print("RESPUESTA:")
mostrar()