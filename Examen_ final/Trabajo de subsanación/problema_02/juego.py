import random
from datetime import datetime


def generar_numero():
    return random.randint(1, 40)


def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 40: "))

            if 1 <= numero <= 40:
                return numero
            else:
                print("Error: el número debe estar entre 1 y 40.")

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def comparar_numero(intento, secreto):
    if intento < secreto:
        return "El número secreto es mayor."
    elif intento > secreto:
        return "El número secreto es menor."
    else:
        return "Número correcto."


def anunciar_partida(funcion):
    def envoltura():
        print("Inicio de la partida")
        funcion()
        print("Fin de la partida")

    return envoltura


@anunciar_partida
def adivina():
    secreto = generar_numero()
    intentos = []

    print("\nBienvenido al juego Acierta el número.")
    print("Adivina el número secreto entre 1 y 40.")

    while True:
        intento = pedir_numero()
        intentos.append(intento)

        resultado = comparar_numero(intento, secreto)
        print(resultado)

        if intento == secreto:
            print("\nHas ganado")

            fecha_hora = datetime.now()
            print(
                "Fecha y hora de victoria:",
                fecha_hora.strftime("%d/%m/%Y %H:%M")
            )

            print("Intentos realizados:", intentos)
            print("Cantidad de intentos:", len(intentos))
            break
