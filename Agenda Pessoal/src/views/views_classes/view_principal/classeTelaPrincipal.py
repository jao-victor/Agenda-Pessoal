# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 650)
        MainWindow.setMinimumSize(QtCore.QSize(950, 650))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.navbar = QtWidgets.QFrame(self.centralwidget)
        self.navbar.setMinimumSize(QtCore.QSize(0, 51))
        self.navbar.setMaximumSize(QtCore.QSize(16777215, 51))
        self.navbar.setStyleSheet("#navbar{\n"
"    background-color: rgb(63, 125, 174);\n"
"}\n"
"")
        self.navbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navbar.setObjectName("navbar")
        self.logo_usuario = QtWidgets.QFrame(self.navbar)
        self.logo_usuario.setGeometry(QtCore.QRect(3, 3, 61, 41))
        self.logo_usuario.setStyleSheet("#logo_usuario{\n"
"    background-color: rgb(63, 125, 174);\n"
"    background-image: url(:/imagens/icone_user.png);\n"
"    background-repeat: no-repeat;\n"
"}")
        self.logo_usuario.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo_usuario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_usuario.setObjectName("logo_usuario")
        self.label_2 = QtWidgets.QLabel(self.navbar)
        self.label_2.setGeometry(QtCore.QRect(75, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(63, 125, 174);\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.navbar)
        self.barra_de_busca = QtWidgets.QFrame(self.centralwidget)
        self.barra_de_busca.setMinimumSize(QtCore.QSize(0, 51))
        self.barra_de_busca.setMaximumSize(QtCore.QSize(16777215, 51))
        self.barra_de_busca.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.barra_de_busca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_de_busca.setObjectName("barra_de_busca")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.barra_de_busca)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.barra_de_busca)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pesquisar_contato = QtWidgets.QLineEdit(self.frame)
        self.pesquisar_contato.setGeometry(QtCore.QRect(10, 20, 191, 21))
        self.pesquisar_contato.setMaximumSize(QtCore.QSize(191, 21))
        self.pesquisar_contato.setStyleSheet("color: black;")
        self.pesquisar_contato.setObjectName("pesquisar_contato")
        self.b_procurar = QtWidgets.QPushButton(self.frame)
        self.b_procurar.setGeometry(QtCore.QRect(210, 17, 80, 25))
        self.b_procurar.setMaximumSize(QtCore.QSize(80, 25))
        self.b_procurar.setStyleSheet("#b_procurar{\n"
"    color: white;\n"
"    background-color: rgb(63, 125, 174);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#b_procurar:hover{\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"#b_procurar:pressed{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.b_procurar.setObjectName("b_procurar")
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.barra_de_busca)
        self.frame_2.setMinimumSize(QtCore.QSize(100, 51))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.b_sair = QtWidgets.QPushButton(self.frame_2)
        self.b_sair.setGeometry(QtCore.QRect(30, 10, 60, 35))
        self.b_sair.setMinimumSize(QtCore.QSize(60, 35))
        self.b_sair.setMaximumSize(QtCore.QSize(60, 35))
        self.b_sair.setStyleSheet("#b_sair{\n"
"    color: white;\n"
"    background-color: rgb(63, 125, 174);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#b_sair:hover{\n"
"    color:black;\n"
"    background-color: rgb(255, 14, 14);\n"
"}\n"
"\n"
"")
        self.b_sair.setObjectName("b_sair")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.barra_de_busca)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 100))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 950, 506))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabela_de_contatos = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.tabela_de_contatos.setStyleSheet("#tabela_de_contatos{\n"
"    color: black;\n"
"            \n"
"    background-color: rgb(255, 255, 224);\n"
"}")
        self.tabela_de_contatos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_de_contatos.setObjectName("tabela_de_contatos")
        self.verticalLayout_2.addWidget(self.tabela_de_contatos)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.barra_de_botoes = QtWidgets.QFrame(self.centralwidget)
        self.barra_de_botoes.setMaximumSize(QtCore.QSize(16777215, 60))
        self.barra_de_botoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_de_botoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_de_botoes.setObjectName("barra_de_botoes")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.barra_de_botoes)
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b_adicionar = QtWidgets.QPushButton(self.barra_de_botoes)
        self.b_adicionar.setMinimumSize(QtCore.QSize(0, 33))
        self.b_adicionar.setStyleSheet("#b_adicionar{\n"
"    color: white;\n"
"    background-color: rgb(63, 125, 174);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#b_adicionar:hover{\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"#b_adicionar:pressed{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.b_adicionar.setObjectName("b_adicionar")
        self.horizontalLayout.addWidget(self.b_adicionar)
        self.b_atualizar = QtWidgets.QPushButton(self.barra_de_botoes)
        self.b_atualizar.setMinimumSize(QtCore.QSize(0, 33))
        self.b_atualizar.setStyleSheet("#b_atualizar{\n"
"    color: white;\n"
"    background-color: rgb(63, 125, 174);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#b_atualizar:hover{\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"#b_atualizar:pressed{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.b_atualizar.setObjectName("b_atualizar")
        self.horizontalLayout.addWidget(self.b_atualizar)
        self.b_deletar = QtWidgets.QPushButton(self.barra_de_botoes)
        self.b_deletar.setMinimumSize(QtCore.QSize(0, 33))
        self.b_deletar.setStyleSheet("#b_deletar{\n"
"    color: white;\n"
"    background-color: rgb(63, 125, 174);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#b_deletar:hover{\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"#b_deletar:pressed{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.b_deletar.setObjectName("b_deletar")
        self.horizontalLayout.addWidget(self.b_deletar)
        self.refresh = QtWidgets.QPushButton(self.barra_de_botoes)
        self.refresh.setMinimumSize(QtCore.QSize(0, 40))
        self.refresh.setMaximumSize(QtCore.QSize(70, 16777215))
        self.refresh.setStyleSheet("#refresh{\n"
"    color: white;\n"
"    background-color: rgb(63, 125, 174);\n"
"    background-image: url(:/imagens/rotacaoE.png);\n"
"    background-position:center;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#refresh:hover{\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"#refresh:pressed{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.refresh.setText("")
        self.refresh.setObjectName("refresh")
        self.horizontalLayout.addWidget(self.refresh)
        self.verticalLayout.addWidget(self.barra_de_botoes)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "UserName"))
        self.b_procurar.setText(_translate("MainWindow", "Buscar"))
        self.b_sair.setText(_translate("MainWindow", "Sair"))
        self.b_adicionar.setText(_translate("MainWindow", "ADICIONAR"))
        self.b_atualizar.setText(_translate("MainWindow", "ATUALIZAR"))
        self.b_deletar.setText(_translate("MainWindow", "DELETAR"))
