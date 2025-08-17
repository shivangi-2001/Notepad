from PySide6.QtWidgets import *
from PySide6.QtCore import  *
from PySide6.QtGui import *


class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self.setObjectName(u"TextEdit")
        self.setStyleSheet(u"border: 0;")
        QTimer.singleShot(0, self.setFocus)
        self.verticalScrollBar().setStyleSheet(
            """
            QScrollBar:vertical {
                border-left: 1px solid #999999;
                border-right: 1px solid #999999;
                background: #f0f0f0;
                width: 14px;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:vertical {
                background: #666666;
                min-height: 0px;
            }

            QScrollBar::add-line:vertical {
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical {
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            """
        )

    def keyPressEvent(self, event: QKeyEvent):
        if event.matches(QKeySequence.Paste):
            clipboard = QApplication.clipboard()
            clipboard_text = clipboard.text()
            self.insertPlainText(clipboard_text)
        else:
            super(TextEdit, self).keyPressEvent(event)

