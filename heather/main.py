# elizabeth.heather.main.py
#ATO 1


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
#from meredith.main import nome_personagem
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
imagem_personagem1 = 'https://cdn-0.imagensemoldes.com.br/wp-content/uploads/2020/04/Simpsons-Dormindo-e-Babando-png-Vetor.png'
imagem_personagem2= 'https://upload.wikimedia.org/wikipedia/pt/thumb/0/02/Homer_Simpson_2006.png/200px-Homer_Simpson_2006.png'
imagem_boneca1 = 'https://i.imgur.com/xTthXnC.png'
imagem_livroerrado = 'https://i.imgur.com/kP9br1f.png'
imagem_boneca2 = 'https://i.imgur.com/NEyFwDm.png'
imagem_computador = "data:image/png;base64,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"
botao_seta = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUPV3dtm3q9iG_TLUGGn5xlzW2q4lI2va1uA&usqp=CAU"
imagem_computador2 = "data:image/png;base64,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"
botao_seta2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6-yZTndXuOF4rwJ74ypUPbBhiyTChSv1CaQ&usqp=CAU"
imagem_abertura = 'data:image/jpeg;base64,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'
botao_play = 'https://i.imgur.com/74ZZX5s.png'
boneca_dormindo = 'https://i.imgur.com/PMwusTO.png'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

class desafio_1:

    def __init__(self):
        self.ABERTURA = Cena(imagem_abertura)
        self.ENTRADA1 = Cena(imagem_computador)
        self.ENTRADA2 = Cena(imagem_computador2)
        self.QUARTO1 = Cena(imagem_quarto)
        self.QUARTO = Cena(imagem_quarto)
        self.QUARTO2= Cena(imagem_quarto2)
        self.cena2= Cena(imagem_livroaberto)
        
        self.BOTAOPLAY = Elemento(botao_play, tit="PLAY",
                         w=55, h=58, x=500, y=390,
                         cena = self.ABERTURA)        
        self.SETAENTRADA1 = Elemento(botao_seta, tit="CLIQUE",
                            w=55, h=58, x=500, y=390,
                            cena = self.ENTRADA1)
        self.SETAENTRADA2 = Elemento(botao_seta2, tit="CLIQUE",
                            w=55, h=58, x=500, y=390,
                            cena = self.ENTRADA2)
        self.BONECADORMINDO = Elemento(boneca_dormindo, tit="Acorde Hipátia",
                              w=300, h=420, x=500, y=390,
                              cena = self.QUARTO1)
        self.SETA = Elemento(seta, tit="Próximo",
                             w=55,h=58, x=900, y=420,
                             cena = self.QUARTO)
        self.BONECA1 = Elemento(imagem_boneca1, tit="Onde pode estar meu livro?",
                                w=300,h=420, x=600, y=200,
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
         
        self.texto_4 = Texto(self.QUARTO1, txt = "Acorde Hipátia")
        self.texto_3 = Texto(self.QUARTO, txt = "Hipátia gosta de ler seu livro quando acorda. Mas, nessa manhã, não o encontrou em sua mesa e resolveu procurar no closet. Estranho...")
        self.texto_1 = Texto(self.QUARTO2, txt = 'Hipátia, encontre o livro')                     
        self.texto_2= Texto(self.cena2, txt= 'Hipátia encontrou uma mensagem estranha em seu livro, aperte o PLAY para decifrá-la')
        
        self.BOTAOPLAY.elt.bind("click", self.BOTAO_PLAY)
        self.SETAENTRADA1.elt.bind("click", self.BOTAO_ENTRADA1)
        self.SETAENTRADA2.elt.bind("click", self.BOTAO_ENTRADA2)
        self.BONECADORMINDO.elt.bind("click", self.ACORDA_BONECA)
        self.SETA.elt.bind("click", self.funcao_de_acao_do_botao3)
        self.LIVRO.elt.bind("click", self.funcao_de_acao_do_botao)
        self.LIVROERRADO.elt.bind("click", self.livro_errado)  
        self.BOTAO_DESAFIO1.elt.bind("click", self.desafio1)
        
    def desafio1(self,*_):
        self.resposta1=str(input('Hipátia, qual é a resposta do desafio?'))
        self.resposta2=self.resposta1.lower()
        #print(self.resposta2, self.resposta2.isalpha()) # ESSA LINHA DE VERIFICAÇAO MOSTRA SE PARTE DO CÓDIGO RODA
        if self.resposta2 == 'va para a biblioteca' or self.resposta2 == 'vá para a biblioteca':
        #print('a verificiação if ta funcionando') # LINHA DE VERIFICAÇÃO É NECESSÁRIO O CONSOLE DO BROWSER
            self.cena4 = Cena(imagem_mapa)
            self.cena4.vai()
            self.parabens = Texto(self.cena4, txt = 'Parabéns, Hipátia, você acertou!')
            self.parabens.vai()
            self.BIBLIOTECA= Elemento(click_biblioteca, tit="CLICK",
                                      w=55,h=58, x=610, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                      cena = self.cena4)   
        else:
        #print('a verificiação else ta funcionando') #LINHA DE VERIFICAÇAO
            self.tente_novamente=Texto(self.cena3, txt = 'Hipátia, tente novamente.')
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
    
    def inicia(self,*_):
        self.ABERTURA.vai()
        
        
        
if __name__ == "__main__":                  
    desafio_1().inicia()