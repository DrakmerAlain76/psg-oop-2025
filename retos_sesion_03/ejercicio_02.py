class Cocinero:
    recetas_permitidas = {
        "pan": {"harina", "agua"},
        "pizza": {"harina", "agua", "sal", "tomate", "queso"},
        "galleta": {"harina", "agua", "sal", "chocolate"}
    }

    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = set(ingredientes)
        self.productividad = 0

    def preparar(self, receta):
        if receta not in Cocinero.recetas_permitidas:
            print(f"{self.nombre}: La receta '{receta}' no existe en el sistema ")
            return

        ingredientes_necesarios = Cocinero.recetas_permitidas[receta]

        if ingredientes_necesarios.issubset(self.ingredientes):
            self.productividad += 1
            print(f"{self.nombre} preparó {receta} con éxito | Productividad: {self.productividad}")
        else:
            faltan = ingredientes_necesarios - self.ingredientes
            print(f"{self.nombre} no puede preparar {receta}. Faltan: {', '.join(faltan)}")

    def mostrar_productividad(self):
        print(f"{self.nombre} tiene productividad {self.productividad} puntos ")

    @classmethod
    def recetas_disponibles(cls):
        print(" Recetas permitidas en el sistema:")
        for receta, ingredientes in cls.recetas_permitidas.items():
            print(f" - {receta.capitalize()}: {', '.join(ingredientes)}")

    @staticmethod
    def total_productividad(cocineros):
        total = sum(c.productividad for c in cocineros)
        print(f" Productividad total del equipo: {total} puntos")
        return total


print("Cocina profesional en acción...\n")

c1 = Cocinero("María", ["harina", "agua", "sal", "tomate", "queso"])
c2 = Cocinero("Juan", ["harina", "agua", "chocolate", "sal"])
c3 = Cocinero("Pedro", ["agua", "harina"])

Cocinero.recetas_disponibles()
print()

c1.preparar("pizza")
c2.preparar("galleta")
c3.preparar("pan")
c1.preparar("galleta")
c2.preparar("pizza")  
c3.preparar("galleta") 

print("\n--- Productividad individual ---")
c1.mostrar_productividad()
c2.mostrar_productividad()
c3.mostrar_productividad()

print("\n--- Productividad total ---")
Cocinero.total_productividad([c1, c2, c3])
