class Transporte:
    def tipo_transporte(self):
        pass

class Coche(Transporte):
    def tipo_transporte(self):
        print("Transporte terrestre")


class Avion(Transporte):
    def tipo_transporte(self):
        print("Transporte aéreo")


class Barco(Transporte):
    def tipo_transporte(self):
        print("Transporte marítimo")


Lamborghini = Coche()
Avianca = Avion()
Yate = Barco()

Lamborghini.tipo_transporte()
Avianca.tipo_transporte()
Yate.tipo_transporte()
