import pip
import os
import sys
import sympy

def limpiar():
    os.system("cls")


xi = [0, 1, 2, 3]
fi = [4, 5, 2, 1]



limpiar()
if len(xi) != len(fi):
    print("")
    sys.exiit("\t[ERROR]: La longitud de xi y fi son diferentes.")

limpiar()

print("")
print("Taller 22 - Interpolación.")
print("")

#/////////////////////////////////////////////////////////
# Verificador de que todo está correcto.

breaker = False

while True:

    if breaker == True:
        break
    breaker = False

    f = float(input("\tValor a buscar (fx): "))
    n = int(input("\tn?: "))
    

    if n < len(xi):

        for i in range(len(xi)):

            if xi[i] == f:
                limpiar()
                print("")
                print(f"\t[ERROR]: El valor de f ({f}) ya se encuentra en xi: [{xi[i]} : {fi[i]}]")
                break

            elif breaker == True:
                break

            else:
                breaker = True
                for i in range(len(xi)-1):
                    if xi[i] < f < xi[i+1]:
                        #print("")
                        #print(f"Te encontré: {xi[i]} < {f} < {xi[i+1]}")
                        break

    else: limpiar(), print(f"\t[ERROR]: El valor de n ({n}) necesita al menos {n+1} variables en xi.")

#/////////////////////////////////////////////////////////
# Fin verificador.



#/////////////////////////////////////////////////////////
#Función para instalar la libreria: Sympy.

def install(package):
    try:
        pip.main(['install', "pip", '--upgrade', "-q"]) #Actualizar pip a la última versión
        pip.main(['install', package, "-q"]) #Instalar Sympy
    except Warning:
        print("Instalando librerias.")

if __name__ == '__main__':
    try:
        import sympy
    except (ImportError, Warning):
        install('SymPy')
        import sympy
#/////////////////////////////////////////////////////////

x = sympy.Symbol("x")
#n = 2
#f = 1.5

z = n
breaker = ""
for i in range(len(xi)-n):
    if breaker == "break":
        break
    temp = []
    z -= n
    for j in range(n+1):
        temp.append(xi[z])  
        z += 1
    for i in range(len(temp)-1):
        if temp[i] < f < temp[i+1]:
            #print("Encontrado!!!")
            #print(f"{temp[i]} < {f} < {temp[i] + 1}")
            print(f"Valores tomados: {temp}") 
            breaker = "break"
            break



xi = temp
for i in range(len(xi)):
    fi[i] = fi[xi[i]]
    

def fn():
    suma = 0
    for i in range(n+1):
        suma += Li(i) * fi[i]
    return suma
        

def Li(i):
    Lix = 1
    for j in range(n+1):
        if j != i:
            Lix *= (x - xi[j])/(xi[i] - xi[j])
    return Lix


print(f"Fn({x}): {fn()}")
x = f
print(f"Fn({x}): ({x}, {fn()})")