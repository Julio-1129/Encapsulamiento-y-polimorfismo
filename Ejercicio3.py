class UsuarioSistema:
    def __init__(self, identificador, puesto, password):
        # Atributos privados
        self.__identificador = identificador
        self.__puesto = puesto
        self.__clave_secreta = self.__encriptar(password)

    # Método privado para "encriptar" la clave (reversa)
    def __encriptar(self, texto):
        return texto[::-1]

    # Método privado para "desencriptar" la clave
    def __desencriptar(self, texto_cifrado):
        return texto_cifrado[::-1]

    # Property para obtener el identificador
    @property
    def identificador(self):
        return self.__identificador

    # Property para obtener el puesto
    @property
    def puesto(self):
        return self.__puesto

    # Verifica si una contraseña ingresada coincide con la original
    def autenticar(self, intento_clave):
        clave_real = self.__desencriptar(self.__clave_secreta)
        return intento_clave == clave_real

    # Cambia la clave si se proporciona correctamente la anterior
    def actualizar_clave(self, anterior, nueva):
        if self.autenticar(anterior):
            self.__clave_secreta = self.__encriptar(nueva)
            print("Contraseña actualizada correctamente.")
        else:
            print("Error: la contraseña anterior es incorrecta.")

#Ejemplo
usuario = UsuarioSistema("María López", "Soporte Técnico", "pass789")

print(f"Identificador: {usuario.identificador}")
print(f"Puesto: {usuario.puesto}")

if usuario.autenticar("pass789"):
    print("Autenticación exitosa.")
else:
    print("Falló la autenticación.")

usuario.actualizar_clave("pass789", "claveNueva321")

if usuario.autenticar("claveNueva321"):
    print("Nueva contraseña verificada con éxito.")
else:
    print("La nueva contraseña no coincide.")

