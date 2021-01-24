#ATO 1


"""     xxxxx

.. codeauthor:: Livia Machado <liviamcampos98@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""


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
imagem_boneca1 = 'https://i.imgur.com/alSNLX0.png'

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

class desafio_1:

    def __init__(self):
        self.QUARTO = Cena(imagem_quarto)
        #self.PERSONAGEM_DORMINDO= Elemento(imagem_personagem1, tit="Acorde",
                             #w=600,h=300,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             #cena = self.cena1)
        
        self.QUARTO2= Cena(imagem_quarto2)
        
        
        self.LIVRO= Elemento(imagem_livro, tit="Livro",
                             w=55,h=58, x=850, y=390, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.QUARTO2)

        
        self.LIVRO.elt.bind("click", self.funcao_de_acao_do_botao)  
        
        
        self.SETA = Elemento(seta, tit="Próximo",
                             w=55,h=58, x=900, y=420,
                             cena = self.QUARTO)
                             
        self.BONECA1 = Elemento(imagem_boneca1, tit="Onde pode estar meu livro?",
                             w=240,h=336, x=600, y=250,
                             cena = self.QUARTO)  
                             
        self.texto_2 = Texto(self.QUARTO, txt = "Hipátia gosta de ler seu livro quando acorda. Mas, nessa manhã, não o encontrou em sua mesa e resolveu procurar no closet. Estranho...")
                             
        self.SETA.elt.bind("click", self.funcao_de_acao_do_botao3)  
        
        self.texto_1 = Texto(self.QUARTO2, txt = 'Hipátia, encontre o livro')
        
        self.cena2= Cena(imagem_livroaberto)
        
        self.texto_2= Texto(self.cena2, txt= 'Hipátia encontrou uma mensagem estranha em seu livro, aperte o PLAY para decifrá-la')
        
        self.BOTAO_DESAFIO1= Elemento(botao_desafio1, tit="PLAY",
                                      w=55,h=58, x=610, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                                      cena = self.cena2)

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
            
            
             
                             
    def funcao_de_acao_do_botao(self,event = None):
        self.cena2.vai()
        self.texto_2.vai()
                                                               
    
    def funcao_de_acao_do_botao3(self,event = None):
        self.QUARTO2.vai()
        self.texto_1.vai()
            
    def inicia(self,*_):
        self.QUARTO.vai()
        self.texto_2.vai()
        
        
if __name__ == "__main__":                  
    desafio_1().inicia()