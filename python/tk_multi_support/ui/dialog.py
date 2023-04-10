# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/s/apps/users/laurettea/packages/mikrosVfx/tk_multi_support/dev/tk-multi-support/resources/dialog.ui'
#
# Created: Mon Apr 10 21:21:48 2023
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
        self.lie_object = QtGui.QLineEdit(Dialog)
        self.lie_object.setObjectName("lie_object")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lie_object)
        self.txe_content = QtGui.QTextEdit(Dialog)
        self.txe_content.setObjectName("txe_content")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txe_content)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.pub_send = QtGui.QPushButton(Dialog)
        self.pub_send.setObjectName("pub_send")
        self.verticalLayout.addWidget(self.pub_send)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Problem Reporting", None, -1))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Object", None, -1))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Message", None, -1))
        self.pub_send.setText(QtGui.QApplication.translate("Dialog", "Send", None, -1))

from . import resources_rc
