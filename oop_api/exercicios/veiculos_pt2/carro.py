from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def __str__(self):
        return f"Marca: {self._marca}\nModelo: {self._modelo}\nCor: {self._cor}"

    def ligar(self):
        print("Estado: Ligado")
