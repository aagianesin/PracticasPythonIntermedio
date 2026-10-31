from tarea.cuenta_base import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def extraer(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            print(f"Extracción exitosa de ${monto} en Cuenta Ahorro de {self.titular}.")
        else:
            print(f"Fondos insuficientes en Cuenta Ahorro de {self.titular} para extraer ${monto}.")

    def aplicar_interes(self):
        interes = self._saldo * 0.001
        self._saldo += interes
        print(f"Interés aplicado (${interes:.2f}). Nuevo saldo en Ahorro: ${self._saldo}")

    def __str__(self):
        return f"[Cuenta Ahorro] Titular: {self.titular} | CBU: {self.cbu} | Saldo: ${self.saldo}"
