class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.material = material
        self.tipo = tipo

    def tocar(self):
        """Devuelve el sonido del instrumento (por defecto)."""
        return "sonido genérico"

    def mostrar(self):
        """Devuelve una representación en texto del instrumento y su sonido."""
        return f"{self.nombre} ({self.tipo}) - {self.tocar()}"


class Guitarra(Instrumento):
    def __init__(self, nombre, material, numero_cuerdas):
        super().__init__(nombre, material, "Cuerda")
        self.numero_cuerdas = numero_cuerdas

    def tocar(self):
        return f"strum (#{self.numero_cuerdas} cuerdas)"


class Piano(Instrumento):
    def __init__(self, nombre, material, numero_teclas):
        super().__init__(nombre, material, "Teclado")
        self.numero_teclas = numero_teclas

    def tocar(self):
        return f"plin (#{self.numero_teclas} teclas)"


class Tambor(Instrumento):
    def __init__(self, nombre, material, tipo_percusion):
        super().__init__(nombre, material, "Percusión")
        self.tipo_percusion = tipo_percusion

    def tocar(self):
        return f"boom (tipo: {self.tipo_percusion})"



if __name__ == "__main__":
    guitarra = Guitarra("Guitarra Acústica", "Madera", 6)
    piano = Piano("Piano de Cola", "Madera y metal", 88)
    tambor = Tambor("Tambor Militar", "Metal", "De marco")


    print(f"Guitarra: {guitarra.mostrar()}")
    print(f"Piano: {piano.mostrar()}")
    print(f"Tambor: {tambor.mostrar()}")
