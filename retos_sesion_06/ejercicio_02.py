class Departamento:
    def __init__(self, numero, inquilinos):
        self.numero = numero
        self.inquilinos = inquilinos

    def mostrar_informacion(self):
        print(f"   🏠 Departamento {self.numero}")
        print(f"      Inquilinos: {', '.join(self.inquilinos)}")


class Oficina:
    def __init__(self, numero, telefono):
        self.numero = numero
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"   🏢 Oficina {self.numero}")
        print(f"      Teléfono: {self.telefono}")


class Piso:
    def __init__(self, numero):
        self.numero = numero
        self._departamentos = []
        self._oficinas = []

    def agregar_departamento(self, departamento):
        self._departamentos.append(departamento)

    def agregar_oficina(self, oficina):
        self._oficinas.append(oficina)

    def mostrar_informacion(self):
        print(f"\n🔹 Piso {self.numero}:")
        if self._departamentos:
            print("  Departamentos:")
            for d in self._departamentos:
                d.mostrar_informacion()
        else:
            print("  No hay departamentos en este piso.")

        if self._oficinas:
            print("  Oficinas:")
            for o in self._oficinas:
                o.mostrar_informacion()
        else:
            print("  No hay oficinas en este piso.")


class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self._pisos = []

    def agregar_piso(self, piso):
        self._pisos.append(piso)

    def mostrar_informacion(self):
        print(f"\n🏢 Edificio: {self.nombre}")
        print(f"📍 Dirección: {self.direccion}")
        print(f"Total de pisos: {len(self._pisos)}")
        for piso in self._pisos:
            piso.mostrar_informacion()



edificio = Edificio("Torre Illimani", "Av. Arce #456, La Paz")


piso1 = Piso(1)
piso2 = Piso(2)
piso3 = Piso(3)


piso1.agregar_departamento(Departamento("101", ["Ana", "Luis"]))
piso1.agregar_oficina(Oficina("1A", "22123456"))

piso2.agregar_departamento(Departamento("201", ["Carlos"]))
piso2.agregar_departamento(Departamento("202", ["Marta", "José"]))
piso2.agregar_oficina(Oficina("2B", "22456789"))

piso3.agregar_departamento(Departamento("301", ["Sofía"]))
piso3.agregar_oficina(Oficina("3A", "22789012"))
piso3.agregar_oficina(Oficina("3C", "22789013"))


edificio.agregar_piso(piso1)
edificio.agregar_piso(piso2)
edificio.agregar_piso(piso3)


edificio.mostrar_informacion()
