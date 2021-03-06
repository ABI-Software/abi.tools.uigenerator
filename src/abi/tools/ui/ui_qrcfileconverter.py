# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\abi\tools\ui\qrcfileconverter.ui'
#
# Created: Thu Aug  2 12:28:38 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_QrcFileConverterDialog(object):
    def setupUi(self, QrcFileConverterDialog):
        QrcFileConverterDialog.setObjectName("QrcFileConverterDialog")
        QrcFileConverterDialog.resize(561, 392)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/ABILogo_Colour.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QrcFileConverterDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(QrcFileConverterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qrc_frame = QtGui.QFrame(QrcFileConverterDialog)
        self.qrc_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qrc_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.qrc_frame.setObjectName("qrc_frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.qrc_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qrcFile_label = QtGui.QLabel(self.qrc_frame)
        self.qrcFile_label.setObjectName("qrcFile_label")
        self.horizontalLayout.addWidget(self.qrcFile_label)
        self.qrcFile_comboBox = QtGui.QComboBox(self.qrc_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qrcFile_comboBox.sizePolicy().hasHeightForWidth())
        self.qrcFile_comboBox.setSizePolicy(sizePolicy)
        self.qrcFile_comboBox.setObjectName("qrcFile_comboBox")
        self.horizontalLayout.addWidget(self.qrcFile_comboBox)
        self.qrcFile_pushButton = QtGui.QPushButton(self.qrc_frame)
        self.qrcFile_pushButton.setObjectName("qrcFile_pushButton")
        self.horizontalLayout.addWidget(self.qrcFile_pushButton)
        self.verticalLayout.addWidget(self.qrc_frame)
        self.sideBySide_groupBox = QtGui.QGroupBox(QrcFileConverterDialog)
        self.sideBySide_groupBox.setCheckable(True)
        self.sideBySide_groupBox.setObjectName("sideBySide_groupBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.sideBySide_groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.outDir_label = QtGui.QLabel(self.sideBySide_groupBox)
        self.outDir_label.setObjectName("outDir_label")
        self.horizontalLayout_3.addWidget(self.outDir_label)
        self.outDir_lineEdit = QtGui.QLineEdit(self.sideBySide_groupBox)
        self.outDir_lineEdit.setObjectName("outDir_lineEdit")
        self.horizontalLayout_3.addWidget(self.outDir_lineEdit)
        self.outDir_pushButton = QtGui.QPushButton(self.sideBySide_groupBox)
        self.outDir_pushButton.setObjectName("outDir_pushButton")
        self.horizontalLayout_3.addWidget(self.outDir_pushButton)
        self.verticalLayout.addWidget(self.sideBySide_groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.screen_label = QtGui.QLabel(QrcFileConverterDialog)
        self.screen_label.setText("")
        self.screen_label.setObjectName("screen_label")
        self.verticalLayout.addWidget(self.screen_label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.quit_frame = QtGui.QFrame(QrcFileConverterDialog)
        self.quit_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.quit_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.quit_frame.setObjectName("quit_frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.quit_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtGui.QPushButton(self.quit_frame)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/settings_grey_48x48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtGui.QSpacerItem(457, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.quit_pushButton = QtGui.QPushButton(self.quit_frame)
        self.quit_pushButton.setObjectName("quit_pushButton")
        self.horizontalLayout_2.addWidget(self.quit_pushButton)
        self.verticalLayout.addWidget(self.quit_frame)

        self.retranslateUi(QrcFileConverterDialog)
        QtCore.QMetaObject.connectSlotsByName(QrcFileConverterDialog)

    def retranslateUi(self, QrcFileConverterDialog):
        QrcFileConverterDialog.setWindowTitle(QtGui.QApplication.translate("QrcFileConverterDialog", "Qrc File Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.qrcFile_label.setText(QtGui.QApplication.translate("QrcFileConverterDialog", "Qrc File:", None, QtGui.QApplication.UnicodeUTF8))
        self.qrcFile_pushButton.setText(QtGui.QApplication.translate("QrcFileConverterDialog", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.sideBySide_groupBox.setTitle(QtGui.QApplication.translate("QrcFileConverterDialog", "side-by-side output", None, QtGui.QApplication.UnicodeUTF8))
        self.outDir_label.setText(QtGui.QApplication.translate("QrcFileConverterDialog", "Output directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.outDir_pushButton.setText(QtGui.QApplication.translate("QrcFileConverterDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.quit_pushButton.setText(QtGui.QApplication.translate("QrcFileConverterDialog", "Quit", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
