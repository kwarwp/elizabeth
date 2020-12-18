# elizabeth.roxanne.main.py
"""     xxxxx

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    
       - Class registro

"""

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from stacy.main import Modulo1

#class parte1:

imagem_play= 'https://img2.gratispng.com/20180325/fyw/kisspng-youtube-play-button-computer-icons-clip-art-button-5ab819cc3d5ee6.2062185015220146682514.jpg'
imagem_pc='https://cdn5.colorir.com/desenhos/color/201049/773d6796c883c528d45a21258f54e263.png'
tela_branca = "http://www.f12com.com.br/wp-content/uploads/tela_branca.jpg"


class Registro:

    def __init__(self, nome = False):
        self.nome = nome
        
    def registra(self):
        self.pergunta_nome= str(input('Escolha o nome da personagem:'))
        if self.pergunta_nome == '':
            self.pergunta_nome = "fulana"
            self.nome = True
        else:
            self.pergunta_nome = self.pergunta_nome
            self.nome = True  
        self.nome_personagem = self.pergunta_nome   
        """ testa se após passar por aqui, self.nome se torna true e a variável grava o nome """
        #print(self.nome, self.nome_personagem) 
        
VAI = Registro()
VAI.registra()



        
class Inicia:

    def __init__(self, ticket = False):
        self.ticket = ticket
        if self.ticket == True:
            Modulo1().mari()
        
        
    def cria_usuario(self):
        TESTE = Registro().registra()
        if nome== True:
            self.ticket = True
            
            
#if __name__ == "__main__":    
    #Inicia().cria_usuario()
    #Registro().registra()