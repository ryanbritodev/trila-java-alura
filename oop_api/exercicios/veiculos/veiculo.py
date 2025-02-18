# 1. Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros: marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
# 2. Construa o Método Especial **str**: Adicione um método especial **str** à classe Veiculo que retorne uma mensagem formatada com a marca, modelo e estado do veículo (ligado/desligado).
# 3. Crie uma Classe Filha (Carro): Crie uma classe chamada Carro que herde da classe Veiculo. No construtor da classe Carro, adicione um novo atributo chamado portas que indique a quantidade de portas do carro.
# 4. Implemente o Método Especial **str** na Classe Filha: Adicione um método especial **str** à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas.
# 5. Crie uma Classe Filha (Moto): Crie uma classe chamada Moto que também herde de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
# 6. Implemente o Método Especial **str** na Classe Filha (Moto): Adicione um método especial **str** à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
# 7. Crie um Arquivo Main ([main.py](http://main.py)): Crie um arquivo [main.py](http://main.py) no mesmo diretório das classes.
# 8. Importe e Instancie Objetos: No arquivo [main.py](http://main.py), importe as classes Carro e Moto. Crie três instâncias de cada classe com diferentes marcas, modelos, quantidade de portas e tipos.
# 9. Exiba as Informações: Imprima no console as informações de cada instância utilizando o método **str**.

class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f"{self.marca}\n{self.modelo}\n{status}"