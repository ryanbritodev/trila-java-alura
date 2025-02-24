from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self._modelo = modelo


    @abstractmethod
    def ligar(self):
        pass
