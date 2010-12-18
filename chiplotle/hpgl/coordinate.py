from __future__ import division
#import numpy

class Coordinate(object):

   __slots__ = ('_x', '_y')

   def __init__(self, *args):
      if len(args) == 1 and isinstance(args[0], Coordinate):
         cp = args[0]
         self._x = cp.x
         self._y = cp.y
      elif len(args) == 1 and isinstance(args[0], (list, tuple)):
         self.__init__(*args[0])
      elif len(args) == 2:
         from chiplotle.tools.iterabletools.isiterable import isiterable
         if isiterable(args[0]) or isiterable(args[1]):
            raise TypeError('Each element in the pair must be a scalar')
         self._x = args[0]
         self._y = args[1]
      else:
         raise TypeError('args not recognized for Coordinate.')


   ## PUBLIC PROPERTIES ##

   @property
   def xy(self):
      return self.x, self.y

   @property
   def x(self):
      return self._x

   @property
   def y(self):
      return self._y


   ## OVERRIDES ##

   def __iter__(self):
      for e in self.xy:
         yield e

   def __getitem__(self, arg):
      return self.xy[arg]

   def __len__(self):
      return 2

   def __neg__(self):
      return Coordinate(-self.x, -self.y)

   def __eq__(self, arg):
      try:
         arg = Coordinate(arg)
         return (self.x == arg.x) and (self.y == arg.y)
      except:
         return False
#      if isinstance(arg, Coordinate):
#         return self.xy == arg.xy
#      else:
#         return self.xy == tuple(arg)

   def __hash__(self):
      ## TODO: what is the best way to hash this pair?
      return hash(('CP', self.x, self.y))

   def __ne__(self, arg):
      return not (self == arg)

   def __abs__(self):
      return Coordinate(abs(self.x), abs(self.y))

   def __add__(self, arg):
      from chiplotle.hpgl.coordinatearray import CoordinateArray
      try:
         arg = Coordinate(arg)
         return Coordinate(self.x + arg.x, self.y + arg.y)
      except TypeError:
         if isinstance(arg, CoordinateArray):
            return arg + self
         elif isinstance(arg, (int, float)):
            return Coordinate(self.x + arg, self.y + arg)
         else:
            raise TypeError('arg not supported.')

   def __radd__(self, arg):
      return self + arg

   def __sub__(self, arg):
      from chiplotle.hpgl.coordinatearray import CoordinateArray
      try:
         arg = Coordinate(arg)
         return Coordinate(self.x - arg.x, self.y - arg.y)
      except TypeError:
         if isinstance(arg, CoordinateArray):
            return -(arg - self)
         elif isinstance(arg, (int, float)):
            return Coordinate(self.x - arg, self.y - arg)
         else:
            raise TypeError('arg not supported.')

   def __rsub__(self, arg):
      return -(self - arg)

   def __mul__(self, arg):
      return Coordinate(self.x * arg, self.y * arg)

   def __rmul__(self, arg):
      return self * arg

   def __floordiv__(self, arg):
      if arg == 0:
         raise ZeroDivisionError
      return Coordinate(self.x // arg, self.y // arg)

   def __div__(self, arg):
      if arg == 0:
         raise ZeroDivisionError
      return Coordinate(self.x / arg, self.y / arg)

   def __truediv__(self, arg):
      if arg == 0:
         raise ZeroDivisionError
      return Coordinate(self.x / arg, self.y / arg)

   def __repr__(self):
      return 'Coordinate(%s, %s)' % (self.x, self.y)

   def __str__(self):
      return '<%s,%s>' % (self.x, self.y)
