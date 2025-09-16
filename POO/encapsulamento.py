class Ponto:
    """
    Representa um ponto com coordenadas X e Y em um plano 2D.
    Sua principal função é manter os dados x e y juntos.
    """
    def __init__(self, x: int, y: int):
        # 'self' cria os atributos 'x' e 'y' que pertencem a cada objeto Ponto
        self.x = x
        self.y = y

    def __repr__(self):
        """ Retorna uma representação em string do objeto para fácil visualização. """
        return f"Ponto(x={self.x}, y={self.y})"

# --- Uso ---
# Criando dois objetos (instâncias) da classe Ponto
p1 = Ponto(10, 20)
p2 = Ponto(5, -3)

# Acessando os atributos de cada objeto
print(f"O Ponto 1 está em: {p1}")
print(f"A coordenada X do Ponto 2 é: {p2.x}")
