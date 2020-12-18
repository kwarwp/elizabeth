"""     xxxxx

.. codeauthor:: Livia Machado <liviamcampos98@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
#from meredith.main import nome_personagem
from roxane.main import *
#from cenas.imix import Inicial
#from cenas.ik import Passeio
        
imagem_quarto = 'https://i.pinimg.com/originals/66/88/9a/66889a5a4db243c94e3c0623df56e664.jpg'
imagem_livro = 'https://livrariaconcreta.com.br/wp-content/uploads/2017/01/Hardcover-Book-MockUp-LIVRO-VERMELHO.png'
imagem_livroaberto = 'https://images.vexels.com/media/users/3/157260/isolated/preview/d48b34b2e855b69b29d5565edda69536-vetor-de-livro-aberto-em-branco-by-vexels.png'
papel_rasgado = 'https://cdn.pixabay.com/photo/2019/03/18/15/10/torn-paper-4063317_960_720.png'
imagem_mapa ='https://comps.canstockphoto.com.br/cidade-mapa-pequeno-sub%C3%BArbio-vila-vetor-clip-arte_csp14479563.jpg'
imagem_personagem1 = 'https://cdn-0.imagensemoldes.com.br/wp-content/uploads/2020/04/Simpsons-Dormindo-e-Babando-png-Vetor.png'
imagem_personagem2= 'https://upload.wikimedia.org/wikipedia/pt/thumb/0/02/Homer_Simpson_2006.png/200px-Homer_Simpson_2006.png'
STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

#STYLE["width"] = 700 #  width = 300 (default)
#STYLE["heigth"] = '600px' # min-height = "300px"
#STYLE["width"] = 394 #  width = 300 (default)
#STYLE["heigth"] = '521px'

class desafio_2:
    

    def __init__(self):
        self.QUARTO = Cena(imagem_quarto)
        #self.cena1.vai()
        #self.PERSONAGEM_DORMINDO= Elemento(imagem_personagem1, tit="Acorde",
                             #w=600,h=300,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             #cena = self.cena1)
        
        self.texto_1 = Texto(self.QUARTO, txt = f'{nome_personagem},Encontre o livro')
        #self.texto_1.vai()
        
        self.LIVRO= Elemento(imagem_livro, tit="Livro",
                             w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = self.QUARTO)
        self.LIVRO.elt.bind("click", self.funcao_de_acao_do_botao)   
        
        
    def funcao_de_acao_do_botao(self,event = None):
        self.cena2= Cena(imagem_livroaberto)
        self.cena2.vai()
        self.PAPEL_RASGADO = Elemento(papel_rasgado, tit="título_do_elemento", 
                                 w=578, h=437, x=450, y=250, 
                                 cena = self.cena2)
        self.PAPEL_RASGADO.elt.bind("click", self.funcao_de_acao_do_botao2)                         

        
    def funcao_de_acao_do_botao2(self,event = None):
        self.cena3= Cena(papel_rasgado)
        self.cena3.vai()
        self.cena3.elt.bind("click", self.desafio1)   

    def desafio1(self,*_):
        self.resposta1=str(input(f'{nome_personagem}, qual é a resposta do desafio?'))
        self.resposta2=self.resposta1.lower()
        #print(self.resposta2, self.resposta2.isalpha()) # ESSA LINHA DE VERIFICAÇAO MOSTRA SE PARTE DO CÓDIGO RODA
        if self.resposta2 == 'va para a biblioteca' or self.resposta2 == 'vá para a biblioteca':
            #print('a verificiação if ta funcionando') # LINHA DE VERIFICAÇÃO É NECESSÁRIO O CONSOLE DO BROWSER
            self.cena4 = Cena(imagem_mapa)
            self.cena4.vai()
            self.parabens = Texto(self.cena4, txt = f'Parabéns,{nome_personagem}, você acertou!')
            self.parabens.vai()
        else:
            #print('a verificiação else ta funcionando') #LINHA DE VERIFICAÇAO
            self.tente_novamente=Texto(self.cena3, txt = f'{nome_personagem}, Tente novamente.')
            self.tente_novamente.vai()
            
    def inicia(self,*_):
        self.cena1.vai()
        self.texto_1.vai()
        
if __name__ == "__main__":                  
    desafio_2().inicia()