# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_adicionar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(363, 443)
        Dialog.setMinimumSize(QtCore.QSize(363, 443))
        Dialog.setMaximumSize(QtCore.QSize(363, 443))
        Dialog.setStyleSheet("")
        self.scrollAreaAdicionar = QtWidgets.QScrollArea(Dialog)
        self.scrollAreaAdicionar.setGeometry(QtCore.QRect(0, 0, 361, 441))
        self.scrollAreaAdicionar.setStyleSheet("\n"
"\n"
"QScrollBar:vertical {\n"
"    \n"
"background-color: rgb(63, 125, 174);\n"
"}\n"
"\n"
"QScrollBar::handle:sub-page:vertical{\n"
"            \n"
"    background-color: rgb(255, 218, 77);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    background-color: rgb(63, 125, 174);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    background-color: rgb(63, 125, 174);\n"
"}\n"
"\n"
"")
        self.scrollAreaAdicionar.setWidgetResizable(True)
        self.scrollAreaAdicionar.setObjectName("scrollAreaAdicionar")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -149, 345, 588))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(63, 125, 174);\n"
"")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 570))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.labelAdicionar = QtWidgets.QLabel(self.frame_3)
        self.labelAdicionar.setGeometry(QtCore.QRect(90, 0, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAdicionar.setFont(font)
        self.labelAdicionar.setStyleSheet("color: white;")
        self.labelAdicionar.setObjectName("labelAdicionar")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(13, 30, 301, 121))
        self.frame_4.setStyleSheet("background-color: white;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(2, 2, 101, 16))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(15, 30, 41, 16))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.nome = QtWidgets.QLineEdit(self.frame_4)
        self.nome.setGeometry(QtCore.QRect(60, 30, 221, 20))
        self.nome.setStyleSheet("color: rgb(0, 0, 0);")
        self.nome.setObjectName("nome")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(15, 60, 41, 16))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(15, 90, 41, 16))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.email = QtWidgets.QLineEdit(self.frame_4)
        self.email.setGeometry(QtCore.QRect(60, 90, 221, 21))
        self.email.setStyleSheet("color: rgb(0, 0, 0);")
        self.email.setObjectName("email")
        self.data = QtWidgets.QDateEdit(self.frame_4)
        self.data.setGeometry(QtCore.QRect(60, 60, 221, 24))
        self.data.setStyleSheet("color: black;")
        self.data.setObjectName("data")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(282, 33, 16, 16))
        self.label_11.setStyleSheet("color: red;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(282, 67, 16, 16))
        self.label_12.setStyleSheet("color: red;")
        self.label_12.setObjectName("label_12")
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setGeometry(QtCore.QRect(282, 92, 16, 16))
        self.label_19.setStyleSheet("color: red;")
        self.label_19.setObjectName("label_19")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(13, 169, 301, 231))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(2, 2, 57, 15))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.rua = QtWidgets.QLineEdit(self.frame_5)
        self.rua.setGeometry(QtCore.QRect(60, 40, 221, 21))
        self.rua.setStyleSheet("color: black;")
        self.rua.setObjectName("rua")
        self.condomio = QtWidgets.QLineEdit(self.frame_5)
        self.condomio.setGeometry(QtCore.QRect(100, 120, 181, 21))
        self.condomio.setStyleSheet("color: black;")
        self.condomio.setObjectName("condomio")
        self.numero_endereco = QtWidgets.QLineEdit(self.frame_5)
        self.numero_endereco.setGeometry(QtCore.QRect(80, 80, 201, 21))
        self.numero_endereco.setStyleSheet("color: black;")
        self.numero_endereco.setObjectName("numero_endereco")
        self.bairro = QtWidgets.QLineEdit(self.frame_5)
        self.bairro.setGeometry(QtCore.QRect(70, 165, 211, 21))
        self.bairro.setStyleSheet("color: black;")
        self.bairro.setObjectName("bairro")
        self.cidade = QtWidgets.QLineEdit(self.frame_5)
        self.cidade.setGeometry(QtCore.QRect(70, 200, 211, 21))
        self.cidade.setStyleSheet("color: black;")
        self.cidade.setObjectName("cidade")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(10, 40, 31, 16))
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 57, 15))
        self.label_2.setStyleSheet("color: black;")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 57, 15))
        self.label_8.setStyleSheet("color: black;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setGeometry(QtCore.QRect(10, 200, 51, 16))
        self.label_9.setStyleSheet("color: black;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.label_10.setStyleSheet("color: black;")
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setGeometry(QtCore.QRect(282, 202, 16, 16))
        self.label_13.setStyleSheet("color: red;")
        self.label_13.setObjectName("label_13")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(13, 420, 301, 91))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setGeometry(QtCore.QRect(2, 2, 57, 15))
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setGeometry(QtCore.QRect(15, 30, 57, 15))
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setGeometry(QtCore.QRect(15, 60, 71, 16))
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.numero = QtWidgets.QLineEdit(self.frame_6)
        self.numero.setGeometry(QtCore.QRect(90, 30, 191, 21))
        self.numero.setStyleSheet("color: rgb(0, 0, 0);")
        self.numero.setObjectName("numero")
        self.tipo = QtWidgets.QLineEdit(self.frame_6)
        self.tipo.setGeometry(QtCore.QRect(90, 58, 191, 21))
        self.tipo.setStyleSheet("color: rgb(0, 0, 0);")
        self.tipo.setObjectName("tipo")
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        self.label_17.setGeometry(QtCore.QRect(282, 32, 16, 16))
        self.label_17.setStyleSheet("color: red;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_6)
        self.label_18.setGeometry(QtCore.QRect(282, 62, 16, 16))
        self.label_18.setStyleSheet("color: red;")
        self.label_18.setObjectName("label_18")
        self.b_adicionar_contato = QtWidgets.QPushButton(self.frame_3)
        self.b_adicionar_contato.setGeometry(QtCore.QRect(70, 540, 80, 23))
        self.b_adicionar_contato.setStyleSheet("#b_adicionar_contato{\n"
"    color: black;\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#b_adicionar_contato:hover{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"#b_adicionar_conato:pressed{\n"
"    background-color: rgb(0, 255, 127);\n"
"}")
        self.b_adicionar_contato.setObjectName("b_adicionar_contato")
        self.b_cancelar_contato = QtWidgets.QPushButton(self.frame_3)
        self.b_cancelar_contato.setGeometry(QtCore.QRect(200, 540, 80, 23))
        self.b_cancelar_contato.setStyleSheet("#b_cancelar_contato{\n"
"    color: black;    \n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#b_cancelar_contato:hover{\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"#b_cancelar_conato:pressed{\n"
"    background-color: rgb(0, 255, 127);\n"
"}")
        self.b_cancelar_contato.setObjectName("b_cancelar_contato")
        self.verticalLayout.addWidget(self.frame_3)
        self.scrollAreaAdicionar.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelAdicionar.setText(_translate("Dialog", "ADICIONAR CONTATO"))
        self.label_3.setText(_translate("Dialog", "Dados Pessoais"))
        self.label_4.setText(_translate("Dialog", "Nome"))
        self.label_5.setText(_translate("Dialog", "Aniv:"))
        self.label_6.setText(_translate("Dialog", "e-mail:"))
        self.label_11.setText(_translate("Dialog", "*"))
        self.label_12.setText(_translate("Dialog", "*"))
        self.label_19.setText(_translate("Dialog", "*"))
        self.label_7.setText(_translate("Dialog", "Endereço"))
        self.label.setText(_translate("Dialog", "Rua:"))
        self.label_2.setText(_translate("Dialog", "Número:"))
        self.label_8.setText(_translate("Dialog", "Bairro:"))
        self.label_9.setText(_translate("Dialog", "Cidade:"))
        self.label_10.setText(_translate("Dialog", "Condomínio:"))
        self.label_13.setText(_translate("Dialog", "*"))
        self.label_14.setText(_translate("Dialog", "Telefone:"))
        self.label_15.setText(_translate("Dialog", "Número:"))
        self.label_16.setText(_translate("Dialog", "Fixo/Móvel:"))
        self.label_17.setText(_translate("Dialog", "*"))
        self.label_18.setText(_translate("Dialog", "*"))
        self.b_adicionar_contato.setText(_translate("Dialog", "Adicionar"))
        self.b_cancelar_contato.setText(_translate("Dialog", "Cancelar"))
