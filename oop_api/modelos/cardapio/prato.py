from .item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        # Caso eu não quiser nenhum desconto, podemos adicionar um "pass"
        self._preco -= (self._preco * 0.05)