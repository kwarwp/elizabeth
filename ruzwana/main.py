# Ato 3

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

porta_adm= 'https://i.imgur.com/TrrsagT.jpeg'
sala_adm= 'https://i.imgur.com/Zntc84W.jpeg'
computador= "https://i.imgur.com/0KB7GXx.jpg"
porta="https://i.imgur.com/QJvPpt9.png"
pasta_confidencial= 'https://i.imgur.com/dVY2hl0.png'
carta = 'https://i.imgur.com/fAZgWdr.png'
seta= 'https://image.flaticon.com/icons/png/512/37/37758.png'
botao_play= "https://i.imgur.com/4IFbhfb.png"
coordenadas = "https://i.imgur.com/ZEUoh7x.png"
coordenadas_rj= "https://i.imgur.com/dKLFxWB.png"
mapa= "https://i.imgur.com/E2MZ6DR.png"
click_biblioteca= 'https://i.imgur.com/ZKiFXHh.png'
click_cabana="https://i.imgur.com/ueEjt2c.png"
pasta= "https://i.imgur.com/KeffUYv.png"
jornal= "https://i.imgur.com/WuKy09p.png"
carta_aberta= "https://i.imgur.com/LVH8eyX.png"

imagem_boneca2 = 'https://i.imgur.com/NEyFwDm.png'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


class desafio_3:

    def __init__(self):
        self.ENTRADA_ADM = Cena(porta_adm)        
        self.ADM= Cena(sala_adm)
        self.ADM2= Cena(sala_adm)
        self.ADM3= Cena(sala_adm)
        self.COMPUTADOR = Cena(computador)
        self.COMPUTADOR2 = Cena(computador)
        self.MAPA= Cena(mapa)
        
        self.PORTA1= Elemento(porta, tit="Abra a porta",
                             w=200,h=400,  x=460, y=70, 
                             cena = self.ENTRADA_ADM)
        self.PASTA_FECHADA= Elemento(pasta_confidencial, tit="Abra a pasta",
                             w=50,h=20,  x=380, y=400, 
                             cena = self.ADM)

                             
        self.BONECA1= Elemento(imagem_boneca2, tit="Hipátia",
                               w=300,h=400, x=100, y=240, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.ENTRADA_ADM)  
                               
        self.BONECA2= Elemento(imagem_boneca2, tit="Hipátia",
                               w=300,h=400, x=100, y=240, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.ADM)  
                               
        self.BONECA3= Elemento(imagem_boneca2, tit="Hipátia",
                               w=300,h=400, x=100, y=240, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.ADM2) 
                               
        self.BONECA4= Elemento(imagem_boneca2, tit="Hipátia",
                               w=300,h=400, x=100, y=240, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.ADM3) 
                               
        self.SENHA= Elemento(coordenadas, tit="Coordenada",
                               w=500,h=264, x=240, y=140, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.COMPUTADOR)  
        self.SENHA2= Elemento(coordenadas_rj, tit="Coordenada",
                               w=500,h=264, x=240, y=140, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.COMPUTADOR2) 
                               
        self.mini_mapa= Elemento(mapa, tit="Mini Mapa",
                               w=100,h=50, x=240, y=140, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.COMPUTADOR2)
                               
        self.BIBLIOTECA= Elemento(click_biblioteca, tit="CLICK",
                                  w=55,h=58, x=610, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                  cena = self.MAPA)      
        self.CABANA= Elemento(click_cabana, tit="CLICK",
                              w=55,h=58, x=250, y=500, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                              cena = self.MAPA)  
                              
                              
        self.PASTA_ABERTA= Elemento (pasta, tit="pasta",
                                     w=700, h=450, x=100, y=100,
                                     cena= self.ADM2)
                                     
        self.PASTA_ABERTA2= Elemento (pasta, tit="pasta",
                                      w=700, h=450, x=100, y=100,
                                      cena= self.ADM3)
                              
        self.CARTA= Elemento (carta, tit="carta",
                              w=300, h=200, x=480, y=240,
                              cena= self.ADM2)
                              
        self.CARTA_ABERTA= Elemento (carta_aberta, tit="carta",
                                     w=300, h=450, x=480, y=100,
                                     cena= self.ADM3)
                                     
        self.JORNAL= Elemento(jornal, tit= "Jornal",
                              w=350, h=300, x=50, y=150,
                              cena=self.ADM2)
        
        self.JORNAL2= Elemento(jornal, tit= "Jornal",
                              w=350, h=300, x=50, y=150,
                              cena=self.ADM3)
                              
        self.SETA = Elemento(seta, tit="SEGUIR",
                             w=30, h=36, x=450, y=300,
                             cena= self.ADM3)
                              
        

        
        self.PORTA1.elt.bind("click", self.abre_porta)
        self.PASTA_FECHADA.elt.bind("click", self.abre_pasta)
        self.SETA.elt.bind("click", self.botao_seguir)
        self.SENHA.elt.bind("click", self.desafio4)
        self.mini_mapa.elt.bind("click", self.abre_mapa)
        self.CARTA.elt.bind("click", self.abre_carta)
        
        self.texto_1=Texto(self.ENTRADA_ADM, txt = 'Parabéns, Hipátia! Você conseguiu escapar. Entre na diretoria da biblioteca para mais informações')
        self.texto_2=Texto(self.ADM, txt = 'Encontre a pasta confidencial.')
        self.texto_3=Texto(self.ADM2, txt = "Após ler as informações, Hipátia percebeu que havia uma carta. Clique para descobrir o que esta escrito.")
        self.texto_4=Texto(self.ADM3, txt = "Descubra o código e anote-o. Hipátia precisará dele para seu próximo passo.")
        self.texto_5=Texto(self.COMPUTADOR, txt = "Insira o código descoberto na última etapa.")
        self.texto_6=Texto(self.MAPA, txt = "Vá até a cabana.")
        
    def botao_seguir (self, event = None):
        self.COMPUTADOR.vai()
        self.texto_5.vai()
        
    def abre_mapa (self, event= None):
        self.MAPA.vai()
        self.texto_6.vai()
    
    def abre_carta (self, event= None):
        self.ADM3.vai()
        self.texto_4.vai()
    
    def desafio4 (self, event = None):
        self.digite_senha= input("Digite a senha do computador para liberar a coordenada.")
        if self.digite_senha == "749182":
            self.COMPUTADOR2.vai()
            self.parabens= Texto(self.COMPUTADOR2, txt= "Você conseguiu logar no computador, click no mini mapa para ser direcionado até a cabana")
            self.parabens.vai()
        else:
            self.tente_novamente2=Texto(self.COMPUTADOR, txt = 'Hipátia, tente novamente.')
            self.tente_novamente2.vai()

        
    def abre_pasta (self,event = None):
        self.ADM2.vai()
        self.texto_3.vai()

    def abre_porta (self,event = None):
        self.ADM.vai()
        self.texto_2.vai()
        
    def inicia(self,*_):
        self.ENTRADA_ADM.vai()
        self.texto_1.vai()

if __name__ == "__main__":                  
    desafio_3().inicia()