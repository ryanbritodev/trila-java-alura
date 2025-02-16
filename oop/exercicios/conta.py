# 1. Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
# 2. Na classe ContaBancaria, adicione um método especial `__str__` que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
# 3. Adicione um método de classe chamado `ativar_conta` à classe `ContaBancaria` que define o atributo ativo como `True`. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
# 4. Refatore a classe `ContaBancaria` para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
# 5. Crie uma instância da classe e imprima o valor da propriedade titular.
# 6. Crie uma classe chamada `ClienteBanco` com um
# construtor que aceita 5 atributos. Instancie 3 objetos desta classe e
# atribua valores aos seus atributos através do método construtor.
# 7. Crie um método de classe para a conta `ClienteBanco`.

class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def ativo(self):
        return "Ativo ✅" if self._ativo else "Inoperante ❌"

    @property
    def titular(self):
        return f"Nome do Titular: {self._titular}"

    @property
    def saldo(self):
        return f"Saldo do Titular: R${self._saldo}"

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    def __str__(self):
        return f"""--------------
{self.titular}
{self.saldo}
{self.ativo}
--------------"""

class ClienteBanco:
    clientes = []

    def __init__(self, nome: str, idade: int, saldo: float, endereco: str, profissao: str):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.endereco = endereco
        self.profissao = profissao
        ClienteBanco.clientes.append(self.nome)

    def __str__(self):
        return f"{self.nome}\n{self.idade}\n{self.saldo}\n{self.endereco}\n{self.profissao}"

    @classmethod
    def listar_clientes(cls):
        for nome in ClienteBanco.clientes:
            print(nome)

pessoa1 = ContaBancaria("José", 2768.12)
pessoa2 = ContaBancaria("Lucas", 4243.43)

print(pessoa1)
print(pessoa2)

pessoa3 = ContaBancaria("Ryan", 345.50)
ContaBancaria.ativar_conta(pessoa3)
print(pessoa3)

pessoa4 = ContaBancaria("Cássio Ramos", 4500000)

print()
print(pessoa4.titular)
print()

cliente1 = ClienteBanco("Jorge", 25, 5635.23, "Rua da Felicidade", "Desenvolvedor")
cliente2 = ClienteBanco("Henrique", 32, 50085.76, "Rua da Alegria", "CEO")
cliente3 = ClienteBanco("Carlos", 19, 2413.65, "Rua da Tristeza", "Estagiário")

ClienteBanco.listar_clientes()
