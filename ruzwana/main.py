# Ato 3

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

porta_adm= 'https://i.imgur.com/TrrsagT.jpeg'
sala_adm= 'https://www.galeriadaarquitetura.com.br/img/ambiente/368x285/6041/243014_bibliotecas-e-salas-de-leitura.jpg'
computador= 'https://s2.glbimg.com/of-wm12tGeAcF_chWnw-0wlWP6E=/0x0:695x522/695x522/s.glbimg.com/po/tt/f/original/2014/02/13/inspiron-3000-e-nova-linha-de-desktop-compacto-com-processador-haswell.jpg'
Imagem_botao="https://images-na.ssl-images-amazon.com/images/I/71nQDXqkyDL.png"
pasta_confidencial= 'https://comps.canstockphoto.com.br/foto-pasta-arquivo-vetor-clip-arte_csp32469962.jpg'
pasta_aberta = 'https://i.imgur.com/8kggT8B.png'
botao_play = 'https://i.imgur.com/74ZZX5s.png'
imagem_desafiocodigo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8hnuTypcbATIdbgeCmywkqxgaCbd9lA6u1w&usqp=CAU'
seta= 'https://image.flaticon.com/icons/png/512/37/37758.png'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class desafio_3:

    def __init__(self):
        self.ENTRADA_ADM = Cena(porta_adm)        
        self.ADM= Cena(sala_adm)
        self.PASTA_ABERTA= Cena(pasta_aberta)
        self.DESAFIO_CODIGO = Cena(imagem_desafiocodigo)
        self.COMPUTADOR = Cena(computador)
        
        self.BOTAO= Elemento(Imagem_botao, tit="Abra a porta",
                             w=30,h=36,  x=450, y=300, 
                             cena = self.ENTRADA_ADM)
        self.PASTA= Elemento(pasta_confidencial, tit="Abra a pasta",
                             w=60,h=72,  x=450, y=300, 
                             cena = self.ADM)
        self.PLAY = Elemento(botao_play, tit="PLAY",
                             w=30, h=36, x=450, y=300,
                             cena= self.PASTA_ABERTA)
        self.SETA = Elemento(seta, tit="SEGUIR",
                             w=30, h=36, x=450, y=300,
                             cena= self.DESAFIO_CODIGO)
        
        self.BOTAO.elt.bind("click", self.abre_porta)
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