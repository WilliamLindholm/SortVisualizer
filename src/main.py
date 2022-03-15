import data
import sort
import time
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np

algs = ["Quick", "Bubble", "Insertion", "Selection"]

size = 500
points = data.DataClass(size)
x = [i for i in range(size)]
result = {}

for alg in algs:
    a = 1
    if alg == "Quick":
        a = sort.Quick(points.unsorted)
        a.sort(0, size - 1)
    elif alg == "Bubble":
        a = sort.Bubble(points.unsorted)
        a.sort()
    elif alg == "Insertion":
        a = sort.Insertion(points.unsorted)
        a.sort() 
    elif alg == "Selection":
        a = sort.Selection(points.unsorted)
        a.sort()

    result[alg] = a.steps

pg.setConfigOptions(antialias = True)
pg.setConfigOptions(background = 'lightgray')
pg.setConfigOptions(foreground = 'darkred')

win = pg.GraphicsLayoutWidget(title = "Sort Visualizer", show = True)
win.resize(3840, 1600)


ps = {}
bgs = {}
rowbreak = len(algs) / 2 
i = 0
for alg in algs:

    ps[alg] = win.addPlot()
    ps[alg].setTitle(alg)
    ps[alg].hideAxis("bottom")
    ps[alg].hideAxis("left")
    bgs[alg] = pg.BarGraphItem(x = x, height = points.unsorted, 
                width = 0.3, brush = 'darkblue')
    ps[alg].addItem(bgs[alg])
    
    i += 1
    if i >= rowbreak:
        win.nextRow()
        i = 0

### Loop with timer
counter = 0
timer = pg.QtCore.QTimer()
def update_plots():
    global counter
    for alg in algs:
        if not counter >= len(result[alg]):
            bgs[alg].setOpts(height = result[alg][counter])
    counter += 1

timer.timeout.connect(update_plots)
timer.start(0)


if __name__ == '__main__':
    pg.exec()
