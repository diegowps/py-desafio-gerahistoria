import random

# --- CLASSE PAI (Superclasse) ---
class Bloco:
    """
    Representa um bloco genérico no mundo do Minecraft.
    Esta é a nossa classe base (ou 'pai').
    """
    def __init__(self, nome: str, dureza: int, ferramenta_ideal: str):
        """
        O construtor __init__ define os atributos que TODO bloco terá.
        'self' representa a instância específica do bloco que está sendo criada.
        """
        print(f"DEBUG: Criando o molde para um bloco do tipo {nome}...")
        self.nome = nome
        self.dureza = dureza
        self.ferramenta_ideal = ferramenta_ideal

    def __repr__(self):
        """ Retorna uma representação em string do objeto. """
        return f"Bloco de {self.nome}"

    def minerar(self, ferramenta_usada: str) -> bool:
        """
        Verifica se a ferramenta usada é a correta para minerar o bloco.
        Este método pertence a cada bloco individual.
        """
        print(f"Tentando minerar {self.nome} com {ferramenta_usada}...")
        if ferramenta_usada == self.ferramenta_ideal:
            print(f"✅ Sucesso! {self.nome} minerado.")
            return True
        else:
            print(f"❌ Falha! {self.ferramenta_ideal} é a ferramenta necessária.")
            return False

# --- CLASSES FILHAS (Subclasses) que herdam de Bloco ---
class Terra(Bloco):
    """
    Uma classe específica para o bloco de Terra. Herda de Bloco.
    """
    def __init__(self):
        # 'super()' chama o construtor da classe pai (Bloco)
        # para configurar os atributos com valores fixos para a Terra.
        super().__init__(nome="Terra", dureza=1, ferramenta_ideal="pá")

class Madeira(Bloco):
    """
    Uma classe específica para o bloco de Madeira. Herda de Bloco.
    """
    def __init__(self):
        super().__init__(nome="Madeira", dureza=3, ferramenta_ideal="machado")

class Diamante(Bloco):
    """
    Uma classe específica para o bloco de Diamante. Herda de Bloco.
    """
    def __init__(self):
        super().__init__(nome="Diamante", dureza=10, ferramenta_ideal="picareta de ferro")
        # Podemos adicionar atributos que só o diamante tem
        self.brilho = random.uniform(0.5, 1.0)
    
    # Podemos sobrescrever um método para dar um comportamento especial
    def minerar(self, ferramenta_usada: str) -> bool:
        # Chama o método original da classe pai primeiro
        sucesso = super().minerar(ferramenta_usada) 
        if sucesso:
            print("💎 UAU! Você encontrou um diamante brilhante!")
        return sucesso

# --- CLASSE QUE INTERAGE COM AS OUTRAS ---
class Jogador:
    """
    Representa o jogador no mundo do Minecraft.
    """
    def __init__(self, nome: str):
        self.nome = nome
        self.inventario = {} # Usaremos um dicionário para contar os itens

    def exibir_inventario(self):
        print("\n" + "="*20)
        print(f"Inventário de {self.nome}:")
        if not self.inventario:
            print("Vazio")
        else:
            for item, quantidade in self.inventario.items():
                print(f"- {item}: {quantidade}")
        print("="*20 + "\n")

    def coletar_bloco(self, bloco_minerado: Bloco):
        """
        Adiciona um bloco ao inventário do jogador ('self').
        """
        if bloco_minerado.nome in self.inventario:
            self.inventario[bloco_minerado.nome] += 1
        else:
            self.inventario[bloco_minerado.nome] = 1
        print(f"{self.nome} coletou 1x {bloco_minerado.nome}.")

# --- SCRIPT DE DEMONSTRAÇÃO (O JOGO ACONTECENDO) ---

# 1. Criando os objetos (instanciando as classes)
print("--- Criando o mundo e o jogador ---\n")
bloco_de_terra = Terra()
bloco_de_madeira = Madeira()
bloco_de_diamante = Diamante()
player = Jogador(nome="Steve")

# 2. O jogador começa com o inventário vazio
player.exibir_inventario()

# 3. O jogador tenta minerar com ferramentas diferentes
print("--- Steve começa sua jornada! ---\n")
,
# Tentativa 1: Ferramenta errada
sucesso_minerar = bloco_de_madeira.minerar(ferramenta_usada="pá")
if sucesso_minerar:
    player.coletar_bloco(bloco_de_madeira)

# Tentativa 2: Ferramenta certa
sucesso_minerar = bloco_de_madeira.minerar(ferramenta_usada="machado")
if sucesso_minerar:
    player.coletar_bloco(bloco_de_madeira)

# Tentativa 3: Minerando diamante
sucesso_minerar = bloco_de_diamante.minerar(ferramenta_usada="picareta de ferro")
if sucesso_minerar:
    player.coletar_bloco(bloco_de_diamante)

# 4. Verificando o inventário final do jogador
player.exibir_inventario()