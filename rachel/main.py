# elizabeth.rachel.main.py

from _spy.vitollino.main import Cena, Sala
"""A Sala é uma COLEÇÃO de cenas organizadas nos pontos cadeais norte, sul, leste e oeste
"""


 = "https://i.imgur.com/l1LeZ9x.jpeg" # Extensões aceitas: png, jpg, jpeg e gif
IMAGEM_OESTE = "https://i.imgur.com/o7cml0T.jpeg" # Extensões aceitas: png, jpg, jpeg e gif


nome_da_cena_norte = Cena(IMAGEM_LESTE)
nome_da_cena_leste = Cena(IMAGEM_OESTE)

""" Bem como na composição na Cena, a ausencia de Cena em algum dos pontos cardeais direciona para a SalaCenaNula()"""
nome_da_sala = Sala(n=nome_da_cena_norte, l=nome_da_cena_leste)

nome_da_sala.norte.vai()
#nome_da_sala.oeste.vai()