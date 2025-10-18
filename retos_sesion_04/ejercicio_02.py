class Celula:
    def __init__(self, ADN, tipo_celula, energia=50):
        self.__ADN = ADN            
        self.__energia = energia    
        self.__tipo_celula = tipo_celula  

    
    @property
    def ADN(self):
        """Devuelve el ADN de la célula (solo lectura)."""
        return self.__ADN

    
    @property
    def tipo_celula(self):
        """Devuelve el tipo de célula."""
        return self.__tipo_celula

    @tipo_celula.setter
    def tipo_celula(self, nuevo_tipo):
        """Permite modificar el tipo de célula."""
        self.__tipo_celula = nuevo_tipo

    
    @property
    def energia(self):
        """Devuelve el nivel de energía actual."""
        return self.__energia

    
    def comer(self, cantidad):
        """Aumenta la energía de la célula al comer."""
        if cantidad > 0:
            self.__energia += cantidad
            print(f"La célula ha comido. Energía actual: {self.__energia}")
        else:
            print("La cantidad de energía debe ser positiva.")

    def dividirse(self):
        """Simula la división celular, consumiendo energía."""
        if self.__energia >= 30:
            self.__energia -= 30
            print(f"La célula se ha dividido correctamente. Energía restante: {self.__energia}")
        else:
            print("No hay suficiente energía para dividirse.")

    def mostrar_estado(self):
        """Muestra el estado actual de la célula."""
        print(f"Tipo: {self.__tipo_celula} | Energía: {self.__energia} | ADN: {self.__ADN}")



if __name__ == "__main__":
    
    celula1 = Celula("ATCGGA", "Muscular", 60)
    celula2 = Celula("GGTACC", "Nerviosa", 40)

    
    celula1.mostrar_estado()
    celula2.mostrar_estado()

    print("\n--- Acciones de la célula 1 ---")
    celula1.comer(20)
    celula1.dividirse()
    celula1.mostrar_estado()

    print("\n--- Acciones de la célula 2 ---")
    celula2.dividirse()
    celula2.comer(15)
    celula2.tipo_celula = "Epitelial"  
    celula2.mostrar_estado()
