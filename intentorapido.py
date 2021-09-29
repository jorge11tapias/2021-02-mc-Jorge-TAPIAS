
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

from sympy.matrices import *

