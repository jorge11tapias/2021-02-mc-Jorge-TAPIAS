import math
valorRad = int(input("Digite el valor en radianes: "))
Cs = 8    #Cifras significativas#
Es = float((0.5 * 10 ** -Cs) * 100) ##Error esperado##
print("Es: ", Es)
Ea = float(100) ##Error aproximado##
def CalcEa(x, y):  ##Función para hallar el error aproximado##
    CEa = abs(((x - y) / x) * 100)
    return CEa
expoFacto = 0   ## Numero factorial##
AproxAc = 0     ## Aproximado actual      ##
AproxAn = 0     ## Aproximado anterior      ##
Signo = 1       ## Intercalar signo en la ecuación cos x     ##
while Ea > Es:
    AproxAc = AproxAc + Signo * (valorRad ** expoFacto) / math.factorial(expoFacto)
    Ea = CalcEa(AproxAc, AproxAn)
    AproxAn = AproxAc
    Signo = Signo * -1
    expoFacto += 2

print(AproxAc)
