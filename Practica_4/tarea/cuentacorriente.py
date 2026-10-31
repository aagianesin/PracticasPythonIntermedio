from tarea.cuenta_base import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
        super().__init__(titular, cbu, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if 0 < monto <= (self._saldo + self.limite_descubierto):
            self._saldo -= monto
            print(f"Extracción exitosa de ${monto} en Cuenta Corriente de {self.titular}.")
        else:
            print(f"Extracción rechazada en Cuenta Corriente de {self.titular}: supera el límite de descubierto.")

    def __str__(self):
        return f"[Cuenta Corriente] Titular: {self.titular} | CBU: {self.cbu} | Saldo: ${self.saldo} (Descubierto: ${self.limite_descubierto})"
