# elizabeth.grace.main.py
from _spy.vitollino.main import Cena, Elemento

CASTELO = "https://i.imgur.com/LF4NbKH.jpg"
PEIXE = "https://i.imgur.com/uw3Q4kO.png"
DESERTO = "https://i.imgur.com/AOysKp6.jpeg"
MORANGO = "https://i.imgur.com/TYqfeqN.png"
TUBARAO_VIVO = "https://i.imgur.com/1tfjX56.png"

castelo= Cena(img=CASTELO)
peixe=Elemento(img=PEIXE, tit ="ooi", top=500, heigth = 9000, widht= 2000, left=1000)
peixe.entra(castelo)
deserto= Cena(img = DESERTO)
castelo.direita=deserto
deserto.esquerda=castelo
morango= Elemento(img=MORANGO,tit ="me chamo morango")
morango.entra(deserto)
#tubarao_vivo =Elemento(img=TUBARAO_VIVO)
#tubarao_vivo.entra(deserto)

castelo.vai()