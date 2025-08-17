from PySide6.QtWidgets import *
from PySide6.QtCore import  *
from PySide6.QtGui import *

class PlainTextEdit(QTextEdit):
    def __init__(self, parent=None):
        self.number = 1
        super(PlainTextEdit, self).__init__(parent)
        self.setObjectName(u"plainTextEdit")
        self.setMaximumSize(40, 16777215)
        self.setStyleSheet(u"border: 0;background-color:rgba(235,235,235,255); font-weight:bold;")
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setReadOnly(True)

        self.setPlainText(str(self.number))


