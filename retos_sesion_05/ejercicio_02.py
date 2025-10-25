class Nadador:
    def nadar(self):
        print(" Este personaje se está desplazando en el agua.")

class Volador:
    def volar(self):
        print(" Este personaje se está desplazando por el aire.")

class Pez(Nadador):
    def mostrar(self):
        print(" Soy un Pez y puedo nadar.")
        self.nadar()

class Pajaro(Volador):
    def mostrar(self):
        print(" Soy un Pájaro y puedo volar.")
        self.volar()

class Pato(Nadador, Volador):
    def mostrar(self):
        print(" Soy un Pato, puedo nadar y volar.")
        self.nadar()
        self.volar()


pez = Pez()
pajaro = Pajaro()
pato = Pato()

print("Personajes en acción")
pez.mostrar()
print()
pajaro.mostrar()
print()
pato.mostrar()
