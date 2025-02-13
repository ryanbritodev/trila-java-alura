# Classe antiga
# class Restaurant:
#     def __init__():
#         name = ''
#         category = ''
#         ativo = False

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
        self._name = name.title()  # Garantindo que todos os nomes das instâncias tenham a letra inicial maiúscula
        self.category = category.upper()  # Garantindo que todos as categorias das instâncias sejam maiúsculas
        self._ativo = False  # Atributo privado/protegido, que não deve ser mexido (boa prática, exige criação de método Setter)
        Restaurant.restaurantes.append(self)

    def __str__(self):
        # Podemos colocar qualquer informação de identificação para o objeto
        return f'{self._name} | {self.category}'

    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"

    @staticmethod
    def listar_restaurantes():
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in Restaurant.restaurantes:
            print(f'{restaurante.name.ljust(25)} | {restaurante.category.ljust(25)} | {restaurante.ativo}')


praca_restaurant = Restaurant('praça', 'Gourmet')
praca_restaurant.nome = "PraçaV2"
praca_restaurant.ativo = True
pizza_restaurant = Restaurant('pizza express', 'Italiana')

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
# print(f'\nValores Individuais\nNome: {praca_restaurant.name}\nCategoria: {praca_restaurant.category}\nAtivo: {praca_restaurant.ativo}')
