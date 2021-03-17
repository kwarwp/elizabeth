# elizabeth.callie.main.py
#ato 2.1


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto


STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

triangulo_azul = "https://i.imgur.com/1NvDXiC.png"
triangulo_verde= 'https://i.imgur.com/ObjxT4w.png'
triangulo_vermelho= 'https://i.imgur.com/QaRil54.png'
triangulo_amarelo= 'https://i.imgur.com/RsWbjkx.png'
triangulo_roxo= 'https://i.imgur.com/f8e7Gkc.png'
triangulo_rosa ='https://i.imgur.com/e5FOwQd.png'
triangulo_laranja= "https://i.imgur.com/TP6Fk9b.png"
triangulo_ciano='https://i.imgur.com/wBVf9VF.png'
desafio1= 'https://i.imgur.com/3rPBqm3.png'
desafio2= 'https://i.imgur.com/v7sxY9h.png'
desafio3= 'https://i.imgur.com/b27vjRF.png'
desafio4= 'https://i.imgur.com/rckuQwS.png'
desafio5= 'https://i.imgur.com/2M08qgZ.png'
desafio6= 'https://i.imgur.com/ASx9OiY.png'
desafio7= 'https://i.imgur.com/HPZJ4vE.png'
desafio8= 'https://i.imgur.com/PrcMDw7.png'
biblioteca_faixada = "https://i.imgur.com/9JTXWZX.png" 
biblioteca_faixada2 = "https://i.imgur.com/wistRJZ.jpeg"

porta= "https://i.imgur.com/wMjyyBt.png"
imagem_boneca2 = 'https://i.imgur.com/NEyFwDm.png'
continua= "https://ffdiamantes.webnode.com/_files/200000009-d4d18d5c9f/continue-png-4.png"



class desafio_teorema():

    def __init__(self):
         
        self.Biblioteca_entrada=Cena(biblioteca_faixada)
    
        self.BIBLIOTECA=Cena(biblioteca_faixada2)
        
        self.BIBLIOTECA2=Cena(biblioteca_faixada2)
        
        self.BIBLIOTECA3=Cena(biblioteca_faixada2)
        
        self.BIBLIOTECA4=Cena(biblioteca_faixada2)
        
        self.BIBLIOTECA5=Cena(biblioteca_faixada2)
        
        self.BIBLIOTECA6=Cena(biblioteca_faixada2)
        
        self.BIBLIOTECA7=Cena(biblioteca_faixada2)
        self.BIBLIOTECA8=Cena(biblioteca_faixada2)
        
        #ELEMENTOS ATO2.1
        
        self.PORTA= Elemento(porta, tit="click", w=238, h=695,  x=350, y=-10, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.Biblioteca_entrada)
                             
        self.BONECA2= Elemento(imagem_boneca2, tit="Hipátia",
                               w=250,h=350, x=50, y=340, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.Biblioteca_entrada)  
                               
        
        
        #ELEMENTOS BIBLIOTECA
        
        self.DESAFIO= Elemento(desafio1, tit="",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA)

        self.T_AZUL=Elemento (triangulo_azul, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=100, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_AMARELO=Elemento (triangulo_amarelo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_VERMELHO =Elemento (triangulo_vermelho, tit="Monte o quebra-cabeça.", 
                                   h=80,w=80, x=300, y=150,
                                   cena=self.BIBLIOTECA)
                                
        self.T_VERDE =Elemento (triangulo_verde, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_ROXO =Elemento (triangulo_roxo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_ROSA =Elemento (triangulo_rosa, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA)
                                
        self.T_LARANJA = Elemento (triangulo_laranja, tit="Monte o quebra-cabeça.", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA)
                                   
        self.T_CIANO = Elemento (triangulo_ciano, tit="Monte o quebra-cabeça.", 
                                 h=80,w=80, x=800, y=150,
                                 cena=self.BIBLIOTECA)
                                   
                                           
        #ELEMENTOS BIBLIOTECA2
        
        self.DESAFIO2= Elemento(desafio2, tit="",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA2)

        self.T_AZUL2=Elemento (triangulo_azul, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=100, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_AMARELO2=Elemento (triangulo_amarelo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_VERMELHO2 =Elemento (triangulo_vermelho, tit="Monte o quebra-cabeça.", 
                                   h=80,w=80, x=300, y=150,
                                   cena=self.BIBLIOTECA2)
                                
        self.T_VERDE2 =Elemento (triangulo_verde, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_ROXO2 =Elemento (triangulo_roxo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_ROSA2 =Elemento (triangulo_rosa, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA2)
                                
        self.T_LARANJA2 = Elemento (triangulo_laranja, tit="Monte o quebra-cabeça.", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA2)
                                   
                                           
        #ELEMENTOS BIBLIOTECA 3
        
        self.DESAFIO3= Elemento(desafio3, tit="",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA3)

                                
        self.T_AMARELO3=Elemento (triangulo_amarelo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA3)
                                
        self.T_VERMELHO3 =Elemento (triangulo_vermelho, tit="Monte o quebra-cabeça.", 
                                   h=80,w=80, x=300, y=150,
                                   cena=self.BIBLIOTECA3)
                                
        self.T_VERDE3 =Elemento (triangulo_verde, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA3)
                                
        self.T_ROXO3 =Elemento (triangulo_roxo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA3)
                                
        self.T_ROSA3 =Elemento (triangulo_rosa, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA3)
                                
        self.T_LARANJA3 = Elemento (triangulo_laranja, tit="Monte o quebra-cabeça.", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA3)
                                   
                                           
        #ELEMENTOS BIBLIOTECA 4
        
        self.DESAFIO4= Elemento(desafio4, tit="",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA4)

                                
        self.T_AMARELO4=Elemento (triangulo_amarelo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA4)
                                
                                
        self.T_VERDE4 =Elemento (triangulo_verde, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_ROXO4 =Elemento (triangulo_roxo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_ROSA4 =Elemento (triangulo_rosa, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA4)
                                
        self.T_LARANJA4 = Elemento (triangulo_laranja, tit="Monte o quebra-cabeça.", 
                                   h=80,w=80, x=700, y=150,
                                   cena=self.BIBLIOTECA4)

        #ELEMENTOS BIBLIOTECA 5
        
        self.DESAFIO5= Elemento(desafio5, tit="",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA5)

                                
        self.T_AMARELO5=Elemento (triangulo_amarelo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=200, y=150,
                                cena=self.BIBLIOTECA5)
                                
                                
        self.T_VERDE5 =Elemento (triangulo_verde, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA5)
                                
        self.T_ROXO5 =Elemento (triangulo_roxo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA5)
                                
        self.T_ROSA5 =Elemento (triangulo_rosa, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA5)
                                
                                          
                                           
        #ELEMENTOS BIBLIOTECA 6
        
        self.DESAFIO6= Elemento(desafio6, tit="",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA6)                              
                                
        self.T_VERDE6 =Elemento (triangulo_verde, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA6)
                                
        self.T_ROXO6=Elemento (triangulo_roxo, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=500, y=150,
                                cena=self.BIBLIOTECA6)
                                
        self.T_ROSA6 =Elemento (triangulo_rosa, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA6)

                
        #ELEMENTOS BIBLIOTECA 7
        
        self.DESAFIO7= Elemento(desafio7, tit="",
                               w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                               cena = self.BIBLIOTECA7)                              
                                
        self.T_VERDE7 =Elemento (triangulo_verde, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=400, y=150,
                                cena=self.BIBLIOTECA7)
                                
        self.T_ROSA7 =Elemento (triangulo_rosa, tit="Monte o quebra-cabeça.", 
                                h=80,w=80, x=600, y=150,
                                cena=self.BIBLIOTECA7)
                                
                #ELEMENTOS BIBLIOTECA 8
        
        self.DESAFIO8= Elemento(desafio8, tit="",
                                w=300,h=300, x=310, y=280, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                cena = self.BIBLIOTECA8)   
                                          
        
        #TEXTO BIBLIOTECA
        self.texto_1_1=Texto(self.Biblioteca_entrada, txt= "Entre na biblioteca interditada." )
        self.texto_2_2=Texto(self.BIBLIOTECA, txt= "A porta esta trancada. Resolva o desafio para abri-la" )
        
        self.texto_1= Texto(self.BIBLIOTECA, txt= 'Clique na peça que se encaixa no quadrado vermelho.')
        self.texto_2= Texto(self.BIBLIOTECA, txt= 'Esta não é a peça correta.')
        self.texto_3= Texto(self.BIBLIOTECA2, txt= 'Esta não é a peça correta.')
        self.texto_4= Texto(self.BIBLIOTECA3, txt= 'Esta não é a peça correta.')
        self.texto_5= Texto(self.BIBLIOTECA4, txt= 'Esta não é a peça correta.')
        self.texto_6= Texto(self.BIBLIOTECA5, txt= 'Esta não é a peça correta.')
        self.texto_7= Texto(self.BIBLIOTECA6, txt= 'Esta não é a peça correta.')
        self.texto_8= Texto(self.BIBLIOTECA7, txt= 'Esta não é a peça correta.')
        self.texto_9= Texto(self.BIBLIOTECA8, txt= 'Parabéns! Você conseguiu completar o desafio!')

        #BOTAO BIBLIOTECA 1
        self.T_CIANO.elt.bind("click", self.desafio1)
        self.T_AZUL.elt.bind("click", self.botao_errado)
        self.T_VERMELHO.elt.bind("click", self.botao_errado)
        self.T_AMARELO.elt.bind("click", self.botao_errado)
        self.T_VERDE.elt.bind("click", self.botao_errado)
        self.T_ROXO.elt.bind("click", self.botao_errado)
        self.T_ROSA.elt.bind("click", self.botao_errado)
        self.T_LARANJA.elt.bind("click", self.botao_errado)
        
        #BOTAO BIBLIOTECA2
        self.T_AZUL2.elt.bind("click", self.desafio2)
        self.T_VERMELHO2.elt.bind("click", self.botao_errado2)
        self.T_AMARELO2.elt.bind("click", self.botao_errado2)
        self.T_VERDE2.elt.bind("click", self.botao_errado2)
        self.T_ROXO2.elt.bind("click", self.botao_errado2)
        self.T_ROSA2.elt.bind("click", self.botao_errado2)
        self.T_LARANJA2.elt.bind("click", self.botao_errado2)
        
        #BOTAOBIBLIOTECA3
        self.T_VERMELHO3.elt.bind("click", self.desafio3)
        self.T_AMARELO3.elt.bind("click", self.botao_errado3)
        self.T_VERDE3.elt.bind("click", self.botao_errado3)
        self.T_ROXO3.elt.bind("click", self.botao_errado3)
        self.T_ROSA3.elt.bind("click", self.botao_errado3)
        self.T_LARANJA3.elt.bind("click", self.botao_errado3)
        
        #BOTAOBIBLIOTECA4

        self.T_AMARELO4.elt.bind("click", self.botao_errado4)
        self.T_VERDE4.elt.bind("click", self.botao_errado4)
        self.T_ROXO4.elt.bind("click", self.botao_errado4)
        self.T_ROSA4.elt.bind("click", self.botao_errado4)
        self.T_LARANJA4.elt.bind("click", self.desafio4)

        #BOTAOBIBLIOTECA5

        self.T_AMARELO5.elt.bind("click", self.desafio5)
        self.T_VERDE5.elt.bind("click", self.botao_errado5)
        self.T_ROXO5.elt.bind("click", self.botao_errado5)
        self.T_ROSA5.elt.bind("click", self.botao_errado5)     
        
        #BOTAOBIBLIOTECA6

        self.T_VERDE6.elt.bind("click", self.botao_errado6)
        self.T_ROXO6.elt.bind("click", self.desafio6)
        self.T_ROSA6.elt.bind("click", self.botao_errado6) 
        
        #BOTAOBIBLIOTECA7

        self.T_VERDE7.elt.bind("click", self.desafio7)
        self.T_ROSA7.elt.bind("click", self.botao_errado7) 
        
        #botao ato2.1
        
        self.PORTA.elt.bind("click", self.abre_porta)
    
    def abre_porta (self,event = None):
        self.BIBLIOTECA.vai()
        self.texto_2_2.vai()
        
        
    def desafio1(self,*_):
        self.BIBLIOTECA2.vai()
        
        
        
    def botao_errado(self,*_):
        self.texto_2.vai()
        
    def desafio2(self,*_):
        self.BIBLIOTECA3.vai()
        
        
    def botao_errado2(self,*_):
        self.texto_3.vai()
        
    def desafio3(self,*_):
        self.BIBLIOTECA4.vai()
        
        
    def botao_errado3(self,*_):
        self.texto_4.vai()

    def desafio4(self,*_):
        self.BIBLIOTECA5.vai()
        
        
    def botao_errado4(self,*_):
        self.texto_5.vai()
   
    def desafio5(self,*_):
        self.BIBLIOTECA6.vai()
        
        
    def botao_errado5(self,*_):
        self.texto_6.vai()      
        
    def desafio6(self,*_):
        self.BIBLIOTECA7.vai()
        
        
    def botao_errado6(self,*_):
        self.texto_7.vai()
        
    def desafio7(self,*_):
        self.BIBLIOTECA8.vai()
        self.texto_9.vai()
        
        
    def botao_errado7(self,*_):
        self.texto_8.vai()  
        
    def inicia(self,*_):
        self.Biblioteca_entrada.vai()
        self.texto_1_1.vai()

if __name__ == "__main__":
    desafio_teorema().inicia()