
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def obtener_nombre(self):
        return self.__nombre

    def mostrar_datos(self):
        print("Nombre:", self.obtener_nombre())
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def impuesto(self):
        if self.sueldo > 4500:
            return self.sueldo * 0.09
        else:
            return 0

    def manejo_diccionario(self):
        return {
            "nombre": self.obtener_nombre(),
            "edad": self.edad,
            "sueldo": self.sueldo,
            "impuesto": self.impuesto()
        }

    def generar_archivo_empleado(self):
        with open("empleados.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{self.obtener_nombre()},"
                f"{self.sueldo:.2f},"
                f"{self.impuesto():.2f}\n"
            )


def leer_archivo_empleados():
    print("\nRegistros guardados en empleados.txt:")

    try:
        with open("empleados.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("El archivo empleados.txt no existe.")


def solicitar_nombre():
    while True:
        nombre = input("Ingrese el nombre: ").strip()

        if nombre:
            return nombre
        else:
            print("Error: el nombre no puede estar vacío.")


def solicitar_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))

            if edad > 0:
                return edad
            else:
                print("Error: la edad debe ser mayor que cero.")

        except ValueError:
            print("Error: ingrese una edad válida.")


def solicitar_sueldo():
    while True:
        try:
            sueldo = float(input("Ingrese el sueldo: "))

            if 0 < sueldo < float("inf"):
                return sueldo
            else:
                print("Error: el sueldo debe ser mayor que cero.")

        except ValueError:
            print("Error: ingrese un sueldo numérico válido.")


def registrar_empleados():
    empleados = []

    while True:
        print("\n--- Registro de empleado ---")

        nombre = solicitar_nombre()
        edad = solicitar_edad()
        sueldo = solicitar_sueldo()

        empleado = Empleado(nombre, edad, sueldo)

        print("\nDatos del empleado:")
        empleado.mostrar_datos()
        print(f"Sueldo: S/ {empleado.sueldo:.2f}")
        print(f"Impuesto: S/ {empleado.impuesto():.2f}")

        datos = empleado.manejo_diccionario()
        empleados.append(datos)

        empleado.generar_archivo_empleado()

        continuar = input(
            "\n¿Desea registrar otro empleado? (s/n): "
        ).strip().lower()

        if continuar != "s":
            break

    print("\nLista de empleados registrados:")

    for empleado in empleados:
        print(empleado)

    leer_archivo_empleados()


if __name__ == "__main__":
    registrar_empleados()
