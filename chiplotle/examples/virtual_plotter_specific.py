from chiplotle import *
from chiplotle.tools.plottertools import instantiate_virtual_plotter

'''
demonstrates the use of a virtual plotter with a specific plotter definition

you must have hp2xx installed for io.view() to work!
'''

'''
    compute size of paper:
    there are 40 plotter units per mm
    HP7550A reference lists 11x17 (ANSI B) max plot dimensions as:
    254 x 411mm
'''

paper_width = 411 * 40
paper_length = 254 * 40

plotter = instantiate_virtual_plotter(type="HP7550A", 
    left_bottom = CoordinatePair(0,0), 
    right_top = CoordinatePair(paper_width, paper_length) )

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
