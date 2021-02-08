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
        
        self.BIBLIOTECA2=Cena(biblioteca)
        
        self.BIBLIOTECA3=Cena(biblioteca)
        
        self.BIBLIOTECA4=Cena(biblioteca)
        
        self.BIBLIOTECA5=Cena(biblioteca)
        
        
        
        #ELEMENTOS BIBLIOTECA
        
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
                                           
        #ELEMENTOS BIBLIOTECA2
        
        self.DESAFIO2= Elemento(desafio, tit="Hipátia",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA2)

        self.T_AZUL2=Elemento (triangulo_azul, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=100, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_AMARELO2=Elemento (triangulo_amarelo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_VERMELHO2 =Elemento (triangulo_vermelho, tit="nome_do_meu_elemento", 
                                   h=80,w=80, x=300, y=150,
                                   cena=self.BIBLIOTECA2)
                                
        self.T_VERDE2 =Elemento (triangulo_verde, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_ROXO2 =Elemento (triangulo_roxo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_ROSA2 =Elemento (triangulo_rosa, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_LARANJA2 = Elemento (triangulo_laranja, tit="nome_do_meu_elemento", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA2)
                                   
        self.QUADRADO_VERMELHO2 = Elemento (quadrado_vermelho, tit="nome_do_meu_elemento", 
                                           h=100,w=100, x=413, y=282,
                                           cena=self.BIBLIOTECA2)
                                           
        #ELEMENTOS BIBLIOTECA 3
        
        self.DESAFIO3= Elemento(desafio, tit="Hipátia",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA3)

                                
        self.T_AMARELO3=Elemento (triangulo_amarelo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA3)
                                
        self.T_VERMELHO3 =Elemento (triangulo_vermelho, tit="nome_do_meu_elemento", 
                                   h=80,w=80, x=300, y=150,
                                   cena=self.BIBLIOTECA3)
                                
        self.T_VERDE3 =Elemento (triangulo_verde, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA3)
                                
        self.T_ROXO3 =Elemento (triangulo_roxo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA3)
                                
        self.T_ROSA3 =Elemento (triangulo_rosa, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA3)
                                
        self.T_LARANJA3 = Elemento (triangulo_laranja, tit="nome_do_meu_elemento", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA3)
                                   
                                   
        self.QUADRADO_VERMELHO3 = Elemento (quadrado_vermelho, tit="nome_do_meu_elemento", 
                                           h=100,w=100, x=513, y=282,
                                           cena=self.BIBLIOTECA3)
                                           
        #ELEMENTOS BIBLIOTECA 4
        
        self.DESAFIO4= Elemento(desafio, tit="Hipátia",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA4)

                                
        self.T_AMARELO4=Elemento (triangulo_amarelo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA4)
                                
                                
        self.T_VERDE4 =Elemento (triangulo_verde, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_ROXO4 =Elemento (triangulo_roxo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_ROSA4 =Elemento (triangulo_rosa, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_LARANJA4 = Elemento (triangulo_laranja, tit="nome_do_meu_elemento", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA4)
                                   
                                   
        self.QUADRADO_VERMELHO4 = Elemento (quadrado_vermelho, tit="nome_do_meu_elemento", 
                                           h=100,w=100, x=313, y=382,
                                           cena=self.BIBLIOTECA4)
        #ELEMENTOS BIBLIOTECA 5
        
        self.DESAFIO5= Elemento(desafio, tit="Hipátia",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA5)

                                
        self.T_AMARELO5=Elemento (triangulo_amarelo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA5)
                                
                                
        self.T_VERDE5 =Elemento (triangulo_verde, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA5)
                                
        self.T_ROXO5 =Elemento (triangulo_roxo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA5)
                                
        self.T_ROSA5 =Elemento (triangulo_rosa, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA5)
                                
                                   
        self.QUADRADO_VERMELHO5 = Elemento (quadrado_vermelho, tit="nome_do_meu_elemento", 
                                           h=100,w=100, x=313, y=382,
                                           cena=self.BIBLIOTECA5)                                           
                                          
        
        #TEXTO BIBLIOTECA
        self.texto_1= Texto(self.BIBLIOTECA, txt= 'Clique na peça que se encaixa no quadrado vermelho.')
        self.texto_2= Texto(self.BIBLIOTECA, txt= 'Esta não é a peça correta.')
        self.texto_3= Texto(self.BIBLIOTECA2, txt= 'Esta não é a peça correta.')
        self.texto_4= Texto(self.BIBLIOTECA3, txt= 'Esta não é a peça correta.')
        #ELEMENTOS BIBLIOTECA 4
        
        self.DESAFIO4= Elemento(desafio, tit="Hipátia",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA4)

                                
        self.T_AMARELO4=Elemento (triangulo_amarelo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA4)
                                
                                
        self.T_VERDE4 =Elemento (triangulo_verde, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_ROXO4 =Elemento (triangulo_roxo, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_ROSA4 =Elemento (triangulo_rosa, tit="nome_do_meu_elemento", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_LARANJA4 = Elemento (triangulo_laranja, tit="nome_do_meu_elemento", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA4)
                                   
                                   
        self.QUADRADO_VERMELHO4 = Elemento (quadrado_vermelho, tit="nome_do_meu_elemento", 
                                           h=100,w=100, x=313, y=382,
                                           cena=self.BIBLIOTECA4)
        #BOTAO BIBLIOTECA 1
        self.T_CIANO.elt.bind("click", self.desafio1)
        self.T_AZUL.elt.bind("click", self.botao_errado)
        self.T_VERMELHO.elt.bind("click", self.botao_errado)
        self.T_AMARELO.elt.bind("click", self.botao_errado)
        self.T_VERDE.elt.bind("click", self.botao_errado)
        self.T_ROXO.elt.bind("click", self.botao_errado)
        self.T_ROSA.elt.bind("click", self.botao_errado)
        self.T_LARANJA.elt.bind("click", self.botao_errado)
        
        #BOTAO BIBLIOTECA2
        self.T_AZUL2.elt.bind("click", self.desafio2)
        self.T_VERMELHO2.elt.bind("click", self.botao_errado2)
        self.T_AMARELO2.elt.bind("click", self.botao_errado2)
        self.T_VERDE2.elt.bind("click", self.botao_errado2)
        self.T_ROXO2.elt.bind("click", self.botao_errado2)
        self.T_ROSA2.elt.bind("click", self.botao_errado2)
        self.T_LARANJA2.elt.bind("click", self.botao_errado2)
        
        #BOTAOBIBLIOTECA3
        self.T_VERMELHO3.elt.bind("click", self.desafio3)
        self.T_AMARELO3.elt.bind("click", self.botao_errado3)
        self.T_VERDE3.elt.bind("click", self.botao_errado3)
        self.T_ROXO3.elt.bind("click", self.botao_errado3)
        self.T_ROSA3.elt.bind("click", self.botao_errado3)
        self.T_LARANJA3.elt.bind("click", self.botao_errado3)
        
        #BOTAOBIBLIOTECA4

        self.T_AMARELO4.elt.bind("click", self.botao_errado4)
        self.T_VERDE4.elt.bind("click", self.botao_errado4)
        self.T_ROXO4.elt.bind("click", self.botao_errado4)
        self.T_ROSA4.elt.bind("click", self.botao_errado4)
        self.T_LARANJA4.elt.bind("click", self.desafio4)
        
        
        
    def desafio1(self,*_):
        self.BIBLIOTECA2.vai()
        
        
        
    def botao_errado(self,*_):
        self.texto_2.vai()
        
    def desafio2(self,*_):
        self.BIBLIOTECA3.vai()
        
        
    def botao_errado2(self,*_):
        self.texto_3.vai()
        
    def desafio3(self,*_):
        self.BIBLIOTECA4.vai()
        
        
    def botao_errado3(self,*_):
        self.texto_4.vai()

    def desafio4(self,*_):
        self.BIBLIOTECA5.vai()
        
        
    def botao_errado4(self,*_):
        self.texto_5.vai()
        
    def inicia(self,*_):
        self.BIBLIOTECA.vai()
        self.texto_1.vai()

if __name__ == "__main__":
    desafio_teorema().inicia()