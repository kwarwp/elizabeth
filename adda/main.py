# elizabeth.adda.main.py
# ato4

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala

imagem_cabanafora = 'https://i.imgur.com/3qeO1qP.jpg'
imagem_cabanadentro1 = 'https://i.imgur.com/OZGjgtL.png'
imagem_porta = 'https://i.imgur.com/f1yocCX.png'


STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class ATO4:

    def __init__(self):
    
        self.CABANA_FORA = Cena(imagem_cabanafora)
        self.CABANA_DENTRO1 = Cena(imagem_cabanadentro1)
        
        
        self.PORTA = Elemento(imagem_porta, tit="CLIQUE",
                              w=35,h=120, x=660, y=250,
                              cena = self.CABANA_FORA)
                             

                             
        self.texto_1 = Texto(self.CABANA_FORA, txt= "Clique na porta para entrar na cabana.")
        self.texto_2 = Texto(self.CABANA_DENTRO1, txt= "Ao entrar, Hipátia se deparou com alguém e se espantou. Era sua mãe. Clique na mãe da Hipátia para saber o que ela tem a dizer.")
        

        
                             
    def inicia(self,*_):
        self.CABANA_FORA.vai()
        self.texto_1.vai()
        

        
if __name__ == "__main__":  
    ATO4().inicia()                    
                             
        