#matplotlib, numpy, pyplot
#Tony Crewe
#Oct 2018

import simplegui as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import numpy as np
import tkinter as tk

"""
Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.
Adapted: From https://gitlab.com/lotspaih/PySimpleGUI/tree/master

Basic steps are:
 * Create a Canvas Element
 * Layout form
 * Display form (NON BLOCKING)
 * Draw plots onto convas
 * Display form (BLOCKING)
"""

#No exactly sure how all this works, but taken from example given as a template.
def draw_figure(canvas, figure, loc = (0,0)):

    figure_canvas_agg = FigureCanvasAgg(figure) 
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo


#------------ Matplotlib code ----------------------
#see https://matplotlib.org/
fig = plt.figure()
ax = fig.add_subplot(111)
#x-values
x = np.linspace(-np.pi*2, np.pi*2, 100)
#y-values
y = np.sin(x)
plt.plot(x,y)

ax.set_title('sin(x)')
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

#------------End Matplotlib code --------------------

layout = [[sg.Text('Plot Test - PySimpleGUI and Matplotlib', font = ('Calibri', 18, 'bold'))],
          [sg.Canvas(size = (figure_w, figure_h), key = '_canvas_')],
          [sg.OK(pad=((figure_w / 2, 0), 3), size=(6, 2))]]

window = sg.Window('Matplot in PySimpleGUI', force_toplevel = True).Layout(layout).Finalize()

fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)

button, value = window.Read()


