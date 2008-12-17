from chiplotle.hpgl.compound.compound import _CompoundHPGL

class Container(_CompoundHPGL, list):
   '''Generic container.'''
   def __init__(self, x, y, shapes=None, pen=None):
      _CompoundHPGL.__init__(self, (x, y), pen)
      shapes = shapes or [ ]
      list.__init__(self, shapes)
      self._linkUp( )

   def _linkUp(self):
      for s in self:
         s._parent = self

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      for s in self:
         result.extend(s._subcommands)
      return result
