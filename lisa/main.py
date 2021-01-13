# elizabeth.lisa.main.py


from _spy.vitollino.main import Cena, Texto, STYLE, Elemento

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"


MINHA_CENA = "https://i.imgur.com/CsOVXPc.jpeg" # Extensões aceitas: png, jpg, jpeg e gif
MEU_ELEMENTO = "https://i.imgur.com/aYRC7bM.png" # Extensões aceitas: png, jpg, jpeg e gif

nome_da_cena = Cena(MINHA_CENA)


RESPOSTA1= Elemento(MEU_ELEMENTO, tit="PLAY", w=55,h=58, x=610, y=300, cena = nome_da_cena)

def resultado(A):
     # O novo popupque será gerado quando o foi() do texto forchamado
    dicionario = dict(A="Você clicou no A", B="Você clicou no B") # dicionário que guarda a devolutiva da opção escolhida
    devolutiva = Texto(nome_da_cena, txt=dicionario[A])
    devolutiva.vai()


pergunta = Texto(nome_da_cena, txt = "Qual é a resposta para o desafio?", foi = resultado, A= "resposta", B= "resposta")

nome_da_cena.vai()
pergunta.vai()