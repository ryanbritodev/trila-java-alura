"""
Exercícios
    Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
    Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
    Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
    Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
    Altere o valor do atributo nome para 'Bistrô'.
    Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
    Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
    Mude o estado da instância restaurante_pizza para ativo.
    Imprima no console o nome e a categoria da instância restaurante_praca.
"""


class Restaurante:
    nome = str
    categoria = str
    ativo = False


restaurante_praca = Restaurante()

restaurante_praca.categoria = "Italiana"
restaurante_praca.nome = "Mamma Mia"

print(restaurante_praca.nome)

if restaurante_praca.ativo:
    print(f"O restaurante {restaurante_praca.nome} está ATIVO! :)")
else:
    print(f"O restaurante {restaurante_praca.nome} está INATIVO! :(")

# Acessando diretamente da classe (tipo str)
categoria = Restaurante.categoria

# Atribuindo novo nome
restaurante_praca.nome = "Bristrô"

restaurante_pizza = Restaurante()

restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

if restaurante_pizza.categoria == "Fast Food":
    print(f"\nA categoria do restaurante {restaurante_pizza.nome} É Fast Food! :)")
else:
    print(f"\nA categoria do restaurante {restaurante_pizza.nome} NÃO É Fast Food! :(")

# Mudando o estado
restaurante_pizza.ativo = True

print(f"\nNome do Restaurante: {restaurante_praca.nome}\nCategoria: {restaurante_praca.categoria}")
