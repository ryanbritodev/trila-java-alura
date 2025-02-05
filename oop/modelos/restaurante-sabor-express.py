class Restaurant:
    name = ''
    category = ''
    active = False


noodle_restaurant = Restaurant()
# Acessando o objeto
noodle_restaurant.name = 'Noodle'
noodle_restaurant.category = 'Gourmet'

pizza_restaurant = Restaurant()

restaurants = [pizza_restaurant, noodle_restaurant]

# Local da Memória onde está o objeto
print('Local do Objeto na Memória:', noodle_restaurant)

# Printando os Atributos/Métodos da Classe
print('Atributos/Métodos da Classe: ', dir(noodle_restaurant))

# Printando os Valores da Classe (Dicionário)
print('Dicionário dos Valores da CLasse: ', vars(noodle_restaurant))

# Printando os Valores Individualmente
print('Valores Individuais:', noodle_restaurant.name, noodle_restaurant.category, noodle_restaurant.active)
