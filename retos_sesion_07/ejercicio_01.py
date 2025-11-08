class Martillo:
    def __init__(self, mango, material, peso):
        self.mango = mango
        self.material = material
        self.peso = peso

    def usar(self):
        print(" Clavando clavos con fuerza.")


class Destornillador:
    def __init__(self, mango, material, peso):
        self.mango = mango
        self.material = material
        self.peso = peso

    def usar(self):
        print(" Ajustando tornillos con precisión.")


class LlaveInglesa:
    def __init__(self, mango, material, peso):
        self.mango = mango
        self.material = material
        self.peso = peso

    def usar(self):
        print(" Apretando tuercas con cuidado.")


class Carpintero:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self, herramienta):
        
        
        print(f"\n {self.nombre} comienza a trabajar con una {herramienta.__class__.__name__}:")
        herramienta.usar()



carpintero = Carpintero("Luis")

martillo = Martillo("madera", "acero", 1.2)
destornillador = Destornillador("plástico", "acero inoxidable", 0.3)
llave = LlaveInglesa("goma", "hierro forjado", 0.8)


carpintero.trabajar(martillo)
carpintero.trabajar(destornillador)
carpintero.trabajar(llave)
