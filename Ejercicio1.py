class Estudiante:
    def __init__(self, nombre, codigo):
        self.__nombre = None        # atributos privados
        self.__codigo = None
        self.__notas = []
        
        # setter para inicializar
        self.nombre = nombre
        self.codigo = codigo

    # Propiedad pa el nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip():  # Validar que el valor no esté vacio
            self.__nombre = valor
        else:
            raise ValueError("El nombre no puede estar vacío.")

    # Property para el codigo
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if valor.isalnum():
            self.__codigo = valor
        else:
            raise ValueError("El código debe ser alfanumérico.")

    # Metodo para que se agreguen las notas
    def agregar_nota(self, nota):
        if 0.0 <= nota <= 5.0:  # establecer el rango de las notas
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")

    # Método para calcular el promedio
    def calcular_promedio(self):
        if self.__notas:  # Verificar que existan notas
            return sum(self.__notas) / len(self.__notas)
        return 0.0

    # Método para determinar si el estudiante aprobó o no
    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0

try:
    estudiante = Estudiante("Anibal conrado", "ASD584")
    estudiante.agregar_nota(3)
    estudiante.agregar_nota(3.5)
    estudiante.agregar_nota(5)

    estudiante1 = Estudiante("Sofia vergara", "AHF544")
    estudiante1.agregar_nota(1)
    estudiante1.agregar_nota(2.5)
    estudiante1.agregar_nota(3)

    print(f"Nombre: {estudiante.nombre}")
    print(f"Código: {estudiante.codigo}")
    print(f"Promedio de notas: {estudiante.calcular_promedio():.2f}")
    print(f"¿aprobó? {'Sí' if estudiante.es_aprobado() else 'No'}")


    print(f"Nombre: {estudiante1.nombre}")
    print(f"Código: {estudiante1.codigo}")
    print(f"Promedio de notas: {estudiante1.calcular_promedio():.2f}")
    print(f"¿aprobó? {'Sí' if estudiante1.es_aprobado() else 'No'}")

except ValueError as e:
    print(f"Error: {e}")