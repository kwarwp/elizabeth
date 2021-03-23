# elizabeth.courtney.main.py
# ATO 2

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto, Sala

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
seguranca = "https://i.imgur.com/z5TxOgI.png"
imagem_botaoajuda = 'https://i.imgur.com/jALMQz4.png'

personagem_assustada= "https://i.imgur.com/2G9fv6S.png"
personagem_correndo = "https://i.imgur.com/FotzDIP.png"

corredor0= "https://i.imgur.com/sGkRK9T.png"
porta= "https://i.imgur.com/QJvPpt9.png"

corredor= "https://i.imgur.com/oO8m0Bq.png"
corredor2="https://i.imgur.com/YzJB15Y.png"
resposta_a= "https://i.imgur.com/Ny4x06n.png"
resposta_b= "https://i.imgur.com/B28Eot5.png"
resposta_c= "https://i.imgur.com/FWrKaip.png"

continua= "https://ffdiamantes.webnode.com/_files/200000009-d4d18d5c9f/continue-png-4.png"

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class desafio_2:

    def __init__(self):
    
        #Cenas
        
        self.Biblioteca_dentro1=Cena(Imagem_Biblioteca_dentro)
        
        self.Biblioteca_dentro2=Cena(Imagem_Biblioteca_dentro)
        
        self.Biblioteca_dentro3=Cena(Imagem_Biblioteca_dentro)
        
        self.biblioteca2= Cena (imagem_biblioteca2)
        
        self.biblioteca3= Cena (imagem_biblioteca2)
        
        self.biblioteca4= Cena (imagem_biblioteca2)
        
        self.biblioteca5= Cena (imagem_biblioteca2)
        
        self.biblioteca6= Cena (imagem_biblioteca2)
        
        self.biblioteca7= Cena (imagem_biblioteca2)
        
        self.caixa_abre = Cena(imagem_papel)
        
        
        #Elementos
                       

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
                               
        self.BONECA8= Elemento(personagem_assustada, tit="CLICK",
                               w=250,h=350, x=350, y=250, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca4)
        
        
        self.BONECA9= Elemento(personagem_correndo, tit="CLICK",
                               w=250,h=350, x=450, y=250, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca5)
                               
        self.BONECA10= Elemento(personagem_correndo, tit="CLICK",
                               w=250,h=350, x=550, y=250, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca6)    
        
        self.BONECA11= Elemento(personagem_correndo, tit="CLICK",
                               w=250,h=350, x=650, y=250, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca7)
                                        
        self.SEGURANCA= Elemento(seguranca, tit="Corra!!!!",
                               w=250,h=350, x=100, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca4)  
        
        self.SEGURANCA2= Elemento(seguranca, tit="Corra!!!!",
                               w=250,h=350, x=100, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca5)  
        
        self.SEGURANCA3= Elemento(seguranca, tit="Corra!!!!",
                               w=250,h=350, x=100, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca6)  
        
        self.SEGURANCA4= Elemento(seguranca, tit="Corra!!!!",
                               w=250,h=350, x=100, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.biblioteca7)  
                               
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

        self.texto_3=Texto(self.Biblioteca_dentro1, txt= "Abra a caixa e colete as informações." )
        self.texto_4=Texto(self.Biblioteca_dentro3, txt= "Vá até a outra sala clicando à direita da imagem e colete mais informações." )
        self.texto_5=Texto(self.biblioteca4, txt= "CORRAAA!! O SEGURANÇA ESTÁ ATRÁS DE VOCÊ!!! CLICK EM HIPATIA " )

        #Click
        

        self.CAIXA_ABERTA.elt.bind("click", self.CAIXA_ABRE)
        self.SETA.elt.bind("click", self.funcao_de_acao_do_botao3)
        self.informacoes.elt.bind("click", self.funcao_de_acao_do_botao4)
        self.BONECA8.elt.bind("click", self.CORRE)
        self.BONECA9.elt.bind("click", self.CORRE1)
        self.BONECA10.elt.bind("click", self.CORRE2)
        self.BONECA11.elt.bind("click", self.CORRE3)
        
        #DESAFIO DO QUADRADO MAGICO
        
        self.CORREDOR0= Cena(corredor0)
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
                                    
        self.PORTA2= Elemento(porta, tit= "CLICK",
                              w=90, h=210, x=420, y=210,
                              cena= self.CORREDOR0)
                              
        self.BONECA12= Elemento(personagem_correndo, tit="CLICK",
                                w=250,h=350, x=300, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                cena = self.CORREDOR0)

                              
        self.CONTINUA = Elemento(continua, tit="Próximo",
                                 w=100,h=60, x=600, y=550,
                                 cena = self.CORREDOR2)
                                 
        self.BOTAO_AJUDA = Elemento(imagem_botaoajuda, tit="PLAY",
                                      w=55,h=58, x=200, y=100,
                                      cena = self.CORREDOR)
        
        
        self.texto_1_1= Texto(self.CORREDOR, txt= 'Ao tentar fugir, Hipátia se deparou com um desafio. Resolvá-o encaixando a peça correta')
        self.texto_1_2= Texto(self.CORREDOR0, txt= 'Entre pela porta principal para despistar o segurança.')
        self.texto_2_2= Texto(self.CORREDOR, txt= 'Esta não é a peça correta.')
        self.texto_3_3= Texto(self.CORREDOR2, txt= 'Parabéns! Você concluiu o desafio!')
        self.texto_5 = Texto(self.CORREDOR, txt = "O desafio é um quadrado mágico. Todas as linhas, colunas e diagonais devem somar o mesmo valor. Tente somar os valores dos exemplos para descobrir qual possui as propriedades de um quadrado mágico.")
        
        #botao
    
        self.RESPOSTA_B.elt.bind("click", self.desafio1)
        self.RESPOSTA_A.elt.bind("click", self.botao_errado)
        self.RESPOSTA_C.elt.bind("click", self.botao_errado)
        self.PORTA2.elt.bind("click", self.abre_porta2)
        self.BOTAO_AJUDA.elt.bind("click", self.AJUDA)
    
    def desafio1(self,*_):
        self.CORREDOR2.vai()
        self.texto_3_3.vai()
        
    def botao_errado(self,*_):
        self.texto_2_2.vai()
    

    def abre_porta (self,event = None):
        self.Biblioteca_porta.vai()
        self.texto_2.vai()
        
    def CORRE (self,event = None):
        self.biblioteca5.vai()
        
    def CORRE1 (self,event = None):
        self.biblioteca6.vai()
        
    def CORRE2 (self,event = None):
        self.biblioteca7.vai()
        
    def CORRE3 (self,event = None):
        self.CORREDOR0.vai()
        self.texto_1_2.vai()
        
    def abre_porta2 (self, event= None):
        self.CORREDOR.vai()
        self.texto_1_1.vai()    
         


    def clique_caixa (self,event = None):
        self.Biblioteca_dentro2.vai()
        
        
    
    def CAIXA_ABRE (self,event = None):
        self.caixa_abre.vai()
        
    def funcao_de_acao_do_botao3(self,event = None):
        self.BIBLIOTECA2.norte.vai()
        self.texto_4.vai()
        
    def funcao_de_acao_do_botao4(self,event = None):
        self.biblioteca4.vai()
        self.texto_5.vai()
        
        
        
    def chama_elemento(self,event=None):
        self.biblioteca3.vai()

        
    
    def inicia(self,*_):
        self.Biblioteca_dentro1.vai()
        self.texto_3.vai()
        
    def AJUDA(self,event = None):
        self.texto_5.vai()
        
if __name__ == "__main__":                  
    desafio_2().inicia()

