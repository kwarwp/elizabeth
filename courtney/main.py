# elizabeth.courtney.main.py
# ATO 2

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

porta_fechada="https://i.imgur.com/wistRJZ.jpeg"
porta_aberta="https://image.freepik.com/vetores-gratis/porta-aberta-dos-desenhos-animados-entrada-do-corredor-do-apartamento-entrada-do-escritorio_53562-8532.jpg"
Imagem_Biblioteca_dentro="https://i.imgur.com/l1LeZ9x.jpg"
imagem_caixa="https://i.imgur.com/7nnzwwN.png"
caixa_aberta= "https://i.imgur.com/grpEmod.png"
imagem_papel="https://thumbs.dreamstime.com/z/folhas-de-pap%C3%A9is-de-nota-com-o-desenho-da-m%C3%A3o-do-pino-do-impulso-89420296.jpg"
Imagem_botao="https://images-na.ssl-images-amazon.com/images/I/71nQDXqkyDL.png"

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class desafio_2:

    def __init__(self):

        self.Biblioteca_entrada=Cena(porta_fechada)
        
        self.Biblioteca_porta=Cena(porta_aberta)
        
        self.Biblioteca_dentro=Cena(Imagem_Biblioteca_dentro)
        
        self.BOTAO= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.Biblioteca_entrada)
                                
        self.BOTAO.elt.bind("click", self.abre_porta)
        
        self.BOTAO2= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                              cena = self.Biblioteca_porta)
                              
        self.BOTAO2= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                              cena = self.Biblioteca_porta)
                                
        self.BOTAO2.elt.bind("click", self.entra_na_biblioteca)
        
        self.caixa_abre = Cena(imagem_papel)
        
        self.botao_caixa = Elemento(imagem_caixa, tit="CLIQUE",
                           style=dict(height=100,widht=100, left=300, top=250), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.Biblioteca_dentro,
                           vai = self.clique_caixa)


    def abre_porta (self,event = None):
        self.Biblioteca_porta.vai()
    


    def entra_na_biblioteca (self,event = None):
        self.Biblioteca_dentro.vai()
    


    def clique_caixa (self,event = None):
        self.caixa_abre.vai()
    
    def inicia(self,*_):
        self.Biblioteca_entrada.vai()
        
if __name__ == "__main__":                  
    desafio_2().inicia()

