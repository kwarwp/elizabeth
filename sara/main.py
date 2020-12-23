# elizabeth.sara.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto


porta_fechada="https://media.istockphoto.com/vectors/closed-door-drawing-vector-id865663698"
Imagem_botao="https://images-na.ssl-images-amazon.com/images/I/71nQDXqkyDL.png"
imagem_desafio='https://s2.static.brasilescola.uol.com.br/img/2019/10/quadrado-abcd.jpg'



Biblioteca_entrada=Cena(porta_fechada)
Biblioteca_entrada.vai()

def abre_desafio (event = None):
    desafio=Cena(imagem_desafio)
    desafio.vai()
    texto_1 = Texto(desafio, txt = 'Complete o quadrado:')
    texto_1.vai()




BOTAO= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                cena = Biblioteca_entrada)
                                
BOTAO.elt.bind("click", abre_desafio)