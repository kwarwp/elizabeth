# elizabeth.julia.main.py
from _spy.vitollino.main import  Cena, Elemento 

CASTELO = "https://i.imgur.com/LF4NbKH.jpeg"
PEIXE = "https://i.imgur.com/uw3Q4kO.png"
DESERTO = "https://i.imgur.com/AOysKp6.jpeg"
MORANGO = "https://i.imgur.com/TYqfeqN.png"
TUBARAO_VIVO = "https://i.imgur.com/1tfjX56.png"
castelo = Cena(img=CASTELO)
peixe = Elemento(img=PEIXE, tit ="ooi")
peixe.entra(castelo)




