# Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome: str, idade: int, profissao: str):
        self._nome = nome.strip().title()
        self._idade = idade
        self.profissao = profissao.strip().upper()

    def __str__(self):
        return f"Nome: {self._nome}\nIdade: {self._idade}"

    def aniversario(self):
        self._idade += 1

    @property
    def saudacao(self):
        return f"Olá {self._nome}! Sua profissão é {self.profissao}"


jose = Pessoa("José", 33, "Mecânico")
print(jose)

print("\n1 ano depois...\n")
jose.aniversario()

print(jose)

print()
print(jose.saudacao)
