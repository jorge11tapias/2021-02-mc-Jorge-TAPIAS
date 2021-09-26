import math
#valor = input("Digite el valor para x: ")
valor = 0.62
h = 0.005
def CalcEa(x, y):
    CEa = abs(((x - y)/x) * 100)
    return CEa

def taylor(x, y, z):
    if x == 0:
        respuesta = x
    else:
        respuesta = (signo * (math.e*-x)/math.factorial(z)) * (y*z)
    return respuesta

AproxAc = 0
AproxAn = 0
signo = 1
uwu = 0
Ea = float(100)

while uwu < 15:
    AproxAc = AproxAc + taylor(valor, h, uwu)
    Ea = CalcEa(AproxAc, AproxAn)
    AproxAn = AproxAc
    uwu += 1
    signo = signo * -1
    print("Ea:", Ea)
    print("AproxAc:", AproxAc)

print("\nAproximado:", AproxAc)
print("Valor real:", math.e**-(0.625))
