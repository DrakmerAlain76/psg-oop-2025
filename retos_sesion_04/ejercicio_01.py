class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0.0):
        self.__numero_cuenta = numero_cuenta   # atributo privado
        self.__saldo = saldo_inicial           # atributo privado
        self.titular = titular                 # atributo público

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        if isinstance(nuevo_titular, str) and nuevo_titular.strip():
            self.__titular = nuevo_titular
        else:
            print(" El nombre del titular debe ser una cadena no vacía.")

    def deposito(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f" Depósito exitoso de Bs.{monto:.2f}. Saldo actual: Bs.{self.__saldo:.2f}")
        else:
            print(" El monto del depósito debe ser positivo.")

    def retiro(self, monto):
        if monto <= 0:
            print(" El monto del retiro debe ser positivo.")
        elif monto > self.__saldo:
            print(f" Fondos insuficientes. Saldo disponible: Bs.{self.__saldo:.2f}")
        else:
            self.__saldo -= monto
            print(f" Retiro exitoso de Bs.{monto:.2f}. Saldo restante: Bs.{self.__saldo:.2f}")

    def mostrar_info(self):
        print(f"Cuenta Nº: {self.__numero_cuenta} | Titular: {self.__titular} | Saldo: Bs.{self.__saldo:.2f}")


print("Creando cuentas bancarias...\n")

cuenta1 = Cuenta("001-12345", "Juan Pérez", 500)
cuenta2 = Cuenta("002-67890", "María Gómez", 1000)

cuenta1.mostrar_info()
cuenta2.mostrar_info()

print("\n--- Operaciones ---")
cuenta1.deposito(200)
cuenta2.retiro(300)

print("\n--- Consultas ---")
print("Número de cuenta de Juan:", cuenta1.numero_cuenta)
print("Saldo actual de María:", cuenta2.saldo)

print("\n--- Cambio de titular ---")
cuenta1.titular = "Juan P. Ramírez"
cuenta1.mostrar_info()

try:
    cuenta1.__saldo = 99999
except AttributeError:
    print(" No se puede modificar el saldo directamente (atributo privado).")
