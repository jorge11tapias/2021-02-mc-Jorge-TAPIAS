import math
valorRad = int(input("Por favor ingrese el valor radian: "))
Contador = 0
Cs = 8     #Cifras significativas#
Es = float((0.5 * 10 ** -Cs) * 100) ##Error esperado##
print("El numero que digito es : ", Es)
Ea = float(100) ##Error aproximado##
def CalcEa(x, y):  ##Función para hallar el error aproximado##
    CEa = abs(((x - y) / x) * 100)
    return CEa
expoFacto = 0   ## Numero factorial##
AproxAc = 0     ## Aproximado actual      ##
AproxAn = 0     ## Aproximado anterior      ##
Signo = 1       ## Intercalar signo en la ecuación cos x     ##
while Ea > Es:
    Contador += 1
    AproxAc = AproxAc + Signo * (valorRad ** expoFacto) / math.factorial(expoFacto)
    Ea = CalcEa(AproxAc, AproxAn)
    AproxAn = AproxAc
    Signo = Signo * -1
    expoFacto += 2
print ("El resultado del valor actual es :",AproxAc)
print ("El resultado del error aproximado es :",Ea *100, "%")
print ("El numero total de iteraciones es de :",Contador)

