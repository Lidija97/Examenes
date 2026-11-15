
class Vehiculo:
    def __init__(self, marca, modelo, anio=2020):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def actualizar_marca(self, nueva_marca):
        self.marca = nueva_marca

    def actualizar_anio(self, nuevo_anio):
        if nuevo_anio > 0:
            self.anio = nuevo_anio
        else:
            print("Error: El año debe ser mayor que cero.")

    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")


class VehiculoAlquiler(Vehiculo):
    def __init__(self, marca, modelo, codigo,
                 tarifa_diaria, anio=2020):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        self.__tarifa_diaria = 0
        self.actualizar_tarifa(tarifa_diaria)

    def actualizar_tarifa(self, nueva_tarifa):
        if nueva_tarifa > 0:
            self.__tarifa_diaria = nueva_tarifa
        else:
            print("Error: La tarifa debe ser mayor que cero.")

    def aumentar_tarifa(self, porcentaje=10):
        if porcentaje < 0:
            print("Error: El porcentaje no puede ser negativo.")
            return

        self.__tarifa_diaria *= (1 + porcentaje / 100)

    def calcular_descuento(self, dias_alquiler):
        if dias_alquiler <= 0:
            raise ValueError("Los días deben ser mayores que cero.")

        importe = self.__tarifa_diaria * dias_alquiler

        if dias_alquiler < 2:
            descuento = 0.05
        elif dias_alquiler <= 5:
            descuento = 0.10
        else:
            descuento = 0.15

        monto_descuento = importe * descuento
        total_final = importe - monto_descuento

        return importe, monto_descuento, total_final

    def mostrar_alquiler(self, dias_alquiler):
        print("\n--- DATOS DEL VEHÍCULO ---")
        self.mostrar_datos()
        print(f"Código: {self.codigo}")
        print(f"Tarifa diaria: S/ {self.__tarifa_diaria:.2f}")

        importe, descuento, total = self.calcular_descuento(
            dias_alquiler
        )

        print(f"Días de alquiler: {dias_alquiler}")
        print(f"Importe sin descuento: S/ {importe:.2f}")
        print(f"Descuento: S/ {descuento:.2f}")
        print(f"Total final: S/ {total:.2f}")


# PRUEBAS OBLIGATORIAS

# Crear dos vehículos diferentes
vehiculo1 = VehiculoAlquiler(
    "Toyota", "Corolla", "V001", 100, 2022
)

vehiculo2 = VehiculoAlquiler(
    "Hyundai", "Tucson", "V002", 150, 2023
)

# Actualizar marca y año
vehiculo1.actualizar_marca("Toyota")
vehiculo1.actualizar_anio(2024)

# Aplicar dos incrementos consecutivos
print("=== INCREMENTOS DE TARIFA ===")
vehiculo1.aumentar_tarifa()
vehiculo1.aumentar_tarifa(20)

# Calcular descuentos con diferentes días
print("\n=== PRUEBA 1: UN DÍA ===")
vehiculo1.mostrar_alquiler(1)

print("\n=== PRUEBA 2: TRES DÍAS ===")
vehiculo1.mostrar_alquiler(3)

print("\n=== PRUEBA 3: SIETE DÍAS ===")
vehiculo2.mostrar_alquiler(7)

# Intentar asignar una tarifa negativa
print("\n=== PRUEBA DE TARIFA NEGATIVA ===")
vehiculo2.actualizar_tarifa(-50)

# Verificar que la tarifa no cambió
vehiculo2.mostrar_alquiler(2)