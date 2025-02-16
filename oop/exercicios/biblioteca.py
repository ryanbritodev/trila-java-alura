# Arquivo biblioteca.py

from livro import Livro

livro1 = Livro("Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro2 = Livro("A Culpa É das Estrelas", "John Green", 2012)

print(livro1)
print("--------------------------")
print(livro2)
print("--------------------------")

livro3 = Livro("A Droga da Obediência", "Pedro Bandeira", 1985)
livro3.emprestar()
print(livro3)

print(f"\nLivros de 1985 disponíveis: {Livro.verificar_disponibilidade(1985)}")
