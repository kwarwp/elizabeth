"""
diga_o_nome = str(input("Diga um nome"))

novo_nome = diga_o_nome

print(f'Eu fui à feira com a {diga_o_nome}')
print(novo_nome)
"""

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

CENARIO = "http://cardolettoilustrador.com.br/wp-content/uploads/estudo-cen%C3%A1rio.jpg"
imagem_play= 'https://img2.gratispng.com/20180325/fyw/kisspng-youtube-play-button-computer-icons-clip-art-button-5ab819cc3d5ee6.2062185015220146682514.jpg'
imagem_pc='https://cdn5.colorir.com/desenhos/color/201049/773d6796c883c528d45a21258f54e263.png'
fundo_transparente='https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.techtudo.com.br%2Fdicas-e-tutoriais%2Fnoticia%2F2012%2F11%2Fcomo-remover-o-fundo-de-fotos-e-deixa-lo-transparente-no-photoscape.html&psig=AOvVaw36qwHy3_KTk7xvMzE0pLBr&ust=1607800797505000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOiZ2vDSxu0CFQAAAAAdAAAAABAD'


pergunta_nome= str(input('Escolha o nome da personagem:'))
nome_personagem= pergunta_nome
if nome_personagem == '':
   nome_personagem = "fulana"
else:
   nome_personagem = nome_personagem



class Entrada():
    global nome_personagem
    
    def __init__(self):
        self.PLAY= Cena(imagem_play)
        self.BOTAO_PLAY= Elemento(imagem_play, tit= "click" ,cena = self.PLAY)
        self.BOTAO_PLAY.elt.bind("click", self.testa_nome_cena)
    
    def testa_nome_cena(self,*_):
        self.cena_teste = Cena(CENARIO)
        self.cena_teste.vai()
        #print(nome_personagem)
        self.texto_ = Texto(self.cena_teste, txt = f'{nome_personagem} Gosta de ler um livro')
        self.texto_.vai()
            
    def start_eng(self):
        self.PLAY.vai()
        
Entrada().start_eng()
            