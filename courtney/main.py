# elizabeth.courtney.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

Imagem_Biblioteca_porta="https://media.istockphoto.com/vectors/closed-door-drawing-vector-id865663698"
Imagem_Biblioteca_porta2="https://image.freepik.com/vetores-gratis/porta-aberta-dos-desenhos-animados-entrada-do-corredor-do-apartamento-entrada-do-escritorio_53562-8532.jpg"
Imagem_Biblioteca_dentro="https://secult.es.gov.br/Media/secult/BPES/IMG_7650.JPG"
Imagem_Biblioteca_caixa="https://thumbs.dreamstime.com/z/caixa-dos-desenhos-animados-no-fundo-branco-98137796.jpg"
Imagem_Biblioteca_papel="https://thumbs.dreamstime.com/z/folhas-de-pap%C3%A9is-de-nota-com-o-desenho-da-m%C3%A3o-do-pino-do-impulso-89420296.jpg"
STYLE["width"] = 500 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

Biblioteca_entrada=Cena(Imagem_Biblioteca_porta)
Biblioteca_entrada.vai()

Biblioteca_porta=Cena(Imagem_Biblioteca_porta2)

Biblioteca_dentro=Cena(Imagem_Biblioteca_dentro)


Imagem_botao="https://images-na.ssl-images-amazon.com/images/I/71nQDXqkyDL.png"

def desafio_porta1 (event = None):
    Biblioteca_porta.vai()
    
BOTAO= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                cena = Biblioteca_entrada)
                                
BOTAO.elt.bind("click", desafio_porta1)

def desafio_porta2 (event = None):
    Biblioteca_dentro.vai()
    
BOTAO2= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                cena = Biblioteca_porta)
                                
BOTAO2.elt.bind("click", desafio_porta2)

Biblioteca_dentro = Cena(Imagem_Biblioteca_caixa)
            #Cena1.vai()
botao_caixa = Elemento(Imagem_Biblioteca_caixa, tit="CLIQUE",
                       style=dict(height=100,widht=100, left=300, top=250), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                       cena = Biblioteca_dentro,
                       vai = clique_caixa)

      def clique_caixa (event = None):
            Biblioteca_papel = Cena(Imagem_Biblioteca_papel)
            Biblioteca_papel.vai()