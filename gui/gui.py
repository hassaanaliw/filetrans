from PyQt4.QtCore import SIGNAL
import sys
from PyQt4 import QtCore, QtGui, uic
import os,goslate
import urllib2


form_class = uic.loadUiType("ui.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.filebut, SIGNAL("clicked()"),self.filebut_click)
        self.connect(self.trans, SIGNAL("clicked()"),self.trans_click)

        self.setStyleSheet("QMainWindow {background-color: #313645; color : black}")

        self.trans.setStyleSheet("background : #3ba86a")
        self.from1.setStyleSheet("background : #3ba86a;border : blue")
        self.to1.setStyleSheet("background : #3ba86a;border : blue")
        self.fileed.setStyleSheet("background : #3ba86a; border : blue")
        self.label.setStyleSheet("color: #3ba86a")
        self.fileed_2.setStyleSheet("background : #3ba86a; border : blue")
        self.label_2.setStyleSheet("color: #3ba86a")
        self.filebut.setStyleSheet("background-color: red")

    def filebut_click(self):
        file = str(QtGui.QFileDialog.getOpenFileName(self, "Select File"))
        name = file.split('.')
        self.fileed.setText(file)
        self.fileed_2.setText(name[0]+'-translated.'+name[len(name)-1])

    def trans_click(self):
        if self.fileed.text() == "":
            self.sb.setStyleSheet("color: red")
            self.sb.setText("No File Given!")
        elif not os.path.isfile(self.fileed.text()):
            self.sb.setStyleSheet("color: red")
            self.sb.setText("No Such File!")
        else:
            target = open(self.fileed.text(),'r')
            tar = target.read()
            translator = goslate.Goslate()

            try:

             text = translator.translate(tar,str(self.to1.text()),str(self.from1.text()))
             new = open(self.fileed_2.text(),'wb')
             new.write(text.encode('utf-8'))
             new.close()
             target.close()
             self.sb.setStyleSheet("color: green")
             self.sb.setText("Finished!")
            except urllib2.URLError:
                self.sb.setStyleSheet("color: red")
                self.sb.setText("Internet Connection Error!")

















app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()