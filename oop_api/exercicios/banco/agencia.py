from .banco import Banco


class Agencia(Banco):
    def __init__(self, nome: str, endereco: str, numero: int):
        super().__init__(nome, endereco)
        self.numero = numero
