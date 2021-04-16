# elizabeth.heather.main.py
#ATO 1


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from callie.main import desafio_teorema as DT   #AQUI VOCÊS TINHAM COLOCADO O NOME DO MODULO COM A PRIMEIRA LETRA MAIÚSCULA
                                                # ESSE "as DT" faz com que o objeto seja chamável. pois cria um nome local da
                                                # função do outro módulo praí
#from roxane.main import *
#from cenas.imix import Inicial
#from cenas.ik import Passeio
        
imagem_quarto = 'https://i.imgur.com/hvHCTF9.jpeg'
seta= 'https://image.flaticon.com/icons/png/512/37/37758.png'
imagem_quarto2='https://i.imgur.com/eatF6gK.jpeg'
imagem_livro = 'https://i.imgur.com/XLWFUsC.png'
imagem_livroaberto = 'https://i.imgur.com/F8BX0Aa.jpg'
botao_desafio1='https://i.imgur.com/74ZZX5s.png'
imagem_mapa ='https://i.imgur.com/E2MZ6DR.png'
click_biblioteca= 'https://i.imgur.com/ZKiFXHh.png'
imagem_boneca1 = 'https://i.imgur.com/xTthXnC.png'
imagem_livroerrado = 'https://i.imgur.com/kP9br1f.png'
imagem_boneca2 = 'https://i.imgur.com/NEyFwDm.png'
imagem_computador = "https://i.imgur.com/7LHPvSS.png"
imagem_computador2 = "https://i.imgur.com/MxZ4mO5.png"
imagem_computador3 = "https://i.imgur.com/53q5GV9.png"
imagem_abertura = 'https://i.imgur.com/mgSlPGj.png'
botao_play = 'https://i.imgur.com/4IFbhfb.png'
boneca_dormindo = 'https://i.imgur.com/PMwusTO.png'
imagem_botaoajuda = 'https://i.imgur.com/jALMQz4.png'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

