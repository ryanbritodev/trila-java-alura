"""
Em Programação Orientada a Objetos (POO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):

```
nome
artista
duracao
```

Agora é sua vez! Crie uma classe chamada **Música** com os seguintes **atributos** e **crie 3 objetos** definindo cada **atributo**…
"""

class Musica:
    nome = ''
    artista = ''
    duracao = int


musica1 = Musica()
musica1.nome = "Bohemian Rhapsody"
musica1.artista = "Queen"
musica1.duracao = 355

musica2 = Musica()
musica2.nome = "Beat It"
musica2.artista = "Michael Jackson"
musica2.duracao = 280

musica3 = Musica()
musica3.nome = "Meu Novo Mundo"
musica3.artista = "Charlie Brown Jr."
musica3.duracao = 230