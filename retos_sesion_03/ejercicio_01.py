class Atleta:
    comida_preferida = "hamburguesa"

    def __init__(self, nombre, energia=100, fuerza=10):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza
    def entrenar(self):
        if self.energia >= 20:
            self.fuerza += 5
            self.energia -= 20
            print(f"{self.nombre} ha entrenado. Fuerza: {self.fuerza}, Energía: {self.energia}")
        else:
            print(f"{self.nombre} está demasiado cansado para entrenar ")
    def descansar(self):
        self.energia += 15
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nombre} ha descansado. Energía: {self.energia}")
    @classmethod
    def mostrar_comida_preferida(cls):
        print(f"La comida preferida de los atletas es la {cls.comida_preferida}")
    # @staticmethod
    # def motivar():
    #     print("¡Nunca te rindas! ¡El esfuerzo siempre vale la pena!")
    def info(self):
        print(f"Atleta: {self.nombre} | Energía: {self.energia} | Fuerza: {self.fuerza}")


print("Creando atletas...")

atleta1 = Atleta("Carlos", energia=80, fuerza=15)
atleta2 = Atleta("Lucía", energia=90, fuerza=12)

atleta1.info()
atleta2.info()

print("\n--- Entrenamiento ---")
atleta1.entrenar()
atleta2.entrenar()

print("\n--- Descanso ---")
atleta1.descansar()
atleta2.descansar()

print("\n--- Comer ---")
Atleta.mostrar_comida_preferida()
atleta1.energia += 10
atleta2.energia += 10
print(f"{atleta1.nombre} comió una hamburguesa. Energía: {atleta1.energia}")
print(f"{atleta2.nombre} comió una hamburguesa. Energía: {atleta2.energia}")

# print("\n--- Motivación ---")
# Atleta.motivar()
