class Trabajador:
    # Clase base para los trabajadores de la empresa
    def __init__(self, nombre_completo, salario_inicial): # método constructor
        self.nombre = nombre_completo
        self._salario = salario_inicial

    @property
    def salario(self): # getter
        return self._salario

    @salario.setter
    def salario(self, nuevo_salario): 
        if nuevo_salario >= 0:
            self._salario = nuevo_salario
        else:
            print("El salario debe ser un valor positivo.")

    def calcular_pago(self): # Método que retorna el salario base
        return self._salario

#herencia
class EmpleadoDePlanta(Trabajador):
    def calcular_pago(self):
        # Los empleados de planta reciben una bonificación de 2500
        return self.salario + 2500

#herencia
class EmpleadoPartTime(Trabajador):
    def __init__(self, nombre_completo, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre_completo, tarifa_por_hora)
        self.horas_laboradas = horas_trabajadas

    def calcular_pago(self):
        # El pago de los empleados a tiempo parcial se calcula por horas trabajadas
        return self.salario * self.horas_laboradas

#herencia
class EmpleadoContratado(Trabajador):
    def calcular_pago(self):
        # Lo empleados contratados tienen una deducción de $800 en su pago
        return self.salario - 800

#Ejemplo
personal = [
    EmpleadoDePlanta("Carlos López", 3200),
    EmpleadoPartTime("Laura Vargas", 22, 150),
    EmpleadoContratado("Andrés Pérez", 2800)
]

for miembro in personal:
    print("Nombre:", miembro.nombre)
    print("Pago calculado:", miembro.calcular_pago())
    print("------")