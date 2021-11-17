import math
import sys

x = [1, 2, 3, 4, 5]
y = [1.7, 3, 4, 4.6, 5]

xy = 0
x2 = 0
x3 = 0
x4 = 0
x2py = 0
sumx = 0
sumy = 0
n = len(x)
m = 2

for i in range(len(x)):
    sumx += x[i]
    sumy += y[i]
    xy += x[i] * y[i]
    x2 += x[i] ** 2
    x3 += x[i] ** 3
    x4 += x[i] ** 4
    x2py += ((x[i] ** 2) * y[i])

promy = sumy / len(y)

print("")
print("sumx:", sumx)
print("sumy:", sumy)
print("x2:", x2)
print("x3:", x3)
print("x4:", x4)
print("xy:", xy)
print("x2py:", x2py)
print("promy:", promy)
print("")


def Gauss():
    A = [
        [n, sumx, x2],
        [sumx, x2, x3],
        [x2, x3, x4]
    ]

    B = [sumy, xy, x2py]

    for x in range(len(A)):
        check = 0
        for i in range(len(A[x])):
            if A[x][i] == 0 or A[i][x] == 0:  # Revisa que no haya una fila/columna de 0.
                check += 1

            # print("check:",check) #Revisa que no hayan más de cierta cantidad de 0.
        if check >= len(A):
            print(" ")
            sys.exit('[Error] Fila/columna de ceros!\n\t>>>"No existe solucion"<<<')

    New = A
    for i in range(len(New)):
        New[i].append(B[i])

    def mostrar():
        for i in range(len(New)):
            for x in range(len(A[i])):
                if x != len(A[i]) - 1:
                    print("{:.3f}".format(A[i][x]), end="\t")
                else:
                    print("| \t {:.3f}".format(A[i][x]), end="\t")
            print(" ")
        print(" ")

    def col1(i):
        verificador = i + 1
        while verificador != len(A):
            # print("verificador:", verificador, "len(A):", len(A))
            pivote = A[verificador][i]
            # print("Cambiar columnas.")
            # print("")
            for x in range(len(A[i])):
                # print("{} - ( {} * {} ) = {}".format(A[verificador][x], pivote, A[i][x], A[verificador][x] - pivote * A[i][x]))
                A[verificador][x] = A[verificador][x] - pivote * A[i][x]
                # mostrar()
            verificador += 1
        # print("!!!!!!!!!")

    print("")
    print("[Matriz original]")
    print("")
    mostrar()

    for i in range(len(A)):
        pivote = A[i][i]

        if pivote == 0:
            # print("[0]------------------[0]")
            # print("")
            temp = A[i]
            A[i] = A[i + 1]
            A[i + 1] = temp
            pivote = A[i][i]
            if pivote != 1 or pivote != 0:
                for x in range(len(A[i])):
                    A[i][x] = A[i][x] / pivote
            col1(i)

        elif pivote == 1:
            # print("[1]------------------[1]")
            # print("")
            col1(i)

        elif pivote != 1:
            # print("[!1]------------------[!1]")
            # print("")
            for x in range(len(A[i])):
                A[i][x] = A[i][x] / pivote
                # mostrar()
            col1(i)

    def col2(i):
        verificador = i
        while verificador != -len(A) - 1:
            # print("verificador:", verificador, "len(A):", len(A))
            pivote = A[verificador][i]
            # print("Cambiar columnas.")
            # print("")
            # print("range:",range(len(A[i])-1))
            for x in range(len(A[i])):
                # print("x:",x)
                # print("{} - ( {} * {} ) = {}".format(A[verificador][x], pivote, A[i+1][x], A[verificador][x] - pivote * A[i+1][x]))
                A[verificador][x] = A[verificador][x] - pivote * A[i + 1][x]
                # mostrar()
            verificador -= 1

    for i in range(-2, -len(A) - 1, -1):
        col2(i)

    print("")
    print("RESPUESTA:")
    mostrar()
    return A


A = Gauss()

a0 = A[0][-1]
a1 = A[1][-1]
a2 = A[2][-1]

print(f"{a0 = }")
print(f"{a1 = }")
print(f"{a2 = }")

Sr = 0
St = 0
r = 0

for i in range(len(x)):
    St += (y[i] - promy) ** 2
    Sr += (y[i] - a0 - (a1 * x[i]) - (a2 * (x[i]) ** 2)) ** 2

syDx = math.sqrt((Sr) / (n - (m + 1)))
r = math.sqrt((St - Sr) / St) * 100

print("")
print(f"[Ecuacion final]: y = {a0:.4f} + {a1:.4f}x + {a2:.4f}x^2")
print("Sr:", Sr)
print("St:", St)
print(f"Error estandar: {syDx}")
print(f"r: {r}%")
print("")