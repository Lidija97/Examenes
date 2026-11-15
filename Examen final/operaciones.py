import random


def generar_numeros(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("La cantidad debe ser un número entero.")

    if n <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    return [random.randint(1, 100) for _ in range(n)]


def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))


def ordenar_numeros(lista):
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    return ascendente, descendente


def mayor_par(lista):
    pares = [numero for numero in lista if numero % 2 == 0]

    if not pares:
        return None

    return max(pares)


def obtener_elemento(lista, posicion):
    if not isinstance(posicion, int) or isinstance(posicion, bool):
        raise TypeError("La posición debe ser un entero.")

    if posicion < 0 or posicion >= len(lista):
        raise IndexError("La posición está fuera del rango.")

    return lista[posicion]
