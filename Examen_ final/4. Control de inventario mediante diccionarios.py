# SISTEMA DE CONTROL DE INVENTARIO

# Diccionario con cuatro productos
inventario = {
    "P001": {
        "nombre": "Laptop",
        "precio": 2500,
        "cantidad": 5
    },
    "P002": {
        "nombre": "Mouse",
        "precio": 50,
        "cantidad": 20
    },
    "P003": {
        "nombre": "Teclado",
        "precio": 120,
        "cantidad": 10
    },
    "P004": {
        "nombre": "Monitor",
        "precio": 800,
        "cantidad": 8
    }
}


# Mostrar todos los productos
def mostrar_inventario():
    print("\n=== INVENTARIO DE PRODUCTOS ===")

    for codigo, producto in inventario.items():
        print(f"\nCódigo: {codigo}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: S/ {producto['precio']:.2f}")
        print(f"Cantidad disponible: {producto['cantidad']}")


# Registrar una compra
def realizar_compra(codigo, cantidad):
    print("\n=== REGISTRO DE COMPRA ===")

    if codigo not in inventario:
        print("Error: El producto no existe.")
        return

    if not isinstance(cantidad, int) or isinstance(cantidad, bool):
        print("Error: La cantidad debe ser un número entero.")
        return

    if cantidad <= 0:
        print("Error: La cantidad debe ser mayor que cero.")
        return

    producto = inventario[codigo]

    if cantidad > producto["cantidad"]:
        print("Error: Stock insuficiente.")
        return

    importe = producto["precio"] * cantidad

    producto["cantidad"] -= cantidad

    print("Compra realizada correctamente.")
    print(f"Producto: {producto['nombre']}")
    print(f"Cantidad comprada: {cantidad}")
    print(f"Importe total: S/ {importe:.2f}")

    return importe


# Calcular el valor monetario del inventario
def calcular_valor_inventario():
    valor_total = 0

    for producto in inventario.values():
        valor_total += (
            producto["precio"] * producto["cantidad"]
        )

    return valor_total


# PRUEBAS OBLIGATORIAS

# 1. Mostrar inventario inicial
print("\n=== PRUEBA 1: INVENTARIO INICIAL ===")
mostrar_inventario()

# 2. Realizar una compra válida
print("\n=== PRUEBA 2: COMPRA VÁLIDA ===")
realizar_compra("P001", 2)

# 3. Intentar comprar un producto inexistente
print("\n=== PRUEBA 3: PRODUCTO INEXISTENTE ===")
realizar_compra("P999", 1)

# 4. Intentar comprar más unidades que el stock
print("\n=== PRUEBA 4: STOCK INSUFICIENTE ===")
realizar_compra("P002", 50)

# 5. Mostrar inventario actualizado
print("\n=== PRUEBA 5: INVENTARIO ACTUALIZADO ===")
mostrar_inventario()

# 6. Mostrar valor monetario total
print("\n=== VALOR TOTAL DEL INVENTARIO ===")
valor = calcular_valor_inventario()
print(f"Valor monetario total: S/ {valor:.2f}")
