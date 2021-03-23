# Ato 3

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

porta_adm= 'https://i.imgur.com/TrrsagT.jpeg'
sala_adm= 'https://i.imgur.com/Zntc84W.jpeg'
computador= "https://i.imgur.com/0KB7GXx.jpg"
porta="https://i.imgur.com/QJvPpt9.png"
pasta_confidencial= 'https://i.imgur.com/dVY2hl0.png'
pasta_aberta = 'https://i.imgur.com/fAZgWdr.png'
imagem_desafiocodigo = 'https://i.imgur.com/fAZgWdr.png'
seta= 'https://image.flaticon.com/icons/png/512/37/37758.png'
botao_play= "https://i.imgur.com/4IFbhfb.png"
coordenadas = ""

imagem_boneca2 = 'https://i.imgur.com/NEyFwDm.png'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class desafio_3:

    def __init__(self):
        self.ENTRADA_ADM = Cena(porta_adm)        
        self.ADM= Cena(sala_adm)
        self.PASTA_ABERTA= Cena(pasta_aberta)
        self.DESAFIO_CODIGO = Cena(imagem_desafiocodigo)
        self.COMPUTADOR = Cena(computador)
        
        self.PORTA1= Elemento(porta, tit="Abra a porta",
                             w=200,h=400,  x=460, y=70, 
                             cena = self.ENTRADA_ADM)
        self.PASTA= Elemento(pasta_confidencial, tit="Abra a pasta",
                             w=30,h=10,  x=380, y=400, 
                             cena = self.ADM)
        self.PLAY = Elemento(botao_play, tit="PLAY",
                             w=30, h=36, x=450, y=300,
                             cena= self.PASTA_ABERTA)
        self.SETA = Elemento(seta, tit="SEGUIR",
                             w=30, h=36, x=450, y=300,
                             cena= self.DESAFIO_CODIGO)
                             
        self.BONECA1= Elemento(imagem_boneca2, tit="Hipátia",
                               w=300,h=400, x=100, y=240, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.ENTRADA_ADM)  
                               
        self.BONECA2= Elemento(imagem_boneca2, tit="Hipátia",
                               w=300,h=400, x=100, y=240, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.ADM)  
                               
        self.SENHA= 
        
        self.PORTA1.elt.bind("click", self.abre_porta)
        self.PASTA.elt.bind("click", self.abre_pasta)
        self.PLAY.elt.bind("click", self.desafio_codigo)
        self.SETA.elt.bind("click", self.botao_seguir)
        
        self.texto_1=Texto(self.ENTRADA_ADM, txt = 'Parabéns, Hipátia! Você conseguiu escapar. Entre na diretoria da biblioteca para mais informações')
        self.texto_2=Texto(self.ADM, txt = 'Encontre a pasta confidencial.')
        self.texto_3=Texto(self.PASTA_ABERTA, txt = "Após ler as informações, Hipátia percebeu que havia um código para ser resolvido. Clique no botão para descobrir o que é.")
        self.texto_4=Texto(self.DESAFIO_CODIGO, txt = "Descubra o código e anote-o. Hipátia precisará dele para seu próximo passo.")
        self.texto_5=Texto(self.COMPUTADOR, txt = "Insira o código descoberto na última etapa.")
        
    def botao_seguir (self, event = None):
        self.COMPUTADOR.vai()
        self.texto_5.vai()
        
    def desafio_codigo (self,event = None):
        self.DESAFIO_CODIGO.vai()
        self.texto_4.vai()
        
    def abre_pasta (self,event = None):
        self.PASTA_ABERTA.vai()
        self.texto_3.vai()

    def abre_porta (self,event = None):
        self.ADM.vai()
        self.texto_2.vai()
        
    def inicia(self,*_):
        self.ENTRADA_ADM.vai()
        self.texto_1.vai()

if __name__ == "__main__":                  
    desafio_3().inicia()