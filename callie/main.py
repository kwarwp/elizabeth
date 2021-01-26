# elizabeth.callie.main.py


from _spy.vitollino.main import Cena, Elemento
from _spy.vitollino.main import INVENTARIO as inv

MEU_ELEMENTO = "https://www.google.com/search?q=triangulo&client=firefox-b-d&sxsrf=ALeKk02DvWgeacvmUUEJvHwHHVgX2O9dbQ:1611682055717&tbm=isch&source=iu&ictx=1&fir=dPgY8LSjDy7WhM%252C_RuuHgfhOqxvSM%252C_&vet=1&usg=AI4_-kRkP1FM7wBFMZL0vriH4hMllIgkLA&sa=X&ved=2ahUKEwivxq_Dj7ruAhXAH7kGHaDZAOgQ_h16BAgVEAE#imgrc=dPgY8LSjDy7WhM" # Extensões aceitas: png, jpg, jpeg e gif
MINHA_CENA = "https://media.gazetadopovo.com.br/haus/2019/10/decoracao-de-quarto-com-cores-neutras-13-768x473-3cf2c1b0.jpg" # Extensões aceitas: png, jpg, jpeg e gif

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
        self.minha_cena=Cena(MINHA_CENA)

        self.meu_elemento=Item_herdado(MEU_ELEMENTO, tit="nome_do_meu_elemento",style=dict(height=60,widht=60, left=100, top=100),cena=self.minha_cena)
        self.meu_elemento.mementor((110,150,200,"200px"))
        self.meu_elemento.vai=self.meu_elemento.bota

        self.minha_cena.vai()

if __name__ == "__main__":
    Main()