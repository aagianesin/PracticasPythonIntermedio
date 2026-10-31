from tarea.cuenta_base import CuentaBancaria

class CuentaCheque(CuentaBancaria):
    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        total_a_descontar = monto + self.costo_emision
        if 0 < total_a_descontar <= self._saldo:
            self._saldo -= total_a_descontar
            print(f"Extracción exitosa de ${monto} (Comisión: ${self.costo_emision}) en Cuenta Cheque de {self.titular}.")
        else:
            print(f"Fondos insuficientes en Cuenta Cheque de {self.titular} para cubrir monto + comisión.")

    def __str__(self):
        return f"[Cuenta Cheque] Titular: {self.titular} | CBU: {self.cbu} | Saldo: ${self.saldo} (Comisión fija: ${self.costo_emision})"
