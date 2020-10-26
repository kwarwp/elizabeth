# elizabeth.angie.main.py
from _spy.vitollino.main import Cena, Elemento

CASTELO = "https://i.imgur.com/LF4NbKH.jpg"
PEIXE = "https://i.imgur.com/uw3Q4kO.png"
DESERTO = "https://i.imgur.com/AOysKp6.jpeg"
MORANGO= "https://i.imgur.com/TYqfeqN.png"

castelo = Cena (img=CASTELO) 
peixe = Elemento (img=PEIXE)
peixe.entra(castelo) 
deserto = Cena (img=DESERTO)
castelo.direita=deserto
deserto.direita=castelo
morango= Elemento (img=MORANGO)
morango.entra(deserto)


castelo.vai()