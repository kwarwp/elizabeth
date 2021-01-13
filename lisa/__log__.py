
{'date': 'Tue Jan 12 2021 22:56:12.450 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  """ A multipla escolha é um popup com opções
  ^
IndentationError: unexpected indent
'''},
{'date': 'Tue Jan 12 2021 22:56:28.8 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 10
    RESPOSTA1= Elemento()
NameError: name 'Elemento' is not defined
'''},
{'date': 'Tue Jan 12 2021 22:58:59.745 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 13
    RESPOSTA1= Elemento(MEU_ELEMENTO, tit="PLAY", w=55,h=58, x=610, y=300, cena = nome_da_cena)
NameError: name 'Elemento' is not defined
'''},