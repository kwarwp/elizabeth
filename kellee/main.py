# elizabeth.kellee.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto


imagem_quarto = 'https://i.pinimg.com/originals/66/88/9a/66889a5a4db243c94e3c0623df56e664.jpg'
imagem_personagem1 = 'https://cdn-0.imagensemoldes.com.br/wp-content/uploads/2020/04/Simpsons-Dormindo-e-Babando-png-Vetor.png'
imagem_personagem2= 'https://upload.wikimedia.org/wikipedia/pt/thumb/0/02/Homer_Simpson_2006.png/200px-Homer_Simpson_2006.png'


STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px'
QUARTO1 = Cena(imagem_quarto)
QUARTO2 = Cena(imagem_quarto)
def acorda_boneca (event = None):
    QUARTO2.vai()
    
PERSONAGEM_DORMINDO= Elemento(imagem_personagem1, tit="Acorde",
                             W=600,h=300,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = QUARTO1
                             vai = acorda_boneca)
                             
PERSONAGEM_ACORDADA = Elemento(imagem_personagem2, tit="",
                             W=600,h=300,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                             cena = QUARTO2)
                             
texto2 = Texto(QUARTO2, txt = "Nome_Fulana gosta de ler um livro quando acorda. Encontre-o")
texto2 = Texto(QUARTO2, txt = f'{nome_personagem} gosta de ler um livro quando acorda. Encontre-o')