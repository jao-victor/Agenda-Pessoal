# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_deletar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.frame_7 = QtWidgets.QFrame(Dialog)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.frame_7.setStyleSheet("background-color: rgb(63, 125, 174);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_17 = QtWidgets.QLabel(self.frame_7)
        self.label_17.setGeometry(QtCore.QRect(120, 10, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: white")
        self.label_17.setObjectName("label_17")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_7)
        self.textBrowser.setGeometry(QtCore.QRect(60, 70, 271, 51))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.box_select_id_2 = QtWidgets.QFrame(self.frame_7)
        self.box_select_id_2.setGeometry(QtCore.QRect(70, 140, 260, 51))
        self.box_select_id_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.box_select_id_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_select_id_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_select_id_2.setObjectName("box_select_id_2")
        self.label_selecioneid_2 = QtWidgets.QLabel(self.box_select_id_2)
        self.label_selecioneid_2.setGeometry(QtCore.QRect(10, 16, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_selecioneid_2.setFont(font)
        self.label_selecioneid_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_selecioneid_2.setObjectName("label_selecioneid_2")
        self.id = QtWidgets.QLineEdit(self.box_select_id_2)
        self.id.setGeometry(QtCore.QRect(110, 16, 111, 21))
        self.id.setStyleSheet("color: rgb(0, 0, 0);")
        self.id.setObjectName("id")
        self.b_excluir_contato = QtWidgets.QPushButton(self.frame_7)
        self.b_excluir_contato.setGeometry(QtCore.QRect(160, 250, 80, 23))
        self.b_excluir_contato.setStyleSheet("#b_excluir_contato{\n"
"    color: white;\n"
"    background-color: red;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#b_excluir_contato:hover{\n"
"    background-color: rgb(255, 255, 0);\n"
"    color:black;\n"
"}\n"
"\n"
"#b_excluir_contato:pressed{\n"
"    background-color: rgb(0, 255, 127);\n"
"}")
        self.b_excluir_contato.setObjectName("b_excluir_contato")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_17.setText(_translate("Dialog", "DELETAR CONTATO"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Digite o id do contato para removê-lo da agenda.</span></p></body></html>"))
        self.label_selecioneid_2.setText(_translate("Dialog", "Digite o ID:"))
        self.b_excluir_contato.setText(_translate("Dialog", "EXCLUIR"))
