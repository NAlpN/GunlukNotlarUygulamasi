# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gunluk.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 457)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gorevler = QtWidgets.QListWidget(self.centralwidget)
        self.gorevler.setGeometry(QtCore.QRect(0, 0, 271, 231))
        self.gorevler.setObjectName("gorevler")
        self.yaz = QtWidgets.QLineEdit(self.centralwidget)
        self.yaz.setGeometry(QtCore.QRect(10, 260, 231, 101))
        self.yaz.setObjectName("yaz")
        self.gorevEkle = QtWidgets.QPushButton(self.centralwidget)
        self.gorevEkle.setGeometry(QtCore.QRect(260, 250, 121, 31))
        self.gorevEkle.setObjectName("gorevEkle")
        self.gorevSil = QtWidgets.QPushButton(self.centralwidget)
        self.gorevSil.setGeometry(QtCore.QRect(260, 350, 121, 31))
        self.gorevSil.setObjectName("gorevSil")
        self.tamamlananGorevler_2 = QtWidgets.QPushButton(self.centralwidget)
        self.tamamlananGorevler_2.setGeometry(QtCore.QRect(260, 300, 121, 31))
        self.tamamlananGorevler_2.setObjectName("tamamlananGorevler_2")
        self.tamamlananGorevler = QtWidgets.QListWidget(self.centralwidget)
        self.tamamlananGorevler.setGeometry(QtCore.QRect(290, 0, 271, 231))
        self.tamamlananGorevler.setObjectName("tamamlananGorevler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gorevEkle.setText(_translate("MainWindow", "Görev Ekle"))
        self.gorevSil.setText(_translate("MainWindow", "Görev Sil"))
        self.tamamlananGorevler_2.setText(_translate("MainWindow", "Tamamlandı"))
