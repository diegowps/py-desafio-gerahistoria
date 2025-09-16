class Retangulo:
    """
    Representa um retângulo com largura e altura.
    Pode calcular a sua própria área.
    """
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def calcular_area(self) -> float:
        """
        Este método usa os atributos do próprio objeto ('self') para fazer um cálculo.
        """
        return self.largura * self.altura

# --- Uso ---
# Criando um objeto Retangulo
r1 = Retangulo(largura=5, altura=4)

# Chamando o método do objeto para obter um resultado
area_do_retangulo = r1.calcular_area()

print(f"Um retângulo de largura {r1.largura} e altura {r1.altura} tem área {area_do_retangulo}.")

