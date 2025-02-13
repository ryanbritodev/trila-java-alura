"""
Exercícios:
1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
"""


class Carro:
    def __init__(self, modelo: str, cor: str, ano: int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"{self.modelo}\n{self.cor}\n{self.ano}"


class Restaurante:
    def __init__(self, nome: str, categoria: str, ativo: False, localizacao: str, data_fundacao: str):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.localizacao = localizacao
        self.data_fundacao = data_fundacao

    def __str__(self):
        return f"{self.nome}\n{self.categoria}"


class Cliente:
    def __init__(self, nome: str, idade: int, prato_favorito: str, valor_conta: int):
        self.nome = nome
        self.idade = idade
        self.prato = prato_favorito
        self.valor = valor_conta



celtinha = Carro("Chevrolet Celta", "Vermelho", 2015)
nonna = Restaurante("Nonna Pizza", "Pizzaria", True, "Parque Marajoara, Santo André - SP", "15/08/1987")
cliente1 = Cliente("João", 27, "Macarrão", 50)
cliente2 = Cliente("Maria", 18, "Lasanha", 65)
cliente3 = Cliente("Jorge", 28, "Pizza", 70)

print(nonna)
