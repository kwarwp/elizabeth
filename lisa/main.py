# elizabeth.lisa.main.py

from _spy.vitollino.main import Cena, Texto, STYLE, Elemento


STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

corredor= "https://i.imgur.com/oO8m0Bq.png"
corredor2="https://i.imgur.com/YzJB15Y.png"
resposta_a= "https://i.imgur.com/Ny4x06n.png"
resposta_b= "https://i.imgur.com/B28Eot5.png"
resposta_c= "https://i.imgur.com/FWrKaip.png"


class desafio_quadrado():

    def __init__(self):
        self.CORREDOR= Cena(corredor)
        self.CORREDOR2= Cena(corredor2)
        
        #ELEMENTOS
        self.RESPOSTA_A= Elemento(resposta_a, tit="Click",
                                  w=139,h=171, x=750, y=50, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                  cena = self.CORREDOR)
                               
        self.RESPOSTA_B= Elemento(resposta_b, tit="Click",
                                  w=139,h=171, x=750, y=250, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                  cena = self.CORREDOR)
        self.RESPOSTA_C= Elemento(resposta_c, tit="Click",
                                  w=139,h=171, x=750, y=450, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                  cena = self.CORREDOR)
        
        
        self.texto_1= Texto(self.CORREDOR, txt= 'Ao tentar fugir, Hipátia se deparou com um dessafio. Resolvá-o encaixando a peça correta')
        self.texto_2= Texto(self.CORREDOR, txt= 'Esta não é a peça correta.')
        self.texto_3= Texto(self.CORREDOR2, txt= 'Parabéns! Você concluiu o desafio!')
        #botao
    
        self.RESPOSTA_B.elt.bind("click", self.desafio1)
        self.RESPOSTA_A.elt.bind("click", self.botao_errado)
        self.RESPOSTA_C.elt.bind("click", self.botao_errado)
    
    def desafio1(self,*_):
        self.CORREDOR2.vai()
        self.texto_3.vai()
        
    def botao_errado(self,*_):
        self.texto_2.vai()
    
    def inicia(self,*_):
        self.CORREDOR.vai()
        self.texto_1.vai()
    
if __name__ == "__main__":
    desafio_quadrado().inicia()