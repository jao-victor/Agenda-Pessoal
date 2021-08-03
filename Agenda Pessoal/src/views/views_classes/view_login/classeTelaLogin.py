# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 513)
        Dialog.setMinimumSize(QtCore.QSize(653, 513))
        Dialog.setMaximumSize(QtCore.QSize(653, 513))
        self.area_logo = QtWidgets.QFrame(Dialog)
        self.area_logo.setGeometry(QtCore.QRect(0, 0, 653, 115))
        self.area_logo.setMaximumSize(QtCore.QSize(16777215, 115))
        self.area_logo.setStyleSheet("background-color: rgb(63, 125, 174);\n"
"")
        self.area_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.area_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.area_logo.setObjectName("area_logo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.area_logo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_image = QtWidgets.QFrame(self.area_logo)
        self.frame_image.setMaximumSize(QtCore.QSize(140, 140))
        self.frame_image.setStyleSheet("#frame_image{\n"
"    background-image: url(:/imagem/agenda.png);\n"
"    background-position:center;\n"
"}\n"
"")
        self.frame_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.horizontalLayout_2.addWidget(self.frame_image)
        self.box_register_login = QtWidgets.QFrame(Dialog)
        self.box_register_login.setGeometry(QtCore.QRect(0, 115, 653, 398))
        self.box_register_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.box_register_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_register_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_register_login.setObjectName("box_register_login")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.box_register_login)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.box_login = QtWidgets.QFrame(self.box_register_login)
        self.box_login.setMaximumSize(QtCore.QSize(240, 320))
        self.box_login.setStyleSheet("background-color: rgb(63, 125, 174);\n"
"")
        self.box_login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.box_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_login.setObjectName("box_login")
        self.login_login = QtWidgets.QLineEdit(self.box_login)
        self.login_login.setGeometry(QtCore.QRect(10, 100, 221, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.login_login.setFont(font)
        self.login_login.setStyleSheet("#login_login{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 5em;\n"
"    color:white;\n"
"}")
        self.login_login.setText("")
        self.login_login.setAlignment(QtCore.Qt.AlignCenter)
        self.login_login.setDragEnabled(False)
        self.login_login.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.login_login.setObjectName("login_login")
        self.login_password = QtWidgets.QLineEdit(self.box_login)
        self.login_password.setGeometry(QtCore.QRect(10, 170, 221, 23))
        self.login_password.setStyleSheet("#login_password{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 5em;\n"
"    color:white;\n"
"}\n"
"")
        self.login_password.setText("")
        self.login_password.setFrame(True)
        self.login_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.login_password.setAlignment(QtCore.Qt.AlignCenter)
        self.login_password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.login_password.setObjectName("login_password")
        self.label = QtWidgets.QLabel(self.box_login)
        self.label.setGeometry(QtCore.QRect(90, 20, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.button_login = QtWidgets.QPushButton(self.box_login)
        self.button_login.setGeometry(QtCore.QRect(80, 280, 80, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_login.setFont(font)
        self.button_login.setStyleSheet("#button_login{\n"
"    color: black;\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#button_login:hover{\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"#button_login:pressed{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.button_login.setObjectName("button_login")
        self.horizontalLayout.addWidget(self.box_login)
        self.box_register = QtWidgets.QFrame(self.box_register_login)
        self.box_register.setMaximumSize(QtCore.QSize(240, 320))
        self.box_register.setStyleSheet("background-color: rgb(63, 125, 174);\n"
"\n"
"")
        self.box_register.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.box_register.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_register.setObjectName("box_register")
        self.register_name = QtWidgets.QLineEdit(self.box_register)
        self.register_name.setGeometry(QtCore.QRect(10, 100, 221, 23))
        self.register_name.setStyleSheet("#register_name{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 5em;\n"
"    color:white;\n"
"}")
        self.register_name.setAlignment(QtCore.Qt.AlignCenter)
        self.register_name.setObjectName("register_name")
        self.register_password = QtWidgets.QLineEdit(self.box_register)
        self.register_password.setGeometry(QtCore.QRect(10, 210, 221, 23))
        self.register_password.setStyleSheet("#register_password{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 5em;\n"
"    color:white;\n"
"}")
        self.register_password.setAlignment(QtCore.Qt.AlignCenter)
        self.register_password.setObjectName("register_password")
        self.register_login = QtWidgets.QLineEdit(self.box_register)
        self.register_login.setGeometry(QtCore.QRect(10, 158, 221, 23))
        self.register_login.setStyleSheet("#register_login{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 5em;\n"
"    color:white;\n"
"}")
        self.register_login.setAlignment(QtCore.Qt.AlignCenter)
        self.register_login.setObjectName("register_login")
        self.label_2 = QtWidgets.QLabel(self.box_register)
        self.label_2.setGeometry(QtCore.QRect(55, 20, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.button_register = QtWidgets.QPushButton(self.box_register)
        self.button_register.setGeometry(QtCore.QRect(90, 280, 80, 23))
        self.button_register.setStyleSheet("#button_register{\n"
"    color: black;\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-style: solid;\n"
"}\n"
"\n"
"#button_register:hover{\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"#button_register:pressed{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.button_register.setObjectName("button_register")
        self.horizontalLayout.addWidget(self.box_register)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_login.setPlaceholderText(_translate("Dialog", "LOGIN"))
        self.login_password.setPlaceholderText(_translate("Dialog", "PASSWORD"))
        self.label.setText(_translate("Dialog", "LOGIN"))
        self.button_login.setText(_translate("Dialog", "Login"))
        self.register_name.setPlaceholderText(_translate("Dialog", "NAME"))
        self.register_password.setPlaceholderText(_translate("Dialog", "PASSWORD"))
        self.register_login.setPlaceholderText(_translate("Dialog", "LOGIN"))
        self.label_2.setText(_translate("Dialog", "REGISTRAR-SE"))
        self.button_register.setText(_translate("Dialog", "Register"))
