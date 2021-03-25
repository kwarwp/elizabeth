# elizabeth.adda.main.py
# ato4

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala

imagem_cabanafora = 'https://i.imgur.com/l1LeZ9x.jpg'
imagem_cabanadentro1 = 'https://i.imgur.com/o7cml0T.jpeg'
imagem_cabanadentro2 = 'https://i.imgur.com/o7cml0T.jpeg'
imagem_cabanadentro3 = 'https://i.imgur.com/o7cml0T.jpeg'
imagem_cabanadentro4 = 'https://i.imgur.com/o7cml0T.jpeg'
imagem_seta = 'https://image.flaticon.com/icons/png/512/37/37758.png'
imagem_continua = 'data:image/png;base64,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'


STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class ATO4:

    def __init__(self):
    
        self.CABANA_FORA = Cena(imagem_cabanafora)
        self.DIALOGO1 = Cena(imagem_cabanadentro1)
        self.DIALOGO2 = Cena(imagem_cabanadentro2)
        self.DIALOGO3 = Cena(imagem_cabanadentro3)
        self.DIALOGO4 = Cena(imagem_cabanadentro4)
        self.CONTINUA = Cena(imagem_continua)
        
        self.SETA1 = Elemento(imagem_seta, tit="CLIQUE",
                             w=250,h=350, x=100, y=250,
                             cena = self.DIALOGO1)
                             
        self.SETA2 = Elemento(imagem_seta, tit="CLIQUE",
                             w=250,h=350, x=100, y=250,
                             cena = self.DIALOGO2)
                             
        self.SETA3 = Elemento(imagem_seta, tit="CLIQUE",
                             w=250,h=350, x=100, y=250,
                             cena = self.DIALOGO3)
                             
        self.SETA4 = Elemento(imagem_seta, tit="CLIQUE",
                             w=250,h=350, x=100, y=250,
                             cena = self.DIALOGO4) 

                             
        self.texto_1 = Texto(self.CABANA_FORA, txt= "Clique na Hipátia para entrar na cabana.")
        self.texto_2 = Texto(self.CABANA_DENTRO, txt= "Ao entrar, Hipátia se deparou com alguém e se espantou. Era sua mãe. Clique na mãe da Hipátia para saber o que ela tem a dizer.")
        
        self.SETA1.elt.bind("click", self.CENA_DIALOGO1)
        self.SETA2.elt.bind("click", self.CENA_DIALOGO2)
        self.SETA3.elt.bind("click", self.CENA_DIALOGO3)
        self.SETA4.elt.bind("click", self.CENA_DIALOGO4)
        
                             
    def inicia(self,*_):
        self.CABANA_FORA.vai()
        self.texto_1.vai()
        
    def CENA_DIALOGO1 (self,event = None):
        self.DIALOGO2.vai()
        
    def CENA_DIALOGO2 (self,event = None):
        self.DIALOGO3.vai()
        
    def CENA_DIALOGO3 (self,event = None):
        self.DIALOGO4.vai()
        
    def CENA_DIALOGO4 (self,event = None):
        self.CONTINUA.vai()
        
if __name__ == "__main__":  
    ATO4().inicia()                    
                             
        