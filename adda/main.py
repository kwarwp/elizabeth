# elizabeth.adda.main.py
# ato4

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala

imagem_cabanafora = 'https://i.imgur.com/3qeO1qP.jpg'
imagem_porta = 'https://i.imgur.com/f1yocCX.png'
imagem_cabanadentro1 = 'https://i.imgur.com/OZGjgtL.png'
imagem_cabanadentro2 = 'https://i.imgur.com/OZGjgtL.png'
imagem_cabanadentro3 = 'https://i.imgur.com/OZGjgtL.png'
imagem_cabanadentro4 = 'https://i.imgur.com/OZGjgtL.png'
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
                              
        self.texto_1 = Texto(self.CABANA_FORA, txt= "Clique na porta para entrar na cabana.")
        self.texto_2 = Texto(self.CABANA_DENTRO1, txt= "Ao entrar, Hipátia se deparou com alguém e se espantou. Era sua mãe. Clique na seta para saber o que a mãe da Hipátia tem a dizer.")
        self.texto_3 = Texto(self.CABANA_DENTRO2, txt= "TEXTO PROVISORIO DE TESTE - CENA PRIMEIRO DIALOGO")
        self.texto_4 = Texto(self.CABANA_DENTRO3, txt= "TEXTO PROVISORIO DE TESTE - CENA SEGUNDO DIALOGO")
        self.texto_5 = Texto(self.CABANA_DENTRO4, txt= "TEXTO PROVISORIO DE TESTE - CENA TERCEIRO DIALOGO")
        
        self.PORTA.elt.bind("click", self.PORTA_ABRE)
        self.SETA_1.elt.bind("click", self.DIALOGO1)
        self.SETA_2.elt.bind("click", self.DIALOGO2)
        self.SETA_3.elt.bind("click", self.DIALOGO3)
        self.SETA_4.elt.bind("click", self.REUNIAO)

        
                             
    def inicia(self,*_):
        self.CABANA_FORA.vai()
        self.texto_1.vai()
        
    def PORTA_ABRE(self,*_):
        self.CABANA_DENTRO1.vai()
        self.texto_2.vai()       
        
    def DIALOGO1(self,*_):
        self.CABANA_DENTRO2.vai()
        self.texto_3.vai()
        
    def DIALOGO2(self,*_):
        self.CABANA_DENTRO3.vai()
        self.texto_4.vai()
        
    def DIALOGO3(self,*_):
        self.CABANA_DENTRO4.vai()
        self.texto_5.vai()
        
    def REUNIAO(self,*_):
        self.SALA_REUNIAO.vai()
        
if __name__ == "__main__":  
    ATO4().inicia()                    
                             
        