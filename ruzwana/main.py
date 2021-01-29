# Ato 3

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

porta_adm= 'https://a-static.besthdwallpaper.com/decoracao-da-porta-bonita-papel-de-parede-10187_L.jpg'
sala_adm= 'https://www.galeriadaarquitetura.com.br/img/ambiente/368x285/6041/243014_bibliotecas-e-salas-de-leitura.jpg'
computador= 'https://s2.glbimg.com/of-wm12tGeAcF_chWnw-0wlWP6E=/0x0:695x522/695x522/s.glbimg.com/po/tt/f/original/2014/02/13/inspiron-3000-e-nova-linha-de-desktop-compacto-com-processador-haswell.jpg'
Imagem_botao="https://images-na.ssl-images-amazon.com/images/I/71nQDXqkyDL.png"
pasta_confidencial= 'https://comps.canstockphoto.com.br/foto-pasta-arquivo-vetor-clip-arte_csp32469962.jpg'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class desafio_3:

    def __init__(self):
        self.ENTRADA_ADM = Cena(porta_adm)        
        self.ADM= Cena(sala_adm)
        
        self.BOTAO= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.ENTRADA_ADM)
                                
        
        self.BOTAO.elt.bind("click", self.abre_porta)
        
        self.texto_1=Texto(self.ENTRADA_ADM, txt = 'Parabéns, Hipátia! Você conseguiu escapar. Entre na diretoria da biblioteca para mais informações')
        
        self.PASTA= Elemento(pasta_confidencial, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.ADM)
                             
        self.texto_2=Texto(self.ADM, txt = 'Encontre a pasta confidencial.')
        
        
#        self.COMPUTADOR= Elemento(computador, tit="click",
#                             w=55,h=58, x=850, y=390, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
#                            cena = self.QUARTO2)

    def abre_porta (self,event = None):
        self.ADM.vai()
        
        
    def inicia(self,*_):
        self.ENTRADA_ADM.vai()
        self.texto_1.vai()

if __name__ == "__main__":                  
    desafio_3().inicia()