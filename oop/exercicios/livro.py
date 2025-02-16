# 1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
# 2. Na classe Livro, adicione um método especial **str** que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
# 3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
# 4. Adicione um método estático chamado `verificar_disponibilidade` à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
# 5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
# 6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
# 7. No arquivo biblioteca.py, utilize o método estático `verificar_disponibilidade` para obter a lista de livros disponíveis publicados em um ano específico.
# 8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método **str**.

# Arquivo livro.py

class Livro:
    livros = []

    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        self.livros.append([self._titulo, self._disponivel, self._ano_publicacao])

    @property
    def disponivel(self):
        return "Disponível ✅" if self._disponivel else "Indisponível ❌"

    def __str__(self):
        return f"{self._titulo}\n{self._autor}\n{self._ano_publicacao}\n{self.disponivel}"

    def emprestar(self):
        self._disponivel = False
        for livro in Livro.livros:
            if self._titulo == livro[0]:
                livro[1] = False
            else:
                continue


    @staticmethod
    def verificar_disponibilidade(ano: int):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro[1] and livro[2] == ano:
                livros_disponiveis.append(livro[0])
            else:
                continue
        if not livros_disponiveis:
            return "Nenhum livro disponível ❌"
        else:
            return livros_disponiveis

