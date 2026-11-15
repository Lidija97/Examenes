
from datetime import datetime
from functools import wraps


# Decorador para registrar pedidos
def registrar_pedido(funcion):
    @wraps(funcion)
    def funcion_interna(*args, **kwargs):
        fecha_hora = datetime.now()

        print("\n--- REGISTRO DE PEDIDO ---")
        print("Fecha y hora:",
              fecha_hora.strftime("%d/%m/%Y %H:%M:%S"))

        try:
            resultado = funcion(*args, **kwargs)
            print("Operación realizada correctamente.")
            return resultado

        except ValueError as error:
            print("Error:", error)
            print("La operación no fue procesada.")
            return None

    return funcion_interna


# Calcular total usando *args
@registrar_pedido
def calcular_total(*precios):
    for precio in precios:
        if (isinstance(precio, bool)
                or not isinstance(precio, (int, float))
                or precio <= 0):
            raise ValueError(
                "Todos los precios deben ser numéricos "
                "y mayores que cero."
            )

    return sum(precios)


# Procesar pedidos usando **kwargs
@registrar_pedido
def procesar_pedido(cliente, **productos):
    print("Cliente:", cliente)

    for producto, precio in productos.items():
        if (isinstance(precio, bool)
                or not isinstance(precio, (int, float))
                or precio <= 0):
            raise ValueError(
                f"Precio inválido para el producto: {producto}"
            )

    for producto, precio in productos.items():
        print(f"{producto}: S/ {precio:.2f}")

    return sum(productos.values())


# PRUEBAS OBLIGATORIAS

# Prueba 1: Tres precios
print("\n=== PRUEBA 1: TRES PRECIOS ===")
total1 = calcular_total(15, 20, 35)

if total1 is not None:
    print(f"Total: S/ {total1:.2f}")


# Prueba 2: Seis precios
print("\n=== PRUEBA 2: SEIS PRECIOS ===")
total2 = calcular_total(10, 15, 20, 25, 30, 40)

if total2 is not None:
    print(f"Total: S/ {total2:.2f}")


# Prueba 3: Pedido válido con cuatro productos
print("\n=== PRUEBA 3: PEDIDO VÁLIDO ===")

pedido1 = procesar_pedido(
    "Carlos",
    hamburguesa=25,
    pizza=35,
    gaseosa=8,
    papas=12
)

if pedido1 is not None:
    print(f"Importe total: S/ {pedido1:.2f}")


# Prueba 4: Pedido con precio negativo
print("\n=== PRUEBA 4: PEDIDO INVÁLIDO ===")

pedido2 = procesar_pedido(
    "María",
    pollo=30,
    ensalada=15,
    bebida=-5,
    postre=12
)

if pedido2 is not None:
    print(f"Importe total: S/ {pedido2:.2f}")
