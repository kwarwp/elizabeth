# elizabeth.callie.main.py


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from _spy.vitollino.main import INVENTARIO as inv

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

triangulo_azul = "https://i.imgur.com/IbG7St4.png"
triangulo_verde= 'https://i.imgur.com/bcse41s.png'
triangulo_vermelho= 'https://i.imgur.com/KAfuNJG.png'
triangulo_amarelo= 'https://i.imgur.com/g8TxYsH.png'
triangulo_roxo= 'http://1.bp.blogspot.com/_o7MZRBJ1zfQ/S3HPfxN6-FI/AAAAAAAADLI/f1i46TAmM4Q/s320/270px-Purple_triangle_svg+triangulo+roxo.png'
triangulo_rosa ='https://aventurasnahistoria.uol.com.br/media/uploads/pink_triangle_up.svg.png'
triangulo_laranja= 'https://lh3.googleusercontent.com/proxy/-WJMuhgeeuzRRxS-nIgZ9PahHXP72kxbnoetbIMvrHxUy1RHrV-Ds7MzNuudP4rIav5ctJ0ELzdYb3EfdrkwKjxzcppd_-WMgtcMjIQ6FWRHD5CcWBMITK-QEz8CAHXIhMCfqC4zlYIKQO1sw0o'
triangulo_ciano='https://cdn.pixabay.com/photo/2017/09/01/09/22/triangle-2703515_1280.jpg'
quadrado_vermelho= 'https://thumbs.dreamstime.com/b/fundo-do-teste-padr%C3%A3o-quadrado-vermelho-110087135.jpg'
desafio= 'https://i.imgur.com/0kfiusf.png'
biblioteca = "https://i.imgur.com/wistRJZ.jpeg" 



class desafio_teorema():

    def __init__(self):
        inv.inicia()
        self.BIBLIOTECA=Cena(biblioteca)
        
        self.DESAFIO= Elemento(desafio, tit="Hipátia",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA)

        self.T_AZUL=Elemento (triangulo_azul, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=100, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_AMARELO=Elemento (triangulo_amarelo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_VERMELHO =Elemento (triangulo_vermelho, tit="nome_do_meu_elemento", 
                                   h=80,w=80, x=300, y=150,
                                   cena=self.BIBLIOTECA)
                                
        self.T_VERDE =Elemento (triangulo_verde, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_ROXO =Elemento (triangulo_roxo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_ROSA =Elemento (triangulo_rosa, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_LARANJA = Elemento (triangulo_laranja, tit="nome_do_meu_elemento", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA)
                                   
        self.T_CIANO = Elemento (triangulo_ciano, tit="nome_do_meu_elemento", 
                                 h=80,w=80, x=800, y=150,
                                 cena=self.BIBLIOTECA)
                                   
        self.QUADRADO_VERMELHO = Elemento (quadrado_vermelho, tit="nome_do_meu_elemento", 
                                           h=100,w=100, x=313, y=282,
                                           cena=self.BIBLIOTECA)
        
        
        self.texto_1= Texto(self.BIBLIOTECA, txt= 'Clique no quadrado vermelho para completar o quebra-cabeça. Escolha a melhor imagem que complete aquela posição.')
        
    def inicia(self,*_):
        self.BIBLIOTECA.vai()
        self.texto_1.vai()

if __name__ == "__main__":
    desafio_teorema().inicia()