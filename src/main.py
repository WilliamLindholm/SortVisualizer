import data
import sort
import time
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np

size = 100
dat = data.DataClass(size)
le = [i for i in range(size)]
alg = sort.Bubble(dat.unsorted)
alg.sort()

class MyWidget(pg.GraphicsWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)
        
        self.counter = 0
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1) # in milliseconds
        self.timer.start()
        self.timer.timeout.connect(self.onNewData)

        self.plotItem = self.addPlot(title="Bubble")

        self.plotDataItem = self.plotItem.plot([], pen=None, 
            symbolBrush=(255,0,0), symbolSize=5, symbolPen=None)


    def setData(self, x, y):
        self.plotDataItem.setData(x, y)


    def onNewData(self):
        x = le
        y = alg.steps[self.counter]
        self.counter += 1 
        self.setData(x, y)

app = QtWidgets.QApplication([])
pg.setConfigOptions(antialias=False)

win = MyWidget()
win.show()
win.resize(800, 800)
win.raise_()
app.exec_()
