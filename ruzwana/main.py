# Ato 3

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

porta_adm= 'https://a-static.besthdwallpaper.com/decoracao-da-porta-bonita-papel-de-parede-10187_L.jpg'
sala_adm= 'https://www.galeriadaarquitetura.com.br/img/ambiente/368x285/6041/243014_bibliotecas-e-salas-de-leitura.jpg'
computador= 'https://s2.glbimg.com/of-wm12tGeAcF_chWnw-0wlWP6E=/0x0:695x522/695x522/s.glbimg.com/po/tt/f/original/2014/02/13/inspiron-3000-e-nova-linha-de-desktop-compacto-com-processador-haswell.jpg'
Imagem_botao="https://images-na.ssl-images-amazon.com/images/I/71nQDXqkyDL.png"
pasta_confidencial= 'https://comps.canstockphoto.com.br/foto-pasta-arquivo-vetor-clip-arte_csp32469962.jpg'
pasta_aberta = 'data:image/jpeg;base64,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'
botao_play = 'https://i.imgur.com/74ZZX5s.png'
imagem_desafiocodigo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8hnuTypcbATIdbgeCmywkqxgaCbd9lA6u1w&usqp=CAU'
seta= 'https://image.flaticon.com/icons/png/512/37/37758.png'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class desafio_3:

    def __init__(self):
        self.ENTRADA_ADM = Cena(porta_adm)        
        self.ADM= Cena(sala_adm)
        self.PASTA_ABERTA(pasta_aberta)
        self.DESAFIO_CODIGO = Cena(imagem_desafiocodigo)
        self.COMPUTADOR = Cena(computador)
        
        self.BOTAO= Elemento(Imagem_botao, tit="Abra a porta",
                             w=30,h=36,  x=450, y=300, 
                             cena = self.ENTRADA_ADM)
        self.PASTA= Elemento(pasta_confidencial, tit="Abra a pasta",
                             w=30,h=36,  x=450, y=300, 
                             cena = self.ADM)
        self.PLAY = Elemento(botao_play, tit="PLAY",
                             w=30, h=36, x=450, y=300,
                             cena= self.PASTA_ABERTA)
        self.SETA = Elemento(seta, tit="SEGUIR",
                             w=30, h=36, x=450, y=300,
                             cena= self.DESAFIO_CODIGO)   
        
        self.BOTAO.elt.bind("click", self.abre_porta)
        self.PASTA.elt.bind("clicK", self.abre_pasta)
        self.PLAY.elt.bind("click", self.desafio_codigo)
        self.SETA.elt.bind("click", self.botao_seguir)
        
        self.texto_1=Texto(self.ENTRADA_ADM, txt = 'Parabéns, Hipátia! Você conseguiu escapar. Entre na diretoria da biblioteca para mais informações')
        self.texto_2=Texto(self.ADM, txt = 'Encontre a pasta confidencial.')
        self.texto_3=Texto(self.PASTA_ABERTA = "Após ler as informações, Hipátia percebeu que havia um código para ser resolvido. Clique no botão para descobrir o que é.")
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