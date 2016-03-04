# -*- coding: utf-8 -*- =>x
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
from opening import Ui_Form1
import random
import appindicator
import pynotify
import gtk

class MuslumButton(QPushButton):
    btn_i = None
    btn_j = None

class start ():
    def __init__(self):
        a=appindicator.Indicator('noti','/home/muslum/Masaüstü/battle_ship/icon.png',appindicator.CATEGORY_APPLICATION_STATUS)
        a.set_status(appindicator.STATUS_ACTIVE)
        m=gtk.Menu()

        baslat=gtk.MenuItem('Oyun Başlat')
        hakkinda=gtk.MenuItem('Hakkında')
        cikis=gtk.MenuItem('Cikis')
        m.append(baslat)
        m.append(hakkinda)
        m.append(cikis)
        a.set_menu(m)
        baslat.show()
        cikis.show()
        hakkinda.show()

        def checkStatus(item):
            print "Oyun Baslatildi"
            Widget()

        baslat.connect('activate',checkStatus)

        def quit(item):
            print "Cikis Yapiliyor..!"
            sys.exit(0)

        cikis.connect('activate',quit)

        def about(item):
            print "ne ögrenmek istersin ?"

        hakkinda.connect('activate',about)
        gtk.main()

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        win = QWidget()
        grid = QGridLayout()

        self.liste=[]
        for i in xrange(15):
            for j in xrange(15):
                btn = MuslumButton("",self)
                btn.btn_i = i
                btn.btn_j = j
                #btn.setToolTip(str(i)+str(j))
                btn.setIcon(QtGui.QIcon('ship24.png'))
                grid.addWidget(btn,i,j)
                self.liste.append(btn)

        self.dortluk=random.randrange(225)
        if self.dortluk%15>12:
            self.dortluk=self.dortluk-4
        else :
            pass
        

        self.ucluk=random.randrange(225)
        if self.ucluk%15>13:
            self.ucluk=self.ucluk-3
        else:
            pass        

        self.ikilik=random.randrange(225)
        if self.ikilik%15>14:
            self.ikilik=self.ikilik-2
        else:
            pass

        self.birlik=random.randrange(225)
        

        button= QPushButton("  Yeni Oyun")
        label = QLabel()
        label.setText("   Skor :         ")
        grid.addWidget(label,2,50)
        grid.addWidget(button,3,50)

        #self.connect(self.liste[self.dortluk],QtCore.SIGNAL('clicked()'),self.vuruldudort)
        self.liste[self.dortluk].clicked.connect(self.onClick1)
        self.liste[self.dortluk+1].clicked.connect(self.onClick2)
        self.liste[self.dortluk+2].clicked.connect(self.onClick3)
        self.liste[self.dortluk+3].clicked.connect(self.onClick4)
        self.liste[self.ucluk].clicked.connect(self.vurulduuc)
        self.liste[self.ucluk+1].clicked.connect(self.vurulduuc1)
        self.liste[self.ucluk+2].clicked.connect(self.vurulduuc2)
        self.liste[self.ikilik].clicked.connect(self.vurulduiki)
        self.liste[self.ikilik+1].clicked.connect(self.vurulduiki1)
        self.liste[self.birlik].clicked.connect(self.birlikk)


        self.statusBar = QStatusBar()
        win.setStyleSheet("background-image:url(asaa.jpg)");
        win.setLayout(grid)
        win.setGeometry(500,100,600,650)
        win.setWindowTitle("PyQt-Battle-Ship")
        win.show()
        sys.exit(app.exec_())

    def onClick1(self):
        print ">>>>>dortluk vuruldu"
        self.liste[self.dortluk].setIcon(QtGui.QIcon('fire.png'))
    def onClick2(self,gelen):
        print ">>>>>dortluk+1 vuruldu"
        self.liste[self.dortluk+1].setIcon(QtGui.QIcon('fire.png'))
    def onClick3(self,gelen):
        print ">>>>>>dortluk+2 vuruldu"
        self.liste[self.dortluk+2].setIcon(QtGui.QIcon('fire.png'))
    def onClick4(self):
        print ">>>>>dortluk+3 vuruldu"
        self.liste[self.dortluk+3].setIcon(QtGui.QIcon('fire.png'))

    def vurulduuc(self):
        print ">>>>>>ucluk vuruldu"
        self.liste[self.ucluk].setIcon(QtGui.QIcon('fire.png'))
    def vurulduuc1(self):
        print ">>>>>>ucluk+1 vuruldu"
        self.liste[self.ucluk+1].setIcon(QtGui.QIcon('fire.png'))
    def vurulduuc2(self):
        print ">>>>>>ucluk+2vuruldu"
        self.liste[self.ucluk+2].setIcon(QtGui.QIcon('fire.png'))

    def vurulduiki(self):
        print ">>>>>>ikilik vuruldu"
        self.liste[self.ikilik].setIcon(QtGui.QIcon('fire.png'))
    def vurulduiki1(self):
        print ">>>>>>ikilik+1 vuruldu"
        self.liste[self.ikilik+1].setIcon(QtGui.QIcon('fire.png'))

    def birlikk(self):
        print ">>>>>>birlik vuruldu"
        self.liste[self.birlik].setIcon(QtGui.QIcon('fire.png'))

if __name__ == '__main__':
  app = QApplication(sys.argv)
  widget = start()
  widget.show()
  sys.exit(app.exec_())