class Musica:
    # Lista para registrar todas as instâncias de músicas criadas
    musicas = []

    def __init__(self, nome: str, artist: str, duracao: int):
        self.nome = nome
        self.artista = artist
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome}\n{self.artista}\n{self.duracao}'

    @staticmethod
    def listar_musicas():
        print("Lista de Músicas:")
        for musica in Musica.musicas:
            print(musica.nome)


queen = Musica("Bohemian Rhapsody", "Queen", 355)
charlie_brown = Musica("Meu Novo Mundo", "Charlie Brown Junior", 50)

print(queen)

print()

Musica.listar_musicas()
