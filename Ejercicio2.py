class CarteraCripto:
    def __init__(self, usuario):
        # Atributos privados
        self.__usuario = usuario
        self.__saldo_btc = 0.0

    # Método para consultar el saldo de Bitcoin
    def consultar_saldo(self):
        return self.__saldo_btc

    # Método para comprar bitcoin
    def comprar_btc(self, monto_usd, precio_actual_btc):
        if monto_usd > 0 and precio_actual_btc > 0:
            cantidad_btc = monto_usd / precio_actual_btc
            self.__saldo_btc += cantidad_btc
            print(f"Has comprado {cantidad_btc:.2f} BTC.") 
        else:
            raise ValueError("El monto en USD y el precio actual deben ser mayores a 0.")

    # Método para vender Bitcoin
    def vender_btc(self, monto_btc, precio_actual_btc):
        if monto_btc > 0 and precio_actual_btc > 0:
            if monto_btc <= self.__saldo_btc:
                monto_usd = monto_btc * precio_actual_btc
                self.__saldo_btc -= monto_btc
                print(f"Has vendido {monto_btc:.2f} BTC y recibido ${monto_usd:.2f}.")
                return monto_usd
            else:
                raise ValueError("No tienes suficiente saldo en BTC para realizar esta venta.")
        else:
            raise ValueError("La cantidad de BTC y el precio actual deben ser mayores a 0.")

try:
    cartera = CarteraCripto("Juan Pérez")

    print(f"Saldo inicial: {cartera.consultar_saldo():.2f} BTC")

    cartera.comprar_btc(10000, 300000)
    print(f"Saldo luego de comprar: {cartera.consultar_saldo():.2f} BTC")

    cartera.vender_btc(0.1, 350000)
    print(f"Saldo luego de vender: {cartera.consultar_saldo():.2f} BTC")

except ValueError as e:
    print(f"Error: {e}")
