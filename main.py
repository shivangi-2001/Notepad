from PySide2.QtWidgets import *
from PySide2.QtGui import  *
from template.notepad import  Ui_Notepad
from Tools.LineNumberTextEdit import PlainTextEdit
from Tools.TextEdit import TextEdit


class NotepadApp(QMainWindow, Ui_Notepad):
    def __init__(self):
        super(NotepadApp, self).__init__()
        self.setupUi(self)
        self.tab_counter = 1
        self.new_tab()

        self.actionNew.triggered.connect(self.new_tab)
        self.tabWidget.tabCloseRequested.connect(lambda index: self.tabWidget.removeTab(index))
        self.text_edit.verticalScrollBar().valueChanged.connect(lambda value: self.plain_text_edit.verticalScrollBar().setValue(value))

        self.actionNew_Window.triggered.connect(self.new_window)
    def create_new_tab(self):
        new_tab = QWidget()

        layout = QHBoxLayout(new_tab)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.plain_text_edit = PlainTextEdit(new_tab)
        self.text_edit = TextEdit(new_tab)
        self.text_edit.textChanged.connect(lambda: self.handle_text_change(self.plain_text_edit, self.text_edit))
        layout.addWidget(self.plain_text_edit)
        layout.addWidget(self.text_edit)
        new_tab.setLayout(layout)
        return new_tab

    def new_tab(self):
        new_tab = self.create_new_tab()
        self.tabWidget.addTab(new_tab, f"Untitled {self.tab_counter}")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(new_tab))
        self.tab_counter += 1

    def handle_text_change(self, plain_text_edit, text_edit):
        cursor = text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        if cursor.atEnd():
            # If cursor is at the end, adjust the plain text accordingly
            plain_text_edit.number = len(text_edit.toPlainText().split('\n'))
            plain_text_edit.setPlainText('\n'.join(map(str, range(1, plain_text_edit.number + 1))))
            plain_text_edit.verticalScrollBar().setValue(plain_text_edit.verticalScrollBar().maximum())

    def new_window(self):
        new_notepad = NotepadApp()
        new_notepad.show()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    notepad = NotepadApp()
    notepad.show()
    sys.exit(app.exec_())
