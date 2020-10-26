# elizabeth.kristen.main.py
from _spy.vitollino.main import Cena, Elemento

CASTELO = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fpt.pngtree.com%2Ffree-png-vectors%2Fcastelo&psig=AOvVaw1XzfQ5PR_TqoNDcSCTQ7_w&ust=1603828352595000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIja2qyE0-wCFQAAAAAdAAAAABAD.png"
PEIXE = "https://toppng.com/public/uploads/preview/yellow-zebrasomatang-fish-png-clipart-fish-11563113723vhpxu98iui.png"
DESERTO = "https://img2.gratispng.com/20180225/djq/kisspng-gobi-desert-red-desert-dune-landscape-desert-scenery-5a937162db54e3.8617587415196122588984.jpg"
MORANGO = "https://i.pinimg.com/originals/a8/6e/1a/a86e1ae5715d3f92df2cccfbd60d29d0.png"
TUBARAO_VIVO = "https://i.pinimg.com/736x/23/7a/db/237adb1023d1609f2f4e61ba5131c6b4.jpg"

castelo= Cena(img=CASTELO)
peixe= Elemento(img=PEIXE, tit="ooi", x=90, y= 50, w=100, h=800)
peixe.entra(castelo)
deserto= Cena(img = DESERTO)
castelo.direita=deserto
deserto.esquerda=castelo
morango= Elemento(img=MORANGO, tit = "me chamo morango")
morango.entra(deserto)
tubarao_vivo = Elemento(img=TUBARAO_VIVO)
tubarao_vivo.entra(deserto)

castelo.vai()
