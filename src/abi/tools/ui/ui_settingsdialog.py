# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\abi\tools\ui\settingsdialog.ui'
#
# Created: Thu Aug  2 12:57:57 2018
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
        self.frame = QtGui.QFrame(SettingsDialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.version_label = QtGui.QLabel(self.frame)
        self.version_label.setObjectName("version_label")
        self.horizontalLayout_2.addWidget(self.version_label)
        self.versionDisplay_label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionDisplay_label.sizePolicy().hasHeightForWidth())
        self.versionDisplay_label.setSizePolicy(sizePolicy)
        self.versionDisplay_label.setObjectName("versionDisplay_label")
        self.horizontalLayout_2.addWidget(self.versionDisplay_label)
        self.verticalLayout.addWidget(self.frame)
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
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.version_label.setText(QtGui.QApplication.translate("SettingsDialog", "Version:", None, QtGui.QApplication.UnicodeUTF8))
        self.versionDisplay_label.setText(QtGui.QApplication.translate("SettingsDialog", "Display version number here", None, QtGui.QApplication.UnicodeUTF8))
        self.registeredLocations_groupBox.setTitle(QtGui.QApplication.translate("SettingsDialog", "Registered locations:", None, QtGui.QApplication.UnicodeUTF8))

