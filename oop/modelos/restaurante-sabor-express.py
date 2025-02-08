# Classe antiga
# class Restaurant:
#     def __init__():
#         name = ''
#         category = ''
#         active = False

# Classe nova
# Utilizando o método __init__ para criar o nosso CONSTRUTOR
# Sempre que criarmos uma nova instância de um objeto (novo restaurante), o método __init__ é chamado, esperando algum tipo de ação
# Isso garante que cada instância vai ter suas próprias informações
class Restaurant:
    # Todo restaurante que for criado, atráves do método __init__, vai estar listado aqui
    restaurantes = []

    # self = Refere-se ao objeto que estamos instânciando
    # name, category = Argumentos que devemos passar para instância
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurantes.append(self)

    def __str__(self):
        # Podemos colocar qualquer informação de identificação para o objeto
        return f'{self.name} | {self.category}'

    def listar_restaurantes():
        for restaurante in Restaurant.restaurantes:
            print(f'{restaurante.name} | {restaurante.category} | {restaurante.active}')


praca_restaurant = Restaurant('Praça', 'Gourmet')
pizza_restaurant = Restaurant('Pizza Express', 'Italiana')

# Nosso próprio método especial que guardar todos os restaurantes instanciados e mostra na tela
Restaurant.listar_restaurantes()

# Acessando o objeto
# noodle_restaurant.name = 'Noodle'
# noodle_restaurant.category = 'Gourmet'

# restaurants = [pizza_restaurant, praca_restaurant]

# Local da Memória onde está o objeto (SEM O MÉTODO __STR__)
# print('Local do Objeto na Memória:', praca_restaurant)

# # Instância em formato de texto
# print(pizza_restaurant)
#
# # Printando os Atributos/Métodos da Classe
# print('\nAtributos/Métodos da Classe: ', dir(praca_restaurant))
#
# # Printando os Valores da Classe (Dicionário)
# print('\nDicionário dos Valores da CLasse: ', vars(praca_restaurant))
#
# # Printando os Valores Individualmente
# print(f'\nValores Individuais\nNome: {praca_restaurant.name}\nCategoria: {praca_restaurant.category}\nAtivo: {praca_restaurant.active}')
