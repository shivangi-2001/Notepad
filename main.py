from PySide2.QtWidgets import *
from PySide2.QtGui import  *
from PySide2.QtCore import *
import os

from template.notepad import  Ui_Notepad
from Tools.LineNumberTextEdit import PlainTextEdit
from Tools.TextEdit import TextEdit


class NotepadApp(QMainWindow, Ui_Notepad):
    def __init__(self):
        super(NotepadApp, self).__init__()
        self.setupUi(self)
        self.tab_counter = 1
        self.modified_tabs = {}
        self.file_path = None
        self.new_tab()

        self.actionNew.triggered.connect(self.new_tab)
        self.tabWidget.tabCloseRequested.connect(lambda index: self.tabWidget.removeTab(index))
        self.text_edit.textChanged.connect(lambda: self.handle_text_change(self.plain_text_edit, self.text_edit))
        self.text_edit.verticalScrollBar().valueChanged.connect(lambda value: self.plain_text_edit.verticalScrollBar().setValue(value))

        self.actionNew_Window.triggered.connect(self.new_window)
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.save_as)
        self.actionSave_all.triggered.connect(self.save_all)
        self.actionClose_tab.triggered.connect(self.close_tab)
        self.actionClose_window.triggered.connect(self.close_window)
        self.actionExit.triggered.connect(self.close_window)

        self.actionZoom_in.triggered.connect(self.zoom_in)
        self.actionZoom_out.triggered.connect(self.zoom_out)
        self.actionRestore_default_zoom.triggered.connect(self.restore_zoom)
        self.actionStatus_bar.triggered.connect(self.toggle_status_bar)
        self.actionWord_Wrap.triggered.connect(self.toggle_word_wrap)

        self.line_number_label = QLabel("Ln: 1")
        self.column_number_label = QLabel("Col: 1")
        self.character_count_label = QLabel("0 characters")
        self.statusBar.addPermanentWidget(self.line_number_label)
        self.statusBar.addPermanentWidget(self.column_number_label)
        self.statusBar.addPermanentWidget(self.character_count_label)

    def zoom_in(self):
        self.text_edit.zoomInF(1.5)
        self.plain_text_edit.zoomInF(1.5)

    def zoom_out(self):
        current_font_size = self.text_edit.font().pointSizeF()
        default_font_size = QFont().pointSizeF()

        if current_font_size > default_font_size:
            self.text_edit.zoomOut(1.5)
            self.plain_text_edit.zoomOut(1.5)

    def restore_zoom(self):
        default_font = QFont()
        self.text_edit.setFont(default_font)
        self.plain_text_edit.setFont(default_font)

    def toggle_status_bar(self):
        self.statusBar.setVisible(self.actionStatus_bar.isChecked())

    def toggle_word_wrap(self):
        current_tab = self.tabWidget.currentWidget()
        if current_tab:
            text_edit = current_tab.findChild(TextEdit)
            if text_edit:
                text_edit.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere if self.actionWord_Wrap.isChecked() else QTextOption.NoWrap)


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

        self.modified_tabs[new_tab] = False



    def handle_text_change(self, plain_text_edit, text_edit):
        current_tab = self.tabWidget.currentWidget()
        if current_tab:
            text_edit = current_tab.findChild(TextEdit)
            plain_text_edit = current_tab.findChild(PlainTextEdit)
            if plain_text_edit.number > 999:
                plain_text_edit.setMaximumSize(50, 16777215)

            cursor = text_edit.textCursor()
            cursor.movePosition(QTextCursor.End)

            print(plain_text_edit.textCursor().blockNumber(), text_edit.textCursor().blockNumber())

            current_line = cursor.blockNumber() + 1
            current_column = cursor.columnNumber() + 1

            # Update status bar labels
            self.line_number_label.setText(f"Ln: {current_line}")
            self.column_number_label.setText(f"Col: {current_column}")

            character_count = len(text_edit.toPlainText())
            self.character_count_label.setText(f"{character_count} characters")

            if cursor.atEnd():
                plain_text_edit.number = len(text_edit.toPlainText().split('\n'))
                plain_text_edit.setPlainText('\n'.join(map(str, range(1, plain_text_edit.number + 1))))
                plain_text_edit.verticalScrollBar().setValue(text_edit.verticalScrollBar().maximum())

            if self.modified_tabs[current_tab] == False:
                self.modified_tabs[current_tab] = True
                self.update_tab_name()

    def new_window(self):
        new_notepad = NotepadApp()
        new_notepad.show()

    def update_tab_name(self):
        current_tab = self.tabWidget.currentWidget()
        if current_tab:
            tab_index = self.tabWidget.indexOf(current_tab)
            tab_name = self.tabWidget.tabText(tab_index)
            if self.modified_tabs[current_tab]:
                tab_name += " *"
            self.tabWidget.setTabText(tab_index, tab_name)

    def open(self):
        current_tab = self.tabWidget.currentWidget()
        if current_tab:
            self.file_path, _ = QFileDialog.getOpenFileName(current_tab, "Open File", "","NJText Files (*.njtext);;Text Files (*.txt);;All Files (*)", options=QFileDialog.DontUseNativeDialog)
            if self.file_path:
                new_tab = self.create_new_tab()
                self.tabWidget.addTab(new_tab, os.path.basename(self.file_path))
                self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(new_tab))
                self.modified_tabs[new_tab] = False

                with open(self.file_path, 'r') as file:
                    content = file.read()
                    new_tab.findChild(TextEdit).setPlainText(content)


    def save_as(self):
        current_tab = self.tabWidget.currentWidget()
        if current_tab:
            self.file_path, _ = QFileDialog.getSaveFileName(current_tab, "Save As", "",
                                                       "NJText Files (*.njtext);;Text Files (*.txt);;All Files (*)",
                                                       options=QFileDialog.DontUseNativeDialog)
            if self.file_path:
                _, file_extension = os.path.splitext(self.file_path)
                if not file_extension:
                    default_extension = ".txt"
                    self.file_path += default_extension

                text_content = current_tab.findChild(TextEdit).toPlainText()
                with open(self.file_path, 'w') as file:
                    file.write(text_content)

                tab_index = self.tabWidget.indexOf(current_tab)
                tab_name = os.path.basename(self.file_path).replace(file_extension, "")
                self.tabWidget.setTabText(tab_index, tab_name)
                self.modified_tabs[current_tab] = False
                self.update_tab_name()


    def save(self):
        if self.file_path:
            current_tab = self.tabWidget.currentWidget()
            text_content = current_tab.findChild(TextEdit).toPlainText()
            with open(self.file_path, 'w') as file:
                    file.write(text_content)

            tab_index = self.tabWidget.indexOf(current_tab)
            tab_name = os.path.basename(self.file_path).replace(os.path.splitext(self.file_path)[1], "")
            self.tabWidget.setTabText(tab_index, tab_name)
            self.modified_tabs[current_tab] = False
            self.update_tab_name()

        else:
            msg_box = QMessageBox(QMessageBox.Question, "Save Changes", "Do you want to save the changes?",
                                  QMessageBox.Save | QMessageBox.Cancel)
            msg_box.setDefaultButton(QMessageBox.Save)
            msg_box.setIcon(QMessageBox.Warning)

            result = msg_box.exec_()
            if result == QMessageBox.Save:
                self.save_as()

    def save_all(self):
        base_filename, _ = QFileDialog.getSaveFileName(self, "Save All As", "",
                                                       "Text Files (*.txt);;All Files (*)",
                                                       options=QFileDialog.DontUseNativeDialog)
        print("basename:", base_filename)
        if base_filename:
            for index in range(self.tabWidget.count()):
                tab_widget = self.tabWidget.widget(index)
                if self.modified_tabs[tab_widget]:
                    self.save_tab(tab_widget, base_filename, index)

    def save_tab(self, tab_widget, base_filename, index):
        _, file_extension = os.path.splitext(base_filename)
        if not file_extension:
            default_extension = ".txt"
            base_filename += default_extension

        directory, base_name = os.path.split(base_filename)
        base_name, file_extension = os.path.splitext(base_name)

        numbered_filename = f"{directory}/{base_name}"
        if index > 0:
            numbered_filename += f"-{index}"

        numbered_filename += f"{file_extension}"
        text_content = tab_widget.findChild(TextEdit).toPlainText()
        with open(numbered_filename, 'w') as file:
            file.write(text_content)

        tab_index = self.tabWidget.indexOf(tab_widget)
        tab_name = f"{base_name}-{index}.{file_extension}" if index > 0 else f"{base_name}.{file_extension}"
        self.tabWidget.setTabText(tab_index, tab_name)
        self.modified_tabs[tab_widget] = False
        self.update_tab_name()

    def close_tab(self):
        current_index = self.tabWidget.currentIndex()

        if current_index != -1:
            current_tab = self.tabWidget.widget(current_index)
            if self.modified_tabs[current_tab]:
                # Check for unsaved changes and prompt the user if needed
                reply = QMessageBox.question(
                    self,
                    'Unsaved Changes',
                    'Do you want to save the changes before closing?',
                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
                )

                if reply == QMessageBox.Save:
                    # Save the changes before closing
                    self.save_tab(current_tab, self.file_path, current_index)
                elif reply == QMessageBox.Cancel:
                    # Cancel the tab close operation
                    return

            # Close the current tab
            self.tabWidget.removeTab(current_index)

    def close_window(self):
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    notepad = NotepadApp()
    notepad.show()
    sys.exit(app.exec_())
