# elizabeth.adda.main.py
# ato4

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala

imagem_cabanafora = 'https://i.imgur.com/3qeO1qP.jpg'
imagem_porta = 'https://i.imgur.com/f1yocCX.png'
imagem_cabanadentro1 = 'https://i.imgur.com/r7WL6jW.jpeg'
imagem_cabanadentro2 = 'https://i.imgur.com/O610LO7.jpeg'
imagem_cabanadentro3 = 'https://i.imgur.com/ax5lNR8.jpeg'
imagem_cabanadentro4 = 'https://i.imgur.com/5eWOp3i.jpeg'
imagem_cabanadentro5 = 'https://i.imgur.com/qx1sdZ8.jpeg'
imagem_reuniao = 'https://i.imgur.com/tzvaPBC.jpeg'
imagem_seta1 = 'https://image.flaticon.com/icons/png/512/37/37758.png'


STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class ATO4:

    def __init__(self):
    
        self.CABANA_FORA = Cena(imagem_cabanafora)
        self.CABANA_DENTRO1 = Cena(imagem_cabanadentro1)
        self.CABANA_DENTRO2 = Cena(imagem_cabanadentro2)
        self.CABANA_DENTRO3 = Cena(imagem_cabanadentro3)
        self.CABANA_DENTRO4 = Cena(imagem_cabanadentro4)
        self.CABANA_DENTRO5 = Cena(imagem_cabanadentro5)
        self.SALA_REUNIAO = Cena(imagem_reuniao)
        
        
        self.PORTA = Elemento(imagem_porta, tit="CLIQUE",
                              w=35,h=120, x=655, y=220,
                              cena = self.CABANA_FORA)

        self.SETA_1 = Elemento(imagem_seta1, tit="CLIQUE",
                              w=55,h=58, x=900, y=420,
                              cena = self.CABANA_DENTRO1)
                             
        self.SETA_2 = Elemento(imagem_seta1, tit="CLIQUE",
                              w=55,h=58, x=900, y=420,
                              cena = self.CABANA_DENTRO2)

        self.SETA_3 = Elemento(imagem_seta1, tit="CLIQUE",
                              w=55,h=58, x=900, y=420,
                              cena = self.CABANA_DENTRO3)

        self.SETA_4 = Elemento(imagem_seta1, tit="CLIQUE",
                              w=55,h=58, x=900, y=420,
                              cena = self.CABANA_DENTRO4)
                              
        self.SETA_5 = Elemento(imagem_seta1, tit="CLIQUE",
                              w=55,h=58, x=900, y=420,
                              cena = self.CABANA_DENTRO5)
                              
        self.texto_1 = Texto(self.CABANA_FORA, txt= "Clique na porta para entrar na cabana.")
        
        self.PORTA.elt.bind("click", self.PORTA_ABRE)
        self.SETA_1.elt.bind("click", self.DIALOGO1)
        self.SETA_2.elt.bind("click", self.DIALOGO2)
        self.SETA_3.elt.bind("click", self.DIALOGO3)
        self.SETA_4.elt.bind("click", self.DIALOGO4)
        self.SETA_5.elt.bind("click", self.REUNIAO)

        
                             
    def inicia(self,*_):
        self.CABANA_FORA.vai()
        self.texto_1.vai()
        
    def PORTA_ABRE(self,*_):
        self.CABANA_DENTRO1.vai()       
        
    def DIALOGO1(self,*_):
        self.CABANA_DENTRO2.vai()
        
    def DIALOGO2(self,*_):
        self.CABANA_DENTRO3.vai()
        
    def DIALOGO3(self,*_):
        self.CABANA_DENTRO4.vai()
        
    def DIALOGO4(self,*_):
        self.CABANA_DENTRO5.vai()
        
    def REUNIAO(self,*_):
        self.SALA_REUNIAO.vai()
        
if __name__ == "__main__":  
    ATO4().inicia()                    
                             
        