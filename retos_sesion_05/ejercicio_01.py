class Vehiculo:
    def __init__(self, velocidad, medio):
        self._velocidad = velocidad     
        self._medio = medio             

    def get_medio(self):
        """Devuelve el medio en el que se desplaza el vehículo."""
        return self._medio

    def set_medio(self, nuevo_medio):
        """Permite modificar el medio de desplazamiento."""
        if nuevo_medio:
            self._medio = nuevo_medio
            print(f" Medio cambiado a: {self._medio}")
        else:
            print(" El medio no puede estar vacío.")

    medio = property(get_medio, set_medio)

    @property
    def velocidad(self):
        """Devuelve la velocidad actual del vehículo."""
        return self._velocidad


    def mostrar_estado(self):
        print(f" Vehículo {self.__class__.__name__} | Medio: {self._medio} | Velocidad: {self._velocidad} km/h")


class Bicicleta(Vehiculo):
    def __init__(self, velocidad, medio="terrestre"):
        super().__init__(velocidad, medio)

    def pedalear(self, incremento):
        """Aumenta la velocidad al pedalear."""
        if incremento > 0:
            self._velocidad += incremento
            print(f" La bicicleta ha acelerado. Nueva velocidad: {self._velocidad} km/h")
        else:
            print(" El incremento debe ser positivo.")


class Avion(Vehiculo):
    def __init__(self, velocidad, medio="aéreo"):
        super().__init__(velocidad, medio)

    def volar(self, incremento):
        """Aumenta la velocidad al volar."""
        if incremento > 0:
            self._velocidad += incremento
            print(f" El avión ha incrementado su velocidad. Nueva velocidad: {self._velocidad} km/h")
        else:
            print(" El incremento debe ser positivo.")


bicicleta = Bicicleta(15)
avion = Avion(200)

print(" Estado inicial ")
bicicleta.mostrar_estado()
avion.mostrar_estado()

print("\n Acciones ")
bicicleta.pedalear(5)
avion.volar(50)

print("\n Cambio de medio ")
bicicleta.set_medio("montaña")
avion.set_medio("espacial")

print("\n Estado final ")
bicicleta.mostrar_estado()
avion.mostrar_estado()
