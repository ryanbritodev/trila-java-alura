from oop_api.modelos.avaliacao import Avaliacao
from .cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    # Métodos repetidos, não é prático
    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)
    #
    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        else:
            print(f"Erro: {item} não é uma instância de ItemCardapio")


    def exibir_cardapio(self):
        print(f"Cardápio do Restaurante {self._nome}:\n")
        # Iterando sobre os itens do cardápio daquele restaurante, e usando a função enumerate para devolver o índice
        for i, item in enumerate(self._cardapio, start=1): # Começar no 1
            # Ao passar o nome da instância e o atributo, a função verifica se ela existe ou não
            if hasattr(item, 'descricao'):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}"
                print(mensagem_prato)
            elif hasattr(item, 'tamanho'):
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}"
                print(mensagem_bebida)
            else:
                mensagem = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho} | Descrição: {item._descricao}"
                print(mensagem)
