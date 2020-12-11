# elizabeth.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

imagem_play= 'https://img2.gratispng.com/20180325/fyw/kisspng-youtube-play-button-computer-icons-clip-art-button-5ab819cc3d5ee6.2062185015220146682514.jpg'
imagem_pc='https://cdn5.colorir.com/desenhos/color/201049/773d6796c883c528d45a21258f54e263.png'
PLAY= Cena(imagem_play)
PC=Cena(imagem_pc)
def nomepersonagem():
    nome_personagem= str(input('Escolha o nome da personagem:'))
    PC.vai 

PLAY.elt.bind("click", nomepersonagem)
