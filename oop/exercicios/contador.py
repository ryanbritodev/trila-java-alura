class Contador:
    contador_global = 0

    def __init__(self):
        self.valor = 0

    def __str__(self):
        return f"Contador: {self.valor}"

    def incrementar(self):
        self.valor += 1

    @classmethod
    def zerar_contador_global(cls):
        cls.contador_global = 0
        return "Contador global zerado ✅"
