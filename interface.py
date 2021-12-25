import sys
from sys import setdlopenflags
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QFrame, QPushButton, QRadioButton, QVBoxLayout, QWidget, QLabel, QSlider, QDial, QMenuBar, QMenu, QStatusBar, QAction
from PyQt5.QtGui import QFont, QColor
from PyQt5 import QtCore 
import pyqtgraph as pg
import numpy as np
from functions import *


class quadratic(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.fram1()
        self.graphics()
        self.fram_input()
        self.fram_plot()
        self.fram2()
        
        

    def initUI(self):
        # this function initiates the graphic interface and sets the parameters of the main window
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle('Quadratic')
        self.setGeometry(300, 300, 600, 500)
        
        self.hlayoutgen=QHBoxLayout(self.centralWidget)

    def fram1(self):
        self.frame1=QFrame(self.centralWidget)
        
        self.hlayoutgen.addWidget(self.frame1)

        self.vlayout1=QVBoxLayout(self.frame1)

    def graphics(self):
        self.framegraph=QFrame(self.frame1)
        self.framegraph.setFrameShape(QFrame.StyledPanel)
        self.framegraph.setFrameShadow(QFrame.Raised)
        self.vlayout1.addWidget(self.framegraph)



    def fram_input(self):
        self.frame_input = QFrame(self.frame1)
        self.frame_input.setMaximumSize(QtCore.QSize(16777215, 75))
        

        self.frame_a = QFrame(self.frame_input)
        
        self.alabel=QLabel(self.frame_a)
        self.alabel.setText('a')

        self.lineEdit_a = QLineEdit(self.frame_a)
        self.lineEdit_a.setPlaceholderText("a_n")
        
        self.hlayout_a=QHBoxLayout(self.frame_a)
        self.hlayout_a.addWidget(self.alabel)
        self.hlayout_a.addWidget(self.lineEdit_a)


        self.frame_b = QFrame(self.frame_input)
        

        self.blabel=QLabel(self.frame_b)
        self.blabel.setText('b')

        self.lineEdit_b = QLineEdit(self.frame_b)
        self.lineEdit_b.setPlaceholderText("a_n-1")
        
        self.hlayout_b=QHBoxLayout(self.frame_b)
        self.hlayout_b.addWidget(self.blabel)
        self.hlayout_b.addWidget(self.lineEdit_b)

        self.frame_c = QFrame(self.frame_input)
        

        self.clabel=QLabel(self.frame_c)
        self.clabel.setText('c')

        self.lineEdit_c = QLineEdit(self.frame_c)
        self.lineEdit_c.setPlaceholderText("a_n-2")
        
        self.hlayout_c=QHBoxLayout(self.frame_c)
        self.hlayout_c.addWidget(self.clabel)
        self.hlayout_c.addWidget(self.lineEdit_c)

        self.hlayout_abc=QHBoxLayout(self.frame_input)
        self.hlayout_abc.addWidget(self.frame_a)
        self.hlayout_abc.addWidget(self.frame_b)
        self.hlayout_abc.addWidget(self.frame_c)

        self.vlayout1.addWidget(self.frame_input)

    def fram_plot(self):
        self.frame_plot=QFrame(self.frame1)
        self.frame_plot.setMaximumSize(QtCore.QSize(16777215, 50))

        self.vlayout1.addWidget(self.frame_plot)

        self.hlayoutplot=QHBoxLayout(self.frame_plot)

        self.plotbutton=QPushButton(self.frame_plot)
        self.plotbutton.setText('Plot')

        self.clearbutton = QPushButton(self.frame_plot)
        self.clearbutton.setText("Clear")
        self.clearbutton.clicked.connect(self.clearzer)
        
        self.hlayoutplot.addWidget(self.plotbutton)
        self.hlayoutplot.addWidget(self.clearbutton)

        

    def fram2(self):
        self.frame2=QFrame(self.centralWidget)
        self.frame2.setMaximumSize(QtCore.QSize(300, 16777215))

        self.hlayoutgen.addWidget(self.frame2)
        
        self.vlayout2=QVBoxLayout(self.frame2)

        self.framex1 = QFrame(self.frame2)

        self.vlayout2.addWidget(self.framex1)

        self.x1label=QLabel(self.framex1)
        self.x1label.setText('x1')
        self.lineEdit_x1=QLineEdit(self.framex1)
        self.lineEdit_x1.setReadOnly(True)
        self.lineEdit_x1.resize(80,20)

        self.hlayoutx1=QHBoxLayout(self.framex1)
        self.hlayoutx1.addWidget(self.x1label)
        self.hlayoutx1.addWidget(self.lineEdit_x1)

    
        self.framex2=QFrame(self.frame2)
        self.vlayout2.addWidget(self.framex2)

        self.x2label=QLabel(self.frame2)
        self.x2label.setText('x2')
        self.lineEdit_x2=QLineEdit(self.framex2)
        self.lineEdit_x2.setReadOnly(True)
        
        self.hlayoutx2 = QHBoxLayout(self.framex2)
        self.hlayoutx2.addWidget(self.x2label)
        self.hlayoutx2.addWidget(self.lineEdit_x2)

        self.rootbutton = QPushButton(self.frame2)
        self.rootbutton.setText('Roots')

        self.vlayout2.addWidget(self.rootbutton)
        self.rootbutton.clicked.connect(self.roots)

    def roots(self):
        self.value_a = int(self.lineEdit_a.text())
        self.value_b = int(self.lineEdit_b.text())
        self.value_c = int(self.lineEdit_c.text())


        rootscompute = compute_roots(trans_quad(self.value_a,self.value_b,self.value_c))

        self.lineEdit_x1.setText(str(rootscompute[0]))
        self.lineEdit_x2.setText(str(rootscompute[1]))

    def clearzer(self):
        listline_Edit=[self.lineEdit_a,self.lineEdit_b,self.lineEdit_c,self.lineEdit_x1,self.lineEdit_x2]
        for i in listline_Edit:
            i.clear()
        



        

def main():
    app = QApplication(sys.argv)
    win = quadratic()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
