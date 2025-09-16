class Lampada:
    """
    Representa uma lâmpada que pode estar ligada ou desligada.
    Seu estado interno ('ligada') é modificado por seus métodos.
    """
    def __init__(self):
        # Toda lâmpada nova começa desligada
        self.ligada = False

    def acender(self):
        """ Muda o estado 'ligada' para True. """
        print("💡 A lâmpada acendeu!")
        self.ligada = True

    def apagar(self):
        """ Muda o estado 'ligada' para False. """
        print("⚫ A lâmpada apagou.")
        self.ligada = False

    def esta_ligada(self) -> bool:
        """ Retorna o estado atual. """
        return self.ligada

# --- Uso ---
# Criando uma lâmpada
lampada_da_sala = Lampada()
print(f"A lâmpada está ligada? {lampada_da_sala.esta_ligada()}")

# Modificando o estado do objeto com seus métodos
lampada_da_sala.acender()
print(f"E agora, a lâmpada está ligada? {lampada_da_sala.esta_ligada()}")

lampada_da_sala.apagar()
print(f"E finalmente, está ligada? {lampada_da_sala.esta_ligada()}")