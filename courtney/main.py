# elizabeth.courtney.main.py
# ATO 2

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala

porta_fechada="https://i.imgur.com/wistRJZ.jpeg"
porta_aberta="https://image.freepik.com/vetores-gratis/porta-aberta-dos-desenhos-animados-entrada-do-corredor-do-apartamento-entrada-do-escritorio_53562-8532.jpg"
Imagem_Biblioteca_dentro="https://i.imgur.com/l1LeZ9x.jpg"
imagem_biblioteca2="https://i.imgur.com/o7cml0T.jpeg"
imagem_caixa="https://i.imgur.com/7nnzwwN.png"
caixa_aberta= "https://i.imgur.com/grpEmod.png"
imagem_papel="https://thumbs.dreamstime.com/z/folhas-de-pap%C3%A9is-de-nota-com-o-desenho-da-m%C3%A3o-do-pino-do-impulso-89420296.jpg"
Imagem_botao="https://images-na.ssl-images-amazon.com/images/I/71nQDXqkyDL.png"
imagem_boneca2 = 'https://i.imgur.com/NEyFwDm.png'
imagem_boneca1 = 'https://i.imgur.com/alSNLX0.png'
seta= 'https://image.flaticon.com/icons/png/512/37/37758.png'
lixo= 'https://i.imgur.com/8TMfOgz.png'
caixa_vazia= 'https://i.imgur.com/4Tm4yIE.png'
infos_lixo= 'https://i.imgur.com/8kggT8B.png'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class desafio_2:

    def __init__(self):
    
        #Cenas

        self.Biblioteca_entrada=Cena(porta_fechada)
        
        self.Biblioteca_porta=Cena(porta_aberta)
        
        self.Biblioteca_dentro1=Cena(Imagem_Biblioteca_dentro)
        
        self.Biblioteca_dentro2=Cena(Imagem_Biblioteca_dentro)
        
        self.Biblioteca_dentro3=Cena(Imagem_Biblioteca_dentro)
        
        self.biblioteca2= Cena (imagem_biblioteca2)
        
        self.biblioteca3= Cena (imagem_biblioteca2)
        
        self.caixa_abre = Cena(imagem_papel)
        
        
        #Elementos
        
        self.BOTAO= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.Biblioteca_entrada)
                       
        self.BOTAO2= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                              cena = self.Biblioteca_porta)
                              
        
        self.botao_caixa = Elemento(imagem_caixa, tit="Abra a caixa",
                                    h=100, w =100, x=500, y=390, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                    cena = self.Biblioteca_dentro1,
                                    vai = self.clique_caixa)
                                    
        self.botao_caixavazia= Elemento(caixa_vazia, tit="Você já colheu informações aqui...",
                                        h=100, w =120, x=500, y=400, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                        cena = self.Biblioteca_dentro3)
                                    
        self.CAIXA_ABERTA= Elemento(caixa_aberta, tit="Colete as informações.",
                                    h=100, w =120, x=500, y=400, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                    cena = self.Biblioteca_dentro2)
         
        self.BONECA2= Elemento(imagem_boneca2, tit="Hipátia",
                               w=250,h=350, x=50, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.Biblioteca_entrada)  
                               
        self.BONECA3= Elemento(imagem_boneca1, tit="Hipátia",
                               w=250,h=350, x=700, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.Biblioteca_dentro1)  
                               
        self.BONECA4= Elemento(imagem_boneca1, tit="Hipátia",
                               w=250,h=350, x=550, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.Biblioteca_dentro2)  
                               
                               
        self.BONECA5= Elemento(imagem_boneca1, tit="Hipátia",
                               w=250,h=350, x=350, y=200, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca2)
                               
        self.BONECA6= Elemento(imagem_boneca2, tit="Hipátia",
                               w=250,h=350, x=700, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.Biblioteca_dentro3)  
                               
        self.BONECA7= Elemento(imagem_boneca1, tit="Hipátia",
                               w=250,h=350, x=350, y=200, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca3)
                               
        
        self.SETA = Elemento(seta, tit="Próximo",
                             w=55,h=58, x=900, y=420,
                             cena = self.caixa_abre)
                             
        self.LIXO= Elemento(lixo, tit="Colete as informações.",
                            h=100, w =103, x=200, y=500, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                            cena = self.biblioteca2,
                            vai=self.chama_elemento)
                            
                            
        self.LIXO2= Elemento(lixo, tit="Colete as informações.",
                            h=100, w =103, x=200, y=500, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                            cena = self.biblioteca3)
                            
        self.informacoes= Elemento(infos_lixo, tit='', 
                                   h=512, w =600, x=200, y=100,
                                   cena= self.biblioteca3)
        
                             
        
                             
                             
        #Salas
        
        self.BIBLIOTECA2 = Sala(n=self.Biblioteca_dentro3, l=self.biblioteca2)
        
        #Texto
        
        self.texto_1=Texto(self.Biblioteca_entrada, txt= "Entre na biblioteca interditada." )
        self.texto_2=Texto(self.Biblioteca_porta, txt= "A porta esta trancada. Resolva o desafio para abri-la" )
        self.texto_3=Texto(self.Biblioteca_dentro1, txt= "Abra a caixa e colete as informações." )
        self.texto_4=Texto(self.Biblioteca_dentro3, txt= "Vá até a outra sala clicando à direita da imagem e colete mais informações." )


        #Click
        
        self.BOTAO2.elt.bind("click", self.entra_na_biblioteca)
        self.BOTAO.elt.bind("click", self.abre_porta)
        self.CAIXA_ABERTA.elt.bind("click", self.CAIXA_ABRE)
        self.SETA.elt.bind("click", self.funcao_de_acao_do_botao3)
                           


    def abre_porta (self,event = None):
        self.Biblioteca_porta.vai()
        self.texto_2.vai()
    


    def entra_na_biblioteca (self,event = None):
        self.Biblioteca_dentro1.vai()
        self.texto_3.vai()
    


    def clique_caixa (self,event = None):
        self.Biblioteca_dentro2.vai()
        
        
    
    def CAIXA_ABRE (self,event = None):
        self.caixa_abre.vai()
        
    def funcao_de_acao_do_botao3(self,event = None):
        self.BIBLIOTECA2.norte.vai()
        self.texto_4.vai()
        
    def chama_elemento(self,event=None):
        self.biblioteca3.vai()

        
    
    def inicia(self,*_):
        self.Biblioteca_entrada.vai()
        self.texto_1.vai()
        
if __name__ == "__main__":                  
    desafio_2().inicia()

