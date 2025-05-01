class Ciudadano:
    def __init__(self, identificacion, años, id_nacional):
        # Atributos privados
        self.__identificacion = identificacion
        self.__años = None
        self.__id_nacional = id_nacional

        self.años = años

    # Property para obtener nombre
    @property
    def identificacion(self):
        return self.__identificacion

    # Property para obtener edad
    @property
    def años(self):
        return self.__años

    @años.setter
    def años(self, valor):
        if valor > 0:
            self.__años = valor
        else:
            raise ValueError("La edad debe ser un número positivo.")

    # Property para el documento de identidad
    @property
    def id_nacional(self):
        return self.__id_nacional

# herencia
class Cliente(Ciudadano):
    def __init__(self, identificacion, años, id_nacional, estado_actual):
        super().__init__(identificacion, años, id_nacional)
        self.__estado_actual = estado_actual
        self.__registros = []

    def agregar_registro(self, texto):
        self.__registros.append(texto)

    def obtener_registros(self):
        return self.__registros

    def obtener_estado(self):
        return self.__estado_actual

#herencia
class Profesional(Ciudadano):
    def __init__(self, identificacion, años, id_nacional, campo):
        super().__init__(identificacion, años, id_nacional)
        self.__campo = campo

    def obtener_campo(self):
        return self.__campo

    def actualizar_estado(self, cliente, nuevo_estado):
        if isinstance(cliente, Cliente):
            cliente._Cliente__estado_actual = nuevo_estado
            print("Estado del cliente actualizado.")
        else:
            print("Error: solo se puede modificar el estado de un cliente.")


# Ejemplo 
try:
    persona1 = Cliente("Carlos Ruiz", 27, "DNI001122", "Observación médica")
    persona1.agregar_registro("Registro inicial - 28/04/2025")
    persona1.agregar_registro("Seguimiento - 29/04/2025")

    experto1 = Profesional("Dr. Emilio Vargas", 52, "DNI998877", "Cardiología")

    print(f"Cliente: {persona1.identificacion}, Edad: {persona1.años}, ID: {persona1.id_nacional}")
    print(f"Estado actual: {persona1.obtener_estado()}")
    print("Registros:", persona1.obtener_registros())

    experto1.actualizar_estado(persona1, "Estable y en seguimiento")
    print(f"Nuevo estado: {persona1.obtener_estado()}")

    print(f"Profesional: {experto1.identificacion}, Campo: {experto1.obtener_campo()}")

except ValueError as err:
    print(f"Error: {err}")
