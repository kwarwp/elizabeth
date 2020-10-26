# elizabeth.callie.main.py
from _spy.vitollino.main import Cena, Elemento

CASTELO = "https://i.imgur.com/LF4NbKH.jpg"
MORANGO = "https://i.imgur.com/TYqfeqN.png"
CASTELO = Cena (img=CASTELO)
MORANGO = Elemento (img=MORANGO, tit = "oi")
MORANGO.entra(CASTELO)
CASTELO.vai()