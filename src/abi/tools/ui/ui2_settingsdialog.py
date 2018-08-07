# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\abi\tools\ui\settingsdialog.ui'
#
# Created: Thu Aug  2 12:28:43 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.registeredLocations_groupBox = QtGui.QGroupBox(SettingsDialog)
        self.registeredLocations_groupBox.setObjectName("registeredLocations_groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.registeredLocations_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.registeredLocations_plainTextEdit = QtGui.QPlainTextEdit(self.registeredLocations_groupBox)
        self.registeredLocations_plainTextEdit.setObjectName("registeredLocations_plainTextEdit")
        self.horizontalLayout.addWidget(self.registeredLocations_plainTextEdit)
        self.verticalLayout.addWidget(self.registeredLocations_groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.registeredLocations_groupBox.setTitle(QtGui.QApplication.translate("SettingsDialog", "Registered locations:", None, QtGui.QApplication.UnicodeUTF8))

