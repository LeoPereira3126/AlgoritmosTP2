import random

def generar_lista(n):
    lista = [random.randint(1, 100) for i in range(n)]
    return lista

def repetidos (a):
    return len(a) != len(set(a))

def unicos(f):
    return list(set(f))


valor = int(input("Ingrese el valor de N: "))
resultado = generar_lista(valor)
print("Lista generada:", resultado)
if repetidos(resultado):
    print("La lista contiene repetidos")
else:
    print("La lista no contiene repetidos")

print()

lista_unica = unicos(resultado)
print(lista_unica)