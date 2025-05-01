# Encapsulamiento-y-polimorfismo


#Ejercicio 1: Clase Estudiante
Descripcion
Define un estudiante con nombre, código y notas.
Valida que el nombre no esté vacío y el código sea alfanumérico.
Permite agregar notas solo si están entre 0.0 y 5.0.
Calcula el promedio de las notas.
Determina si el estudiante está aprobado (promedio >= 3.0).

#Ejercicio 2: Clase CarteraCripto
Descripcion:
Gestiona un saldo de Bitcoin para un usuario.
Permite consultar el saldo actual en BTC.
Permite comprar BTC con USD al precio actual, validando montos positivos.
Permite vender BTC al precio actual, validando la cantidad y el saldo disponible.

#Ejercicio 3: Clase Empleado
Descripcion
Define un empleado con nombre, rol y clave de acceso cifrada (invertida).
Cifra y descifra la clave utilizando métodos internos.
Permite verificar si una clave ingresada es correcta.
Permite cambiar la clave solo si la clave antigua es correcta.

#Ejercicio 4: Clases Persona, Paciente y Doctor
Descripcion:
Persona: Clase base con nombre, edad (validada > 0) y documento.
Paciente: Hereda de Persona y añade diagnóstico e historial médico. Permite agregar y ver el historial, y ver el diagnóstico.
Doctor: Hereda de Persona y añade especialidad. Permite ver la especialidad y modificar el diagnóstico de un paciente.
