import uuid # Usaremos para gerar IDs únicos para os produtos

# --- CLASSE 1: O MOLDE PARA OS PRODUTOS ---
class Produto:
    """
    Representa um item individual em nosso e-commerce.
    O __init__ aqui serve para definir as características obrigatórias de qualquer produto.
    """
    def __init__(self, nome: str, preco: float):
        # Validação básica dos dados de entrada
        if not nome or preco <= 0:
            raise ValueError("Nome do produto não pode ser vazio e o preço deve ser positivo.")
        
        # self está atribuindo os parâmetros recebidos aos atributos DO PRÓPRIO OBJETO
        self.nome = nome
        self.preco = preco
        self.id_produto = str(uuid.uuid4()) # Gera um ID único e universal

    def __repr__(self):
        """
        Método especial para retornar uma representação "oficial" do objeto como string.
        Facilita a depuração e a exibição.
        """
        return f"Produto(ID: {self.id_produto}, Nome: '{self.nome}', Preço: R${self.preco:.2f})"


# --- CLASSE 2: O MOLDE PARA O CARRINHO DE COMPRAS ---
class CarrinhoDeCompras:
    """
    Gerencia uma coleção de objetos Produto.
    Demonstra como um objeto pode conter e interagir com outros objetos.
    """
    def __init__(self, cliente_id: str):
        # self está definindo o ESTADO INICIAL de cada novo carrinho
        self.cliente_id = cliente_id
        self.itens = [] # A lista de itens pertence a ESTE carrinho específico (`self`)

    def adicionar_produto(self, produto: Produto):
        """
        Adiciona um objeto Produto à lista de itens do carrinho.
        'self.itens' acessa a lista de itens DESTE carrinho.
        """
        if isinstance(produto, Produto):
            self.itens.append(produto)
            print(f"✅ '{produto.nome}' foi adicionado ao carrinho.")
        else:
            print("❌ Erro: Apenas objetos do tipo Produto podem ser adicionados.")

    def remover_produto(self, id_produto: str):
        """
        Remove um produto da lista de itens com base em seu ID.
        'self.itens' é modificada por este método.
        """
        produto_para_remover = None
        for item in self.itens:
            if item.id_produto == id_produto:
                produto_para_remover = item
                break
        
        if produto_para_remover:
            self.itens.remove(produto_para_remover)
            print(f"🗑️ '{produto_para_remover.nome}' foi removido do carrinho.")
        else:
            print(f"⚠️ Produto com ID {id_produto} não encontrado no carrinho.")

    def calcular_total(self) -> float:
        """
        Calcula o valor total de todos os produtos no carrinho.
        'self.itens' é lida por este método.
        """
        # Uma forma elegante de somar os preços de todos os produtos na lista self.itens
        total = sum(produto.preco for produto in self.itens)
        return total

    def exibir_carrinho(self):
        """
        Mostra um resumo de todos os itens no carrinho e o valor total.
        Demonstra como métodos de um mesmo objeto se chamam usando 'self'.
        """
        print("\n" + "="*40)
        print(f"🛒 Carrinho do Cliente: {self.cliente_id}")
        print("="*40)
        if not self.itens:
            print("O seu carrinho está vazio.")
        else:
            for item in self.itens:
                print(f"- {item.nome}: R${item.preco:.2f}")
        
        # Chamando outro método do mesmo objeto usando self
        total_compra = self.calcular_total()
        print("-" * 40)
        print(f"💰 Total: R${total_compra:.2f}")
        print("="*40 + "\n")


# --- SCRIPT DE DEMONSTRAÇÃO ---

# 1. Criando instâncias (objetos) da classe Produto
livro = Produto(nome="POO em Python", preco=79.90)
cafe = Produto(nome="Café Gourmet 500g", preco=25.50)
teclado = Produto(nome="Teclado Mecânico", preco=350.00)

print(livro) # Mostra a representação criada pelo __repr__

# 2. Criando uma instância da classe CarrinhoDeCompras
meu_carrinho = CarrinhoDeCompras(cliente_id="cliente-123")

# 3. Interagindo com o objeto 'meu_carrinho' usando seus métodos
meu_carrinho.exibir_carrinho() # Mostra o carrinho vazio

meu_carrinho.adicionar_produto(livro)
meu_carrinho.adicionar_produto(cafe)
meu_carrinho.adicionar_produto(teclado)

meu_carrinho.exibir_carrinho() # Mostra o carrinho com 3 itens

meu_carrinho.remover_produto(cafe.id_produto) # Remove o café usando seu ID único

meu_carrinho.exibir_carrinho() # Mostra o carrinho atualizado