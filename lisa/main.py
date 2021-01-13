# elizabeth.lisa.main.py


from _spy.vitollino.main import Cena, Texto


MINHA_CENA = "https://i.imgur.com/CsOVXPc.jpeg" # Extensões aceitas: png, jpg, jpeg e gif
MEU_ELEMENTO = "https://i.imgur.com/aYRC7bM.png" # Extensões aceitas: png, jpg, jpeg e gif

nome_da_cena = Cena(MINHA_CENA)
nome_da_cena.vai()

RESPOSTA1= Elemento(MEU_ELEMENTO, tit="PLAY", w=55,h=58, x=610, y=300, cena = nome_da_cena)

def resultado(A):
     # O novo popupque será gerado quando o foi() do texto forchamado
    dicionario = dict(A="Você clicou no A", B="Você clicou no B") # dicionário que guarda a devolutiva da opção escolhida
    devolutiva = Texto(nome_da_cena, txt=dicionario[A])
    devolutiva.vai()


pergunta = Texto(nome_da_cena, txt = "Seu enunciado aqui", foi = resultado, A= "resposta", B= "resposta")
pergunta.vai()