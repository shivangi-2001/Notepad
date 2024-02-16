# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(572, 40)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(Frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(400, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)

        self.down = QPushButton(Frame)
        self.down.setObjectName(u"down")

        self.gridLayout.addWidget(self.down, 2, 2, 1, 1)

        self.up = QPushButton(Frame)
        self.up.setObjectName(u"up")

        self.gridLayout.addWidget(self.up, 2, 1, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.down.setText(QCoreApplication.translate("Frame", u"down", None))
        self.up.setText(QCoreApplication.translate("Frame", u"up", None))
    # retranslateUi

