
{'date': 'Fri Dec 11 2020 16:03:38.828 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print("Eu fui à feira com a" diga_o_nome)
                                ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Dec 11 2020 16:03:46.423 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print("Eu fui à feira com a" diga_o_nome)
                                ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Dec 11 2020 16:04:38.611 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print(f'Eu fui à feira com a' diga_o_nome)
                                 ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Dec 11 2020 16:05:56.506 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  novo nome = diga_o_nome
        ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Dec 11 2020 18:14:38.494 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 12
  CENARIO = http://cardolettoilustrador.com.br/wp-content/uploads/estudo-cen%C3%A1rio.jpg
                 ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Dec 11 2020 18:15:50.72 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 27
    nome_escolhido = nome_jogador()
  module <module> line 20
    nome_personagem= pergunta_nome
NameError: name 'pergunta_nome' is not defined
'''},
{'date': 'Fri Dec 11 2020 18:17:22.739 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 46
    Entrada().start_eng()
  module <module> line 36
    BOTAO_PLAY= Elemento(imagem_play, tit= "click" ,cena = PLAY)
NameError: name 'PLAY' is not defined
'''},
{'date': 'Fri Dec 11 2020 18:18:27.871 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 44
    Entrada().start_eng()
  module <module> line 35
    self.BOTAO_PLAY.elt.bind("click", Nome_jogador)
NameError: name 'Nome_jogador' is not defined
'''},