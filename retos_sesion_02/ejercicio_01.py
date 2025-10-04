# Ejercicio 1 - Clase Animal
# Un zoológico quiere llevar un registro de los animales que llegan 
# a sus instalaciones.
# Necesitan registrar su especie, tipo y lugar donde los encontraron.
# Los animales del zoológico pueden ser mamíferos, reptiles o aves.
# El origen de todos los animales es "feral". 
# Este zoológico cuenta con 2 mamíferos, 1 reptil y 1 ave

# - Realiza el análisis y diseño de la clase Animal
# - Escribe el codigo en Python para crear la clase Animal
# - Instancia los 4 animales con sus respectivos atributos 

class Animal:
    origen = "feral"
    def __init__(self, especie, tipo, lugar):
        self.especie = especie
        self.tipo = tipo
        self.lugar = lugar

print("Animales registrados en el zoológico")

mamifero1 = Animal("León", "mamífero", "Sabana africana")
mamifero2 = Animal("Oso pardo", "mamífero", "Bosques europeos")
reptil1 = Animal("Cocodrilo del Nilo", "reptil", "Río Nilo")
ave1 = Animal("Águila real", "ave", "Montañas rocosas")

print("Mamífero 1:", mamifero1.origen, mamifero1.especie, mamifero1.tipo, mamifero1.lugar)
print("Mamífero 2:", mamifero2.origen, mamifero2.especie, mamifero2.tipo, mamifero2.lugar)
print("Reptil:", reptil1.origen, reptil1.especie, reptil1.tipo, reptil1.lugar)
print("Ave:", ave1.origen, ave1.especie, ave1.tipo, ave1.lugar)
