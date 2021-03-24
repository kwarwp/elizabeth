
{'date': 'Wed Mar 24 2021 20:34:50.593 GMt-0300 (GMT-03:00) -X- SuPyGirls -X-',
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
  module <module> line 40
    ATO4().inicia()                    
  module <module> line 32
    self.HIPATIA_COSTAS = Elemento(imagem_hipatiacostas, tit="CLIQUE",
AttributeError: 'ATO4' object has no attribute 'CABANAFORA'
'''},