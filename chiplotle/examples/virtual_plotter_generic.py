from chiplotle import *
from chiplotle.tools.plottertools import instantiate_virtual_plotter

'''
Demonstrates the use of a virtual plotter with the generic plotter. 
Paper will automatically be set to 8.5x11" (ANSI A)

you must have hp2xx installed for io.view() to work!
'''

plotter = instantiate_virtual_plotter()

plotter.margins.soft.draw_outline()
plotter.select_pen(1)
plotter.goto(0,0)
plotter.pen_down()
plotter.goto(0,1000)
plotter.select_pen(2)
plotter.goto(1000,1000)
plotter.select_pen(3)
plotter.goto(1000,0)
plotter.select_pen(4)
plotter.goto(0,0)
plotter.select_pen(5)
plotter.goto(1000,1000)
plotter.pen_up()
plotter.select_pen(6)
plotter.goto(0,1000)
plotter.pen_down()
plotter.goto(1000,0)
plotter.pen_up()
plotter.select_pen(0)

io.view(plotter)
