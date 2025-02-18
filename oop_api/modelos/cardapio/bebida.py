from .item_cardapio import ItemCardapio


class Bedida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho # Atributo da classe

    def __str__(self):
        return self._nome