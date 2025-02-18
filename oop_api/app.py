from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bedida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bedida("Suco de Melancia", 5.0, "Grande")
prato_paozinho = Prato("Pãozinho", 2.0, "O Melhor Pão da Cidade!")


def main():
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()
