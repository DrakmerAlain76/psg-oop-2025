class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def __str__(self):
        return f"{self.nombre} → destino: {self.destino}"


class Minibus:
    def __init__(self, numero_ruta, paradas):
        self._numero_ruta = numero_ruta
        self._paradas = paradas
        self._pasajeros = []
        self._direccion = 1  
        self._indice_actual = 0

    def parada_actual(self):
        return self._paradas[self._indice_actual]

    def avanzar(self):
        """Mueve el minibús a la siguiente parada, invirtiendo sentido si es necesario."""
        self._indice_actual += self._direccion

        
        if self._indice_actual >= len(self._paradas):
            self._direccion = -1
            self._indice_actual = len(self._paradas) - 2

        elif self._indice_actual < 0:
            self._direccion = 1
            self._indice_actual = 1

        print(f"🚌 Avanzando a la parada: {self.parada_actual()}")
        self.bajar_pasajeros()

    def subir_pasajero(self, pasajero):
        """Permite subir a un pasajero solo si su destino está en las paradas."""
        if pasajero.destino in self._paradas:
            self._pasajeros.append(pasajero)
            print(f"🧍 {pasajero.nombre} ha subido. Destino: {pasajero.destino}")
        else:
            print(f"❌ {pasajero.nombre} no puede subir. Destino no válido.")

    def bajar_pasajeros(self):
        """Bajan los pasajeros cuyo destino coincide con la parada actual."""
        parada = self.parada_actual()
        bajan = [p for p in self._pasajeros if p.destino == parada]
        if bajan:
            for p in bajan:
                print(f"🚪 {p.nombre} ha bajado en {parada}.")
                self._pasajeros.remove(p)
        else:
            print(f"🚏 Nadie baja en {parada}.")

    def mostrar_estado(self):
        print(f"\n🚌 Minibus Ruta {self._numero_ruta}")
        print(f"📍 Parada actual: {self.parada_actual()}")
        if self._pasajeros:
            print("👥 Pasajeros a bordo:")
            for p in self._pasajeros:
                print(f"   - {p}")
        else:
            print("🚫 No hay pasajeros a bordo.")



paradas = ["Arce", "Prado", "Perez", "Mariscal", "20 de Octubre"]
bus = Minibus(42, paradas)

p1 = Pasajero("Ana", "Perez")
p2 = Pasajero("Luis", "20 de Octubre")
p3 = Pasajero("Marta", "Central")  

bus.subir_pasajero(p1)
bus.subir_pasajero(p2)
bus.subir_pasajero(p3)

bus.mostrar_estado()


for _ in range(8):
    bus.avanzar()
    bus.mostrar_estado()
