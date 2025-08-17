from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Find_TextEdit(QWidget):
    searchTextChanged = Signal(str)
    backspaceClicked = Signal()

    def __init__(self, parent=None):
        super(Find_TextEdit, self).__init__(parent)
        self.setFixedSize(330, 30)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.FindTextEdit = QLineEdit(self)
        self.FindTextEdit.setObjectName("textEdit")
        self.FindTextEdit.setMinimumSize(330, 30)
        self.FindTextEdit.setMaximumSize(16777215, 30)
        self.FindTextEdit.setFrame(False)
        QTimer.singleShot(0, self.FindTextEdit.setFocus)
        self.FindTextEdit.textChanged.connect(self.searchtext)

        self.down = QPushButton(self)
        self.down.setIcon(self.style().standardIcon(QStyle.SP_ArrowDown))

        self.up = QPushButton(self)
        self.up.setIcon(self.style().standardIcon(QStyle.SP_ArrowUp))

        self.backspace_button = QToolButton(self)
        self.backspace_button.setIcon(QIcon.fromTheme("go-previous"))
        self.backspace_button.setDisabled(True)
        self.backspace_button.clicked.connect(self.backspace_clicked)

        self.gridLayout.addWidget(self.FindTextEdit, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.down, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.up, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.backspace_button, 2, 4, 1, 1)

    def searchtext(self):
        if self.FindTextEdit.text():
            self.backspace_button.setDisabled(False)
            self.searchTextChanged.emit(self.FindTextEdit.text())
        else:
            self.backspaceClicked.emit()


    def backspace_clicked(self):
        current_text = self.FindTextEdit.text()
        if current_text == '':
            self.backspace_button.setDisabled(True)
            self.backspaceClicked.emit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.backspace_clicked()
            return
        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    notepad = Find_TextEdit()
    notepad.show()
    sys.exit(app.exec_())