class desafio_1:

    def __init__(self):
        self.ABERTURA = Cena(imagem_abertura)
        self.ENTRADA1 = Cena(imagem_computador)
        self.ENTRADA2 = Cena(imagem_computador2)
        self.ENTRADA3= Cena(imagem_computador3)
        self.QUARTO1 = Cena(imagem_quarto)
        self.QUARTO = Cena(imagem_quarto)
        self.QUARTO2= Cena(imagem_quarto2)
        self.cena2= Cena(imagem_livroaberto)
        self.cena4 = Cena(imagem_mapa)
        
        self.BOTAOPLAY = Elemento(botao_play, tit="PLAY",
                         w=150, h=150, x=200, y=390,
                         cena = self.ABERTURA)        
        self.SETAENTRADA1 = Elemento(seta, tit="Próximo",
                             w=55,h=58, x=750, y=330,
                             cena = self.ENTRADA1)
        self.SETAENTRADA2 = Elemento(seta, tit="Próximo",
                             w=55,h=58, x=750, y=330,
                             cena = self.ENTRADA2)
        self.SETAENTRADA3 = Elemento(seta, tit="Próximo",
                             w=55,h=58, x=750, y=330,
                             cena = self.ENTRADA3)
        self.BONECADORMINDO = Elemento(boneca_dormindo, tit="Acorde Hipátia",
                              w=336, h=240, x=260, y=270,
                              cena = self.QUARTO1)
        self.SETA = Elemento(seta, tit="Próximo",
                             w=55,h=58, x=900, y=420,
                             cena = self.QUARTO)
        self.BONECA1 = Elemento(imagem_boneca1, tit="Onde pode estar meu livro?",
                                w=240,h=336, x=300, y=230,
                                cena = self.QUARTO)
        self.LIVRO= Elemento(imagem_livro, tit="É esse!",
                             w=55,h=58, x=850, y=390,
                             cena = self.QUARTO2)
        self.LIVROERRADO= Elemento(imagem_livroerrado, tit="Acho que não é esse...",
                             w=55,h=58, x=500, y=390, 
                             cena = self.QUARTO2)
        self.BONECA2= Elemento(imagem_boneca2, tit="Acho que encontrei meu livro!",
                               w=300,h=420, x=200, y=200, 
                               cena = self.QUARTO2)
        self.BOTAO_DESAFIO1= Elemento(botao_desafio1, tit="PLAY",
                                      w=55,h=58, x=610, y=300,
                                      cena = self.cena2)
        self.BOTAO_AJUDA = Elemento(imagem_botaoajuda, tit="PLAY",
                                      w=55,h=58, x=200, y=100,
                                      cena = self.cena2)
        self.BIBLIOTECA= Elemento(click_biblioteca, tit="CLICK",
                                  w=55,h=58, x=610, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                  cena = self.cena4)  
         
        self.texto_4 = Texto(self.QUARTO1, txt = "Acorde Hipátia")
        self.texto_3 = Texto(self.QUARTO, txt = "Hipátia gosta de ler seu livro quando acorda. Mas, nessa manhã, não o encontrou em sua mesa e resolveu procurar no closet. Estranho...")
        self.texto_1 = Texto(self.QUARTO2, txt = 'Hipátia, encontre o livro')                     
        self.texto_2= Texto(self.cena2, txt= 'Hipátia encontrou uma mensagem estranha em seu livro, aperte o PLAY para decifrá-la')
        self.texto_5 = Texto(self.cena2, txt = "O desafio é um anagrama. Um anagrama é criado a partir de uma palavra com suas letras embaralhadas. Tente reorganizar a frase para encontrar o recado e resolver o desafio.")
        
        self.BOTAOPLAY.elt.bind("click", self.BOTAO_PLAY)
        self.SETAENTRADA1.elt.bind("click", self.BOTAO_ENTRADA1)
        self.SETAENTRADA2.elt.bind("click", self.BOTAO_ENTRADA2)
        self.BONECADORMINDO.elt.bind("click", self.ACORDA_BONECA)
        self.SETA.elt.bind("click", self.funcao_de_acao_do_botao3)
        self.LIVRO.elt.bind("click", self.funcao_de_acao_do_botao)
        self.LIVROERRADO.elt.bind("click", self.livro_errado)  
        self.BOTAO_DESAFIO1.elt.bind("click", self.desafio1)
        self.BOTAO_AJUDA.elt.bind("click", self.AJUDA)
        self.BIBLIOTECA.elt.bind("click", self.chama_sala)
        
    def desafio1(self,*_):
        self.resposta1=str(input('Hipátia, qual é a resposta do desafio?'))
        self.resposta2=self.resposta1.lower()
        #print(self.resposta2, self.resposta2.isalpha()) # ESSA LINHA DE VERIFICAÇAO MOSTRA SE PARTE DO CÓDIGO RODA
        if self.resposta2 == 'va para a biblioteca' or self.resposta2 == 'vá para a biblioteca':
        #print('a verificiação if ta funcionando') # LINHA DE VERIFICAÇÃO É NECESSÁRIO O CONSOLE DO BROWSER
            self.cena4.vai()
            self.parabens = Texto(self.cena4, txt = 'Parabéns, Hipátia, você acertou!')
            self.parabens.vai() 
        else:
        #print('a verificiação else ta funcionando') #LINHA DE VERIFICAÇAO
            self.tente_novamente=Texto(self.cena2, txt = 'Hipátia, tente novamente.')
            self.tente_novamente.vai()
        
    def livro_errado(self,event = None):
        self.texto_4=Texto(self.QUARTO2, txt = 'Este não é o livro correto, continue procurando.')
        self.texto_4.vai()
            
    def funcao_de_acao_do_botao(self,event = None):
        self.cena2.vai()
        self.texto_2.vai()

    def funcao_de_acao_do_botao3(self,event = None):
        self.QUARTO2.vai()
        self.texto_1.vai()
            
    def BOTAO_ENTRADA2(self,event = None):
        self.QUARTO1.vai() 
        self.texto_4.vai()
        
    def BOTAO_ENTRADA1(self,event = None):
        self.ENTRADA2.vai()
        
    def BOTAO_PLAY(self,event = None):
        self.ENTRADA1.vai()
    
    def ACORDA_BONECA(self,event = None):
        self.QUARTO.vai()
        self.texto_3.vai()
        
    def AJUDA(self,event = None):
        self.texto_5.vai()
        
    def chama_sala(self, event= None):
        DT().inicia() # Daí aqui alterei os "as" lá do import
    
    def inicia(self,*_):
        self.ABERTURA.vai()
        
        
        
if __name__ == "__main__":                  
    desafio_1().inicia()