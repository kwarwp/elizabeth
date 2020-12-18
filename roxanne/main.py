# elizabeth.roxanne.main.py
"""     xxxxx

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    
       - Class registro
       - Class inicia 

"""

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from stacy.main import Modulo1

#class parte1:

imagem_play= 'https://img2.gratispng.com/20180325/fyw/kisspng-youtube-play-button-computer-icons-clip-art-button-5ab819cc3d5ee6.2062185015220146682514.jpg'
imagem_pc='https://cdn5.colorir.com/desenhos/color/201049/773d6796c883c528d45a21258f54e263.png'
tela_branca = "http://www.f12com.com.br/wp-content/uploads/tela_branca.jpg"
registrador = "https://www.freeiconspng.com/uploads/register-button-png-0.png"
comecador = "https://pngimage.net/wp-content/uploads/2018/06/game-play-button-png-3.png"


class Registro:

    def __init__(self, nome = False):
        #self.nome = nome
        self.ticket = False
        self.instancia = Registro()
        
        self.cena = Cena(tela_branca)
        self.bot1 = Elemento(comecador, tit="CLIQUE PARA COMEÇAR",
                           style=dict(height=100,widht=100, left=150, top=125), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = self.cena,
                           vai = self.registra)
        
    def registra(self):
        self.pergunta_nome= str(input('Escolha o nome da personagem:'))
        if self.pergunta_nome == '':
            self.pergunta_nome = "fulana"
            #self.nome = True
            #self.chama_mod1()
        else:
            self.pergunta_nome = self.pergunta_nome
            #self.nome = True  
            #self.chama_mod1()
        self.nome_personagem = self.pergunta_nome   
        
        """ testa se após passar por aqui, self.nome se torna true e a variável grava o nome """
        #print(self.nome, self.nome_personagem) 
    def chama_mod1(self):
        Modulo1().mari()

    def gera(self):
        self.cena.vai()
        
if __name__ == "__main__":   
    Registro().gera()
    
#VAI = Registro() 
#VAI.registra()
#print(VAI.nome, VAI.nome_personagem)


