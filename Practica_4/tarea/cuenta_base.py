from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, titular, cbu, saldo_inicial=0):
        self.titular = titular
        self._cbu = cbu
        self._saldo = saldo_inicial if saldo_inicial >= 0 else 0

    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
        else:
            raise ValueError("El monto a depositar debe ser mayor a cero.")

    def __str__(self):
        return f"[CuentaBancaria] Titular: {self.titular} | CBU: {self.cbu} | Saldo: ${self.saldo}"

    @abstractmethod
    def extraer(self, monto):
        pass
