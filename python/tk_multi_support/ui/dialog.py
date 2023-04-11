# -*- coding: utf-8 -*-

# Form implementation generated
#
# Created: Tue Apr 11 23:38:46 2023
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 392)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lab_subject = QtGui.QLabel(Dialog)
        self.lab_subject.setObjectName("lab_subject")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lab_subject)
        self.lie_subject = QtGui.QLineEdit(Dialog)
        self.lie_subject.setObjectName("lie_subject")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lie_subject)
        self.lab_content = QtGui.QLabel(Dialog)
        self.lab_content.setObjectName("lab_content")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lab_content)
        self.txe_content = QtGui.QTextEdit(Dialog)
        self.txe_content.setObjectName("txe_content")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txe_content)
        self.lab_thumbnail = QtGui.QLabel(Dialog)
        self.lab_thumbnail.setObjectName("lab_thumbnail")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lab_thumbnail)
        self.item_thumbnail = Thumbnail(Dialog)
        self.item_thumbnail.setMinimumSize(QtCore.QSize(160, 90))
        self.item_thumbnail.setMaximumSize(QtCore.QSize(160, 90))
        self.item_thumbnail.setText("")
        self.item_thumbnail.setPixmap(QtGui.QPixmap(":/tk_multi_support/camera.png"))
        self.item_thumbnail.setScaledContents(True)
        self.item_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.item_thumbnail.setObjectName("item_thumbnail")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.item_thumbnail)
        self.verticalLayout.addLayout(self.formLayout)
        self.pub_send = QtGui.QPushButton(Dialog)
        self.pub_send.setObjectName("pub_send")
        self.verticalLayout.addWidget(self.pub_send)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Problem Reporting", None, -1))
        self.lab_subject.setText(QtGui.QApplication.translate("Dialog", "Subject", None, -1))
        self.lie_subject.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Subject", None, -1))
        self.lab_content.setText(QtGui.QApplication.translate("Dialog", "Message", None, -1))
        self.txe_content.setPlaceholderText(QtGui.QApplication.translate("Dialog", "What\'s going wrong ?", None, -1))
        self.lab_thumbnail.setText(QtGui.QApplication.translate("Dialog", "Thumbnail", None, -1))
        self.item_thumbnail.setToolTip(QtGui.QApplication.translate("Dialog", "Click to take a screenshot.", None, -1))
        self.item_thumbnail.setAccessibleName(QtGui.QApplication.translate("Dialog", "item thumbnail", None, -1))
        self.pub_send.setText(QtGui.QApplication.translate("Dialog", "Send", None, -1))

from ..thumbnail import Thumbnail
from . import resources_rc
