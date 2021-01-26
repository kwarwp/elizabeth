# elizabeth.callie.main.py


from _spy.vitollino.main import Cena, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

triangulo_azul = "https://i.imgur.com/IbG7St4.png"
triangulo_verde= 'https://i.imgur.com/bcse41s.png'
triangulo_vermelho= 'https://i.imgur.com/KAfuNJG.png'
triangulo_amarelo= 'https://i.imgur.com/g8TxYsH.png'
desafio= 'https://i.imgur.com/0kfiusf.png'
biblioteca = "https://i.imgur.com/wistRJZ.jpeg" 

class Item_herdado(Elemento):
    """Construção de uma classe que herde de Elemento
    """
    def bota(self, *_):
        """Aciona estado de inv.bota = True para que eventual clique devolva o Elemento para a cena"""
        inv.bota(self, True)
        #self.vai=lambda*_:self.resgata(x=x,y=y,w=w,h=h)
        """Método vai do Elemento atrelado ao evento de reposicionamento, onde o memento especifica os argumentos pedidos pelo método resgata."""
        self.vai=lambda*_:self.resgata(*self.memento)

    def resgata(self,x,y,w,h):
        """Método para resgate do Elemento no inventário"""
        self.x,self.y,self.w,self.h= x,y,w,h
        """Retira Elemento atrelado ao título do inventário"""
        inv.tira(self.tit)
        """Coloca Elemento na cena"""
        self.entra(inv.cena)
        """Aciona estado de inv.bota = False para que eventual clique devolva o Elemento para o inventário"""
        self.vai=self.bota

    def mementor(self,memento):
         """Permite que o style do elemento a ser recolocado na tela seja especificado"""
         self.memento=memento


class Main():

    def __init__(self):
        inv.inicia()
        self.BIBLIOTECA=Cena(biblioteca)
        
        self.DESAFIO= Elemento(desafio, tit="Hipátia",
                               w=250,h=250, x=300, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA)

        self.T_AZUL=Item_herdado(triangulo_azul, tit="nome_do_meu_elemento", 
                                H=60,w=60, X=100, Y=100,
                                cena=self.BIBLIOTECA)
        
        self.T_AZUL.mementor((110,150,200,"200px"))
        self.T_AZUL.vai=self.T_AZUL.bota

        self.BIBLIOTECA.vai()

if __name__ == "__main__":
    Main()