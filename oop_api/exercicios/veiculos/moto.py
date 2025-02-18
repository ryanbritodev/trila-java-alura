from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, tipo: str):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}\n{self.tipo}"