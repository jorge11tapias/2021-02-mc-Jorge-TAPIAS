def definir_vectores ():
    texto_vector_a = input("Escriba los valores para el vector  a sin parentesis y separado por espacios:\n")
    lista_vector_a = list(map(float, texto_vector_a.split()))
    texto_vector_b = input("Escriba los valores para el vector  B sin parentesis y separado por espacios:\n")
    lista_vector_b = list(map(float, texto_vector_b.split()))

    return lista_vector_a,lista_vector_b
def scalar_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("La longitud de los vectores para multiplicarlos debe ser igual")
    return sum([x*y for x,y in zip(v1,v2)])

if __name__ == "__main__":
    a, b = definir_vectores()
    print("el producto escalar es:\n", scalar_product(a, b))
A = [
    [3, 4, 5],
    [5, 7, 8],
    [4, 3, 2]
]

B = [
    [6, 7, 8],
    [1, 2, 3],
    [1, 4, 5]
]

boole = True
vari = 1
uwu = 0
while boole == True:
    print("[OPERACIONES]\n1) 3A\n2) 4B\n3) A+B\n4) BxA")
    xd = int(input("Digite el número de la operación que desea hacer: "))
    print(" -/-/-/-/-\n")

    if xd == 1: 
        for i in range(len(A)):
            for u in range(len(A[i])):
                uwu = 3*A[i][u]
                print(uwu,'\t', end="")
                boole = False
            print("")

    elif xd == 2:
        for i in range(len(B)):
            for u in range(len(B[i])):
                uwu = 4*B[i][u]
                print(uwu,'\t', end="")
                boole = False
            print("")

    elif xd == 3:
        if (len(A)) == (len(B)):
            for x in range(len(A)):
                if len((A)[x]) == len((B)[x]):
                    vari = vari * 1
                else: vari = vari * 0

            if vari == 1:
                for i in range(len(A)):
                    for u in range(len(A[i])):
                        uwu = A[i][u] + B[i][u] 
                        print(uwu, end=" \t")
                        boole = False
                    print("")
            else: print("[Error] Las matrices no tienen las mismas dimensiones.\n")
        else: print("[Error] Las matrices no tienen las mismas dimensiones.\n")

    elif xd == 4:
        for x in range(len(A)):
            if len((A)[x]) == len((B)):
                vari = vari * 1
            else: vari = vari * 0

        if vari == 1:
            uwu = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*B)] for X_row in A]
            for i in range(len(uwu)):
                for u in range(len(uwu[i])):
                    print(uwu[i][u],'\t', end="")
                    boole = False
                print("")
        else: print("[Error] Las matrices no tienen las dimensiones correctas.\n")
    else:
        print("[Error]\n")

