# elizabeth.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

#class parte1:

imagem_play= 'https://img2.gratispng.com/20180325/fyw/kisspng-youtube-play-button-computer-icons-clip-art-button-5ab819cc3d5ee6.2062185015220146682514.jpg'
imagem_pc='https://cdn5.colorir.com/desenhos/color/201049/773d6796c883c528d45a21258f54e263.png'
fundo_transparente='https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.techtudo.com.br%2Fdicas-e-tutoriais%2Fnoticia%2F2012%2F11%2Fcomo-remover-o-fundo-de-fotos-e-deixa-lo-transparente-no-photoscape.html&psig=AOvVaw36qwHy3_KTk7xvMzE0pLBr&ust=1607800797505000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOiZ2vDSxu0CFQAAAAAdAAAAABAD'


PLAY= Cena(imagem_play)
BOTAO_PLAY= Elemento(imagem_play, tit= "click" ,cena = PLAY)

PC=Cena(imagem_pc)
nome_personagem=''
#def nomepersonagem(pergunta_nome):
    
pergunta_nome= str(input('Escolha o nome da personagem:'))
nome_personagem= pergunta_nome
if nome_personagem == None:
    nome_personagem=fulana
    print(nome_personagem)
#        PC.vai()
else:
    nome_personagem= nome_personagem
    #    PC.vai()
    print(nome_personagem)
        

        
texto_ = Texto(PLAY, txt = nome_personagem + 'Gosta de ler um livro')


        
    
    
PLAY.vai()
#BOTAO_PLAY.elt.bind("click", nomepersonagem)
texto_.vai()



