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
imagem_livroerrado = 'https://i.imgur.com/kP9br1f.png'
imagem_boneca2 = 'https://i.imgur.com/NEyFwDm.png'
imagem_computador = "data:image/png;base64,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"
botao_seta = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUPV3dtm3q9iG_TLUGGn5xlzW2q4lI2va1uA&usqp=CAU"
imagem_computador2 = "data:image/png;base64,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"
botao_seta2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6-yZTndXuOF4rwJ74ypUPbBhiyTChSv1CaQ&usqp=CAU"

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

class desafio_1:

    def __init__(self):
        self.QUARTO = Cena(imagem_quarto)
        #self.PERSONAGEM_DORMINDO= Elemento(imagem_personagem1, tit="Acorde",
                             #w=600,h=300,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             #cena = self.cena1)
                     
        self.QUARTO2= Cena(imagem_quarto2)        
        
        self.LIVRO= Elemento(imagem_livro, tit="É esse!",
                             w=55,h=58, x=850, y=390, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.QUARTO2)
                             
        self.LIVROERRADO= Elemento(imagem_livroerrado, tit="Acho que não é esse...",
                             w=55,h=58, x=500, y=390, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.QUARTO2)     
                             
        self.BONECA2= Elemento(imagem_boneca2, tit="Acho que encontrei meu livro!",
                             w=300,h=420, x=200, y=200, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.QUARTO2)    
        
        self.LIVRO.elt.bind("click", self.funcao_de_acao_do_botao)  
        
        self.LIVROERRADO.elt.bind("click", self.livro_errado)  
        
        self.SETA = Elemento(seta, tit="Próximo",
                             w=55,h=58, x=900, y=420,
                             cena = self.QUARTO)
                             
        self.BONECA1 = Elemento(imagem_boneca1, tit="Onde pode estar meu livro?",
                             w=300,h=420, x=600, y=200,
                             cena = self.QUARTO)  
                             
        self.texto_3 = Texto(self.QUARTO, txt = "Hipátia gosta de ler seu livro quando acorda. Mas, nessa manhã, não o encontrou em sua mesa e resolveu procurar no closet. Estranho...")
                             
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
            
    def livro_errado(self,event = None):
        self.texto_4=Texto(self.QUARTO2, txt = 'Este não é o livro correto, continue procurando.')
        self.texto_4.vai()
                             
    def funcao_de_acao_do_botao(self,event = None):
        self.cena2.vai()
        self.texto_2.vai()
                                                                  
    def funcao_de_acao_do_botao3(self,event = None):
        self.QUARTO2.vai()
        self.texto_1.vai()        
    
    def inicia(self,*_):
        self.QUARTO.vai()
        self.texto_3.vai()
        
        
        
if __name__ == "__main__":                  
    desafio_1().inicia()