from operaciones import (
    generar_numeros,
    eliminar_duplicados,
    ordenar_numeros,
    mayor_par,
    obtener_elemento
)


def ejecutar_prueba(cantidad):
    print(f"\n=== PRUEBA CON {cantidad} NÚMEROS ===")

    try:
        numeros = generar_numeros(cantidad)

        print("Lista original:", numeros)

        sin_duplicados = eliminar_duplicados(numeros)
        print("Lista sin duplicados:", sin_duplicados)

        ascendente, descendente = ordenar_numeros(numeros)
        print("Orden ascendente:", ascendente)
        print("Orden descendente:", descendente)

        par = mayor_par(numeros)

        if par is None:
            print("No existen números pares.")
        else:
            print("Mayor número par:", par)

        print("Elemento en posición 0:",
              obtener_elemento(numeros, 0))

        try:
            obtener_elemento(numeros, 1000)
        except IndexError as error:
            print("Error de posición:", error)

    except (ValueError, TypeError) as error:
        print("Error:", error)


# PRUEBAS OBLIGATORIAS
ejecutar_prueba(10)
ejecutar_prueba(15)

print("\n=== PRUEBA DE CANTIDAD INVÁLIDA ===")
ejecutar_prueba(-5)

