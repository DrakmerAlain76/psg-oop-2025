class Romano:
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100
    }

    def __init__(self, valor_romano):
        self.valor_romano = valor_romano
        self._valor_decimal = self._romano_a_decimal(valor_romano)

    def _romano_a_decimal(self, romano):
        """Convierte un número romano a su equivalente decimal."""
        total = 0
        prev = 0
        for simbolo in reversed(romano):
            valor = self.valores.get(simbolo, 0)
            if valor < prev:
                total -= valor
            else:
                total += valor
            prev = valor
        return total

    def _decimal_a_romano(self, numero):
        """Convierte un número decimal a romano."""
        equivalencias = [
            (100, 'C'), (90, 'XC'), (50, 'L'),
            (40, 'XL'), (10, 'X'), (9, 'IX'),
            (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        resultado = ""
        for valor, simbolo in equivalencias:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado

    def __add__(self, otro):
        """Sobrecarga del operador + (polimorfismo de operadores)."""
        if not isinstance(otro, Romano):
            raise TypeError("Solo se pueden sumar objetos Romano.")
        suma_decimal = self._valor_decimal + otro._valor_decimal
        nuevo_romano = self._decimal_a_romano(suma_decimal)
        return Romano(nuevo_romano)

    def mostrar(self):
        """Método polimórfico: puede redefinirse en subclases."""
        return f"{self.valor_romano} ({self._valor_decimal})"



num1 = Romano("X")
num2 = Romano("V")
resultado = num1 + num2

print(f"A: {num1.mostrar()}")
print(f"B: {num2.mostrar()}")
print(f"A+B: {resultado.mostrar()}")
