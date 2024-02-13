# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notepad.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Notepad(object):
    def setupUi(self, Notepad):
        if not Notepad.objectName():
            Notepad.setObjectName(u"Notepad")
        Notepad.resize(800, 600)
        self.actionNew = QAction(Notepad)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew_Window = QAction(Notepad)
        self.actionNew_Window.setObjectName(u"actionNew_Window")
        self.actionOpen = QAction(Notepad)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(Notepad)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(Notepad)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(Notepad)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(Notepad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"padding: 0px")
        self.tabWidget.setTabsClosable(True)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        Notepad.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Notepad)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        Notepad.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(Notepad)
        self.statusBar.setObjectName(u"statusBar")
        Notepad.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(Notepad)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Notepad)
    # setupUi

    def retranslateUi(self, Notepad):
        Notepad.setWindowTitle(QCoreApplication.translate("Notepad", u"Notepad", None))
        self.actionNew.setText(QCoreApplication.translate("Notepad", u"New File", None))
        self.actionNew_Window.setText(QCoreApplication.translate("Notepad", u"New Window", None))
        self.actionOpen.setText(QCoreApplication.translate("Notepad", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("Notepad", u"Save ...", None))
        self.actionSave_As.setText(QCoreApplication.translate("Notepad", u"Save As ...", None))
        self.actionExit.setText(QCoreApplication.translate("Notepad", u"Exit", None))
        self.menuFile.setTitle(QCoreApplication.translate("Notepad", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Notepad", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("Notepad", u"View", None))
    # retranslateUi

