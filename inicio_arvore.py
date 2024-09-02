class Arvore:


    def __init__(self):
        self.raiz: Node|None = None


    @property
    def vazia(self) -> bool:
        return self.raiz is None


