#ecuaciones de potencias y razon de crecimiento
#Taller 18- Presentado por : Jorge Enrique Tapias Barragan  
import math
def minimosCuadrados(x, y):
    A = [x,y]
    n = len(A[0])
    sumX = 0.0
    sumY = 0.0
    sumXY = 0.0
    sumX2 = 0.0
    for i in range(n):
        
        sumX += A[0][i]
        sumY += A[1][i]
        sumXY += (A[0][i]*A[1][i])
        sumX2 += (A[0][i]*A[0][i])
    
    promX = sumX/n
    promY = sumY/n
    
    #formulita

    a1 = (n*sumXY-sumX*sumY)/(n*sumX2-pow(sumX,2))
    a0 = promY - a1*promX
    
    #respuesta
    print(f"respuesta :y = {a0} + {a1}x")

def exponencial(x, y):
    lnY = [0 for i in range(len(y))]

    #Crear lista de lnY
    for i in range(len(y)):
        lnY[i] = math.log(y[i])
    
    A = [x,lnY]
    n = len(A[0])
    sumX = 0.0
    sumlnY = 0.0
    sumXlnY = 0
    sumX2 = 0.0

    for i in range(n):
        
        sumX += A[0][i]
        sumlnY += A[1][i]
        sumXlnY += (A[0][i]*A[1][i])
        sumX2 += (A[0][i]*A[0][i])
    
    promX = sumX/n
    promlnY = sumlnY/n
    
    #formulita
    a1 = (n*sumXlnY-sumX*sumlnY)/(n*sumX2-pow(sumX,2))
    a0 = promlnY - a1*promX

    #alpha
    alpha = math.exp(a0)

    print(f"respuesta :y = {alpha}*e^({a1}x)")

def ecuacionesPotencias(x, y):
    logY = [0 for i in range(len(y))]
    logX = [0 for i in range(len(x))]

    #Crear lista de logX
    for i in range(len(x)):
        logX[i] = math.log(x[i], 10)

    #Crear lista de logY
    for i in range(len(y)):
        logY[i] = math.log(y[i], 10)
    
    A = [logX,logY]
    n = len(A[0])
    sumlogX = 0.0
    sumlogY = 0.0
    sumlogXlogY = 0
    sumlogX2 = 0.0

    for i in range(n):
        
        sumlogX += A[0][i]
        sumlogY += A[1][i]
        sumlogXlogY += (A[0][i]*A[1][i])
        sumlogX2 += (A[0][i]*A[0][i])
    
    promlogX = sumlogX/n
    promlogY = sumlogY/n
    
    #formulita
    a1 = (n*sumlogXlogY-sumlogX*sumlogY)/(n*sumlogX2-pow(sumlogX,2))
    a0 = promlogY - a1*promlogX

    #alpha
    alpha = pow(10,a0)

    print(f"respuesta :y = {alpha}*x^({a1})")

def razonDeCrecimiento(x, y):
    Yinv = [0 for i in range(len(y))]
    Xinv = [0 for i in range(len(x))]

    #Crear lista de Xinv
    for i in range(len(x)):
        Xinv[i] = 1/x[i]

    #Crear lista de Yinv
    for i in range(len(y)):
        Yinv[i] = 1/y[i]
    
    A = [Xinv,Yinv]
    n = len(A[0])
    sumXinv = 0.0
    sumYinv = 0.0
    sumXinvYinv = 0
    sumXinv2 = 0.0

    for i in range(n):
        
        sumXinv += A[0][i]
        sumYinv += A[1][i]
        sumXinvYinv += (A[0][i]*A[1][i])
        sumXinv2 += (A[0][i]*A[0][i])
    
    promXinv = sumXinv/n
    promYinv = sumYinv/n
    
    #formulita
    a1 = (n*sumXinvYinv-sumXinv*sumYinv)/(n*sumXinv2-pow(sumXinv,2))
    a0 = promYinv - a1*promXinv

    #alpha
    alpha = 1/a0
    betha = a1/a0

    print(f"respuesta :y = {alpha}*x/({betha}+x)")


def main():
    x = [1,3,5,7,9,11,13,15] #0
    y = [4.1,6.5,7.5,7.9,8.3,8.8,9.1,9.3] #1
    minimosCuadrados(x, y)
    print("-"*80)
    #para este caso, la mas exacta es la exponencial
    exponencial(x, y)
    print("-"*80)
    ecuacionesPotencias(x, y)
    print("-"*80)
    razonDeCrecimiento(x, y)
    print("-"*80)

if __name__ == '__main__':
    main()
