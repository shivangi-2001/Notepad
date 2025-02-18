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
        Notepad.setStyleSheet(u"")
        self.actionNew = QAction(Notepad)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.setCheckable(False)
        self.actionNew.setShortcutContext(Qt.WidgetShortcut)
        self.actionNew.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionNew.setShortcutVisibleInContextMenu(True)
        self.actionNew_Window = QAction(Notepad)
        self.actionNew_Window.setObjectName(u"actionNew_Window")
        self.actionNew_Window.setShortcutContext(Qt.ApplicationShortcut)
        self.actionOpen = QAction(Notepad)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setShortcutContext(Qt.ApplicationShortcut)
        self.actionSave = QAction(Notepad)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(Notepad)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(Notepad)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSave_all = QAction(Notepad)
        self.actionSave_all.setObjectName(u"actionSave_all")
        self.actionPage_setup = QAction(Notepad)
        self.actionPage_setup.setObjectName(u"actionPage_setup")
        self.actionPrint = QAction(Notepad)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionClose_tab = QAction(Notepad)
        self.actionClose_tab.setObjectName(u"actionClose_tab")
        self.actionClose_window = QAction(Notepad)
        self.actionClose_window.setObjectName(u"actionClose_window")
        self.actionUndo = QAction(Notepad)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionCut = QAction(Notepad)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(Notepad)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(Notepad)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionDelete = QAction(Notepad)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionFind = QAction(Notepad)
        self.actionFind.setObjectName(u"actionFind")
        self.actionFind_next = QAction(Notepad)
        self.actionFind_next.setObjectName(u"actionFind_next")
        self.actionFind_previous = QAction(Notepad)
        self.actionFind_previous.setObjectName(u"actionFind_previous")
        self.actionReplace = QAction(Notepad)
        self.actionReplace.setObjectName(u"actionReplace")
        self.actionGo_to = QAction(Notepad)
        self.actionGo_to.setObjectName(u"actionGo_to")
        self.actionSelect_all = QAction(Notepad)
        self.actionSelect_all.setObjectName(u"actionSelect_all")
        self.actionTime_Date = QAction(Notepad)
        self.actionTime_Date.setObjectName(u"actionTime_Date")
        self.actionTime_Date.setCheckable(True)
        self.actionFont = QAction(Notepad)
        self.actionFont.setObjectName(u"actionFont")
        self.actionStatus_bar = QAction(Notepad)
        self.actionStatus_bar.setObjectName(u"actionStatus_bar")
        self.actionStatus_bar.setCheckable(True)
        self.actionStatus_bar.setChecked(True)
        self.actionWord_Wrap = QAction(Notepad)
        self.actionWord_Wrap.setObjectName(u"actionWord_Wrap")
        self.actionWord_Wrap.setCheckable(True)
        self.actionWord_Wrap.setChecked(True)
        self.actionZoom_in = QAction(Notepad)
        self.actionZoom_in.setObjectName(u"actionZoom_in")
        self.actionZoom_out = QAction(Notepad)
        self.actionZoom_out.setObjectName(u"actionZoom_out")
        self.actionRestore_default_zoom = QAction(Notepad)
        self.actionRestore_default_zoom.setObjectName(u"actionRestore_default_zoom")
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
        self.menubar.setGeometry(QRect(0, 0, 800, 27))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.menubar.setFont(font)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuZoom = QMenu(self.menuView)
        self.menuZoom.setObjectName(u"menuZoom")
        Notepad.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(Notepad)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setEnabled(True)
        self.statusBar.setMinimumSize(QSize(0, 30))
        self.statusBar.setInputMethodHints(Qt.ImhNone)
        self.statusBar.setSizeGripEnabled(True)
        Notepad.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave_all)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPage_setup)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_tab)
        self.menuFile.addAction(self.actionClose_window)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFind_next)
        self.menuEdit.addAction(self.actionFind_previous)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addAction(self.actionGo_to)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_all)
        self.menuEdit.addAction(self.actionTime_Date)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFont)
        self.menuView.addAction(self.menuZoom.menuAction())
        self.menuView.addAction(self.actionStatus_bar)
        self.menuView.addAction(self.actionWord_Wrap)
        self.menuZoom.addAction(self.actionZoom_in)
        self.menuZoom.addAction(self.actionZoom_out)
        self.menuZoom.addAction(self.actionRestore_default_zoom)

        self.retranslateUi(Notepad)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Notepad)
    # setupUi

    def retranslateUi(self, Notepad):
        Notepad.setWindowTitle(QCoreApplication.translate("Notepad", u"Notepad", None))
        self.actionNew.setText(QCoreApplication.translate("Notepad", u"New tab", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.actionNew_Window.setText(QCoreApplication.translate("Notepad", u"New window", None))
#if QT_CONFIG(shortcut)
        self.actionNew_Window.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("Notepad", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("Notepad", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("Notepad", u"Save as", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("Notepad", u"Exit", None))
        self.actionSave_all.setText(QCoreApplication.translate("Notepad", u"Save all", None))
        self.actionPage_setup.setText(QCoreApplication.translate("Notepad", u"Page setup", None))
        self.actionPrint.setText(QCoreApplication.translate("Notepad", u"Print", None))
        self.actionClose_tab.setText(QCoreApplication.translate("Notepad", u"Close tab", None))
        self.actionClose_window.setText(QCoreApplication.translate("Notepad", u"Close window", None))
        self.actionUndo.setText(QCoreApplication.translate("Notepad", u"Undo", None))
        self.actionCut.setText(QCoreApplication.translate("Notepad", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("Notepad", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("Notepad", u"Paste", None))
        self.actionDelete.setText(QCoreApplication.translate("Notepad", u"Delete", None))
        self.actionFind.setText(QCoreApplication.translate("Notepad", u"Find", None))
#if QT_CONFIG(shortcut)
        self.actionFind.setShortcut(QCoreApplication.translate("Notepad", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionFind_next.setText(QCoreApplication.translate("Notepad", u"Find next", None))
        self.actionFind_previous.setText(QCoreApplication.translate("Notepad", u"Find previous", None))
        self.actionReplace.setText(QCoreApplication.translate("Notepad", u"Replace", None))
#if QT_CONFIG(shortcut)
        self.actionReplace.setShortcut(QCoreApplication.translate("Notepad", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionGo_to.setText(QCoreApplication.translate("Notepad", u"Go to", None))
#if QT_CONFIG(shortcut)
        self.actionGo_to.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.actionSelect_all.setText(QCoreApplication.translate("Notepad", u"Select all", None))
        self.actionTime_Date.setText(QCoreApplication.translate("Notepad", u"Time/Date", None))
        self.actionFont.setText(QCoreApplication.translate("Notepad", u"Font", None))
        self.actionStatus_bar.setText(QCoreApplication.translate("Notepad", u"Status bar", None))
        self.actionWord_Wrap.setText(QCoreApplication.translate("Notepad", u"Word wrap", None))
        self.actionZoom_in.setText(QCoreApplication.translate("Notepad", u"Zoom in", None))
#if QT_CONFIG(shortcut)
        self.actionZoom_in.setShortcut(QCoreApplication.translate("Notepad", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionZoom_out.setText(QCoreApplication.translate("Notepad", u"Zoom out", None))
#if QT_CONFIG(shortcut)
        self.actionZoom_out.setShortcut(QCoreApplication.translate("Notepad", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionRestore_default_zoom.setText(QCoreApplication.translate("Notepad", u"Restore default zoom", None))
        self.menuFile.setTitle(QCoreApplication.translate("Notepad", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Notepad", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("Notepad", u"View", None))
        self.menuZoom.setTitle(QCoreApplication.translate("Notepad", u"Zoom", None))
    # retranslateUi

