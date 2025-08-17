from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class GoTo(QDialog):
    go_to_line = Signal()
    def __init__(self, parent=None):
        super(GoTo, self).__init__(parent)

        if not self.objectName():
            self.setObjectName("Dialog")
        self.setFixedSize(361, 165)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(25, 10, 25, 10)
        self.GoToLineEdit = QLineEdit(self.widget)
        self.GoToLineEdit.setObjectName("GoToLineEdit")
        font = QFont()
        font.setPointSize(12)
        self.GoToLineEdit.setFont(font)

        self.gridLayout_2.addWidget(self.GoToLineEdit, 2, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(QFont.Weight.Normal)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        font2 = QFont()
        font2.setPointSize(13)
        self.label_2.setFont(font2)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout_2.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.setWindowTitle("Go To Line")
        self.label.setText("Go To Line")
        self.label_2.setText("Line Number: ")
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # Set up the validator for the line edit
        validator = QIntValidator(1, 2147483647)  # Set the range as needed
        self.GoToLineEdit.setValidator(validator)

        self.GoToLineEdit.textChanged.connect(lambda:self.go_to_line.emit())




# Example usage:
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    goToDialog = GoTo()
    goToDialog.show()
    sys.exit(app.exec_())
