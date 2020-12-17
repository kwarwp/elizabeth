# elizabeth.natalia.main.py
from _spy.vitollino.main import Cena, Elemento, Droppable, Dragger, STYLE
from browser import document, alert, html

OCEANO = "https://static.scientificamerican.com/sciam/cache/file/BCC3BD1E-5DC0-4843-A841706AE575C694.jpg"
class Bloco:
    def __init__(self, img):
        self.img = img
        self.folhas = {}
        self.monta = lambda *_: None
        ordem = ["%02d"%x for x in range(16)]
        desordem = ordem[:]
        from random import shuffle
        shuffle(desordem)
        self.tela = document["pydiv"]
        self.suporte = html.DIV(style=dict(position="absolute",
        left=10, top=20, width=400, height='%dpx'%400, border=1,
        borderColor="white"))
        self.folha = html.DIV(style=dict(position="absolute",
        left=410, top=20, width=450, height='%dpx'%450))
        self.tela.html = ""
        self.tela <= self.suporte
        self.tela <= self.folha
        self.pecas_colocadas = []
        #print(list(enumerate(ordem)))
        for pos, fl in enumerate(ordem):
            Suporte(self, "folha" + fl, pos//4, pos%4)
        for pos, tx in enumerate(desordem):
            Folha(self, pos//4, pos%4, int(tx)//4, int(tx)%4)

    def inicia_de_novo(self):
        pass

    def conta_pecas(self, valor_peca):
        self.pecas_colocadas += valor_peca
        if len(self.pecas_colocadas) == 4:
            if all(self.pecas_colocadas):
                input("O texto esta certo.")
            else:
                vai = input("Tentar de novo?")
                if vai == "s":
                    self.inicia_de_novo()

    def nao_monta(self):
        pass

    def vai(self):
        self.monta()
        self.monta = self.nao_monta
        # self.centro.norte.vai()


if __name__ == "__main__":
    #main()
    Bloco(OCEANO)