# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_temperatura.ui'
#
# Created: Fri May  2 13:35:36 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(745, 308)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/graph.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ui_qwtPlot = QwtPlot(self.centralwidget)
        self.ui_qwtPlot.setEnabled(False)
        self.ui_qwtPlot.setObjectName(_fromUtf8("ui_qwtPlot"))
        self.gridLayout_2.addWidget(self.ui_qwtPlot, 0, 0, 2, 1)
        self.ui_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.ui_groupBox.setEnabled(False)
        self.ui_groupBox.setObjectName(_fromUtf8("ui_groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.ui_groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.ui_label_2 = QtGui.QLabel(self.ui_groupBox)
        self.ui_label_2.setObjectName(_fromUtf8("ui_label_2"))
        self.gridLayout.addWidget(self.ui_label_2, 4, 0, 1, 1)
        self.ui_lcdNumber_2 = QtGui.QLCDNumber(self.ui_groupBox)
        self.ui_lcdNumber_2.setObjectName(_fromUtf8("ui_lcdNumber_2"))
        self.gridLayout.addWidget(self.ui_lcdNumber_2, 6, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 120, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        self.ui_label = QtGui.QLabel(self.ui_groupBox)
        self.ui_label.setObjectName(_fromUtf8("ui_label"))
        self.gridLayout.addWidget(self.ui_label, 0, 0, 1, 1)
        self.ui_lcdNumber = QtGui.QLCDNumber(self.ui_groupBox)
        self.ui_lcdNumber.setObjectName(_fromUtf8("ui_lcdNumber"))
        self.gridLayout.addWidget(self.ui_lcdNumber, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.ui_groupBox, 0, 1, 1, 1)
        self.ui_botonIniciar = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/conectar.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui_botonIniciar.setIcon(icon1)
        self.ui_botonIniciar.setObjectName(_fromUtf8("ui_botonIniciar"))
        self.gridLayout_2.addWidget(self.ui_botonIniciar, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 745, 20))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menu_Action = QtGui.QMenu(self.menuBar)
        self.menu_Action.setObjectName(_fromUtf8("menu_Action"))
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/exit.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.action_Average = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/edit.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Average.setIcon(icon3)
        self.action_Average.setObjectName(_fromUtf8("action_Average"))
        self.menuTools.addAction(self.action_Average)
        self.menu_Action.addAction(self.actionExit)
        self.menuBar.addAction(self.menu_Action.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.toolBar.addAction(self.action_Average)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Adquisición", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "INFO", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_label_2.setText(QtGui.QApplication.translate("MainWindow", "Promedio 30 min", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_label.setText(QtGui.QApplication.translate("MainWindow", "Promedio 1 min", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_botonIniciar.setToolTip(QtGui.QApplication.translate("MainWindow", "Inicia la adquisición de datos.", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_botonIniciar.setText(QtGui.QApplication.translate("MainWindow", "&Iniciar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Action.setTitle(QtGui.QApplication.translate("MainWindow", "&Action", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setToolTip(QtGui.QApplication.translate("MainWindow", "Termina la conexión correctamente y sale de la aplicación.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Average.setText(QtGui.QApplication.translate("MainWindow", "&Average", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Average.setToolTip(QtGui.QApplication.translate("MainWindow", "Cambia el tiempo en el cual se promedia al temperatura.", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Average.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))

#from qwt_plot import QwtPlot
from PyQt4.Qwt5.Qwt import QwtPlot
import icons_rc
