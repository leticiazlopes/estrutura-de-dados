class Node:


    def __init__(self, valor):
        self.valor = valor
        self.filho_esquerda: Node|None = None
        self.filho_direita: Node|None = None


    def __repr__(self):
        return f'No(valor={self.valor})'


    def add_esquerda(self, valor):
        if self.filho_esquerda is None:
            self.filho_esquerda = Node(valor)


    def add_direita(self, valor):
        if self.filho_direita is None:
            self.filho_direita = Node(valor)


    @property
    def tem_filho_esquerda(self) -> bool:
        return bool(self.filho_esquerda)


    @property
    def tem_filho_direita(self) -> bool:
        return bool(self.filho_direita)


    @property
    def eh_folha(self) -> bool:
        return not self.tem_filho_direita and not self.tem_filho_esquerda




class Arvore:
#enquanto houver um filho à esquerda, ele vai indo para lá...
    def _get_sucessor(self, no: Node) -> Node:
        atual: Node = no
        while atual.tem_filho_esquerda:
            atual = atual.filho_esquerda
        return atual
#o sucessor é o nó com o menor valor na subarvore à direita, na posicao mais a esquerda
   # 50
   #/  \
  #30   70
 #/ \   / \
#20 40 60 80

  #70
 #/ \
#60 80
#é usado o numero 60


#interface pública de remocao
    def remocao(self, valor):
        self.raiz = self._remocao(self.raiz, valor)
        #essa linha inicia o processo de remocao pela raiz e atualização do valor da raíz


    def _remocao(self, no: Node|None, valor) -> Node|None:
        if no is None:
            return None
        if valor < no.valor:
            no.filho_esquerda = self._remocao(no.filho_esquerda, valor)
        elif valor > no.valor:
            no.filho_direita = self._remocao(no.filho_direita, valor)
        else:
            if not no.tem_filho_direita:
                return no.filho_esquerda
            elif not no.tem_filho_esquerda:
                return no.filho_direita
            else:
                substituto = self._get_sucessor(no.filho_direita)
                no.valor = substituto.valor
                no.filho_direita = self._remocao(no.filho_direita, no.valor)
        return no
