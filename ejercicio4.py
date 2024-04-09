import random

def eliminar_valores(lista, eliminar):
    for valor in eliminar:
        while valor in lista:
            lista.remove(valor)

# Solicitar al usuario el tamaño de la lista
longitud_lista = int(input("Ingrese la longitud de la lista: "))

# Generar lista original con números aleatorios
original = [random.randint(1, 100) for _ in range(longitud_lista)]

# Solicita los valores a eliminar
eliminar = []
while len(eliminar) < 5:
    valor = int(input("Ingrese un valor a eliminar: "))
    eliminar.append(valor)

# Verificar si los datos a eliminar superan el largo de la lista original
if len(eliminar) > longitud_lista:
    print("Error: La cantidad de valores a eliminar excede la longitud de la lista original.")
else:
    print("Lista original:", original)
    print("Valores a eliminar:", eliminar)

    eliminar_valores(original, eliminar)

    print("Lista resultante:", original)
