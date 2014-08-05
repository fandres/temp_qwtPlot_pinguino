# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'average.ui'
#
# Created: Mon Jul 21 22:44:53 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(253, 84)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 251, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.ui_buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.ui_buttonBox.setGeometry(QtCore.QRect(10, 40, 221, 41))
        self.ui_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ui_buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ui_buttonBox.setObjectName(_fromUtf8("ui_buttonBox"))
        self.layoutWidget = QtGui.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 221, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.ui_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.ui_spinBox.setWrapping(False)
        self.ui_spinBox.setMinimum(1)
        self.ui_spinBox.setMaximum(720)
        self.ui_spinBox.setProperty("value", 1)
        self.ui_spinBox.setObjectName(_fromUtf8("ui_spinBox"))
        self.horizontalLayout.addWidget(self.ui_spinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ui_comboTiempo = QtGui.QComboBox(self.layoutWidget)
        self.ui_comboTiempo.setObjectName(_fromUtf8("ui_comboTiempo"))
        self.ui_comboTiempo.addItem(_fromUtf8(""))
        self.ui_comboTiempo.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.ui_comboTiempo)
        self.label_2.setBuddy(self.ui_spinBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.ui_buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.ui_buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Average time", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setToolTip(QtGui.QApplication.translate("Dialog", "Asignar tiempo para el cual capturar y mostrar el ptomedio durante este periodo de tiempo.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Time:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_comboTiempo.setItemText(0, QtGui.QApplication.translate("Dialog", "minute(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_comboTiempo.setItemText(1, QtGui.QApplication.translate("Dialog", "hour(s)", None, QtGui.QApplication.UnicodeUTF8))

