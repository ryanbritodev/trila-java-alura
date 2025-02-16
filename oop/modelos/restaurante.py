from oop.modelos.avaliacao import Avaliacao

class Restaurant:
    """
    Representa um restaurante e suas características
    """
    # Todo restaurante que for criado, atráves do método __init__, vai estar listado aqui
    restaurantes = []

    # self = Refere-se ao objeto que estamos instânciando
    # name, category = Argumentos que devemos passar para instância
    def __init__(self, name, category):
        """
        Inicializa a instância da nossa classe Restaurant
        Parâmetros:
        -> :param name: O nome do restaurante
        -> :param category: A categoria do restaurante
        """
        # Realizando alterações DIRETAMENTE no construtor (title, upper)
        self._name = name.title()  # Garantindo que todos os nomes das instâncias tenham a letra inicial maiúscula
        self._category = category.upper()  # Garantindo que todos as categorias das instâncias sejam maiúsculas
        self._ativo = False  # Atributo privado/protegido, que não deve ser mexido (boa prática, exige criação de um método Setter, que no caso é nossa Property)
        self._avaliacao = []
        Restaurant.restaurantes.append(self)

    def __str__(self):
        """
        Retorna uma representação da nossa classe em forma de string
        :return: Nome e Categoria do restaurante formatados
        """
        # Podemos colocar qualquer informação de identificação para o objeto
        return f'{self._name} | {self._category}'

    # Property NECESSÁRIA para controle de acesso
    @property
    def ativo(self):
        """
        Retorna um símbolo de correto caso o atributo ativado seja verdadeiro, e um símbolo de incorreto caso o atributo seja falso
        :return: ✅ ou ❌
        """
        return "✅" if self._ativo else "❌"

    @classmethod
    def listar_restaurantes(cls):
        """
        Exibe uma lista formatada de todos os restaurantes
        :return: Sem retorno
        """
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._name.ljust(25)} | {restaurante._category.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    def alternar_estado(self):
        """
        Alternar o estado de atividade do restaurante
        :return: Sem retorno
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente: str, nota: float):
        """
        Registra uma avaliação para o restaurante
        -> :param cliente: Nome do Cliente
        -> :param nota: Valor da Nota
        :return: Sem retorno
        """
        if nota > 5:
            nota = 5
        if nota < 0:
            nota = 0
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """
        Calcula e retorna a média das avaliações do restaurante
        :return: Média das avaliações daquela instância
        """
        if not self._avaliacao:
            return "Sem avaliações! 😄"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1) # Arredondado apenas uma casa decimal
        return media

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

# praca_restaurant = Restaurant('praça', 'Gourmet')
# praca_restaurant.alternar_estado()

# Não podemos realizar nenhuma alteração, pois não estamos nenhum atributo de setter que irá permirtir que possamos atribuir um novo valor (afinal, ele está protegido)
# praca_restaurant.name = "PraçaV2"
# praca_restaurant.ativo = True

# Agora sim ✅
# praca_restaurant._name = "PraçaV2"
# praca_restaurant._ativo = True

# pizza_restaurant = Restaurant('pizza express', 'Italiana')

# Nosso próprio método especial que guarda todos os restaurantes instanciados e mostra na tela
# Restaurant.listar_restaurantes()

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
