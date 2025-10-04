class Vino:
    def __init__(self, nombre, tipo, cepa, anio):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio = anio


class Queso:
    def __init__(self, nombre, variedad, edad, sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad
        self.sal = sal


print("Inventario de la Vinoteca")

vino1 = Vino("Viñero Vitichi Vino tinto", "Tinto", "Cabernet Sauvignon", 2024)
vino2 = Vino("Hacienda Tumusla Vino Blanco", "Blanco", "Chardonnay", 2020)
vino3 = Vino("Vino yureño", "Tinto", "Malbec", 2019)
vino4 = Vino("Cotagaita Vino Cholero", "Rosado", "Grenache", 2020)

queso1 = Queso("Roquefort", "Azul", 12, True)
queso2 = Queso("Gouda", "Semiduro", 6, True)
queso3 = Queso("Mozzarella Montero", "Fresco", 2, False)

print("\nVinos disponibles:")
print("'",vino1.nombre,"'", "-", vino1.tipo, "-", vino1.cepa, "-", vino1.anio)
print("'",vino2.nombre,"'", "-", vino2.tipo, "-", vino2.cepa, "-", vino2.anio)
print("'",vino3.nombre,"'", "-", vino3.tipo, "-", vino3.cepa, "-", vino3.anio)
print("'",vino4.nombre,"'", "-", vino4.tipo, "-", vino4.cepa, "-", vino4.anio)

print("\nQuesos disponibles:")
print(queso1.nombre, "-", queso1.variedad, "-", str(queso1.edad) + " meses", "- Con sal" if queso1.sal else "- Sin sal")
print(queso2.nombre, "-", queso2.variedad, "-", str(queso2.edad) + " meses", "- Con sal" if queso2.sal else "- Sin sal")
print(queso3.nombre, "-", queso3.variedad, "-", str(queso3.edad) + " meses", "- Con sal" if queso3.sal else "- Sin sal")
