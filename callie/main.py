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



class Main():

    def __init__(self):
        inv.inicia()
        self.BIBLIOTECA=Cena(biblioteca)
        
        self.DESAFIO= Elemento(desafio, tit="Hipátia",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA)

        self.T_AZUL=Elemento (triangulo_azul, tit="nome_do_meu_elemento", 
                                H=60,w=60, X=100, Y=100,
                                cena=self.BIBLIOTECA)
                                
        self.T_AMARELO=Elemento (triangulo_amarelo, tit="nome_do_meu_elemento", 
                                H=60,w=60, X=200, Y=200,
                                cena=self.BIBLIOTECA)
                                
        self.T_VERMELHO =Elemento (triangulo_vermelho, tit="nome_do_meu_elemento", 
                                H=60,w=60, X=300, Y=300,
                                cena=self.BIBLIOTECA)
        
        


        self.BIBLIOTECA.vai()

if __name__ == "__main__":
    Main()