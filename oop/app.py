from modelos.restaurante import Restaurant

restaurante_praca = Restaurant("Praça", "Gourmet")
restaurante_japa = Restaurant("Japa", "Japonesa")
restaurante_mexicano = Restaurant("El Chavito", "Mexicana")
restaurante_praca.receber_avaliacao("Guilherme", 9.1)
restaurante_praca.receber_avaliacao("Laís", 8.2)
restaurante_praca.receber_avaliacao("Emy", 4.3)
restaurante_japa.receber_avaliacao("Cássio", 8)
restaurante_japa.receber_avaliacao("Jorge", 5)
restaurante_japa.receber_avaliacao("Lucas", 7)

def main():
    Restaurant.listar_restaurantes()

if __name__ == '__main__':
    main()