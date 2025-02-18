from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return f"{super().__str__()}\n{self.portas}"
