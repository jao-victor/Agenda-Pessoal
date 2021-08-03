from excecoes.exception_register import ExceptionRegister
from excecoes.exception_login import verification_login_user
from PyQt5.QtWidgets import QDialog
from views.views_classes.view_login.classeTelaLogin import Ui_Dialog # importa o dialogo de login
from views.views_classes.imagens.janela_login import imagem # importa as imagens da tela de login
from model.operation_in_Bd import add_user, get_sessao_user
from PyQt5.QtWidgets import QMessageBox


class TelaLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.janela_de_login = Ui_Dialog()
        self.janela_de_login.setupUi(self)

        self.janela_de_login.button_login.clicked.connect(self.login)
        self.janela_de_login.button_register.clicked.connect(self.register)

    def login(self):

        #bloco de definições dos valores das variáveis
        self.login = self.janela_de_login.login_login.text()
        self.senha = self.janela_de_login.login_password.text()

        # bloco de verificações
        erro =  verification_login_user(self.login, self.senha) # verifica se o login e a senha existem e coincidem
    
        if (erro == False):
            self.sessao_user = get_sessao_user(self.login, self.senha) 
            self.retorna_sessao()
            self.accept()

        elif(erro == True):
            msg = QMessageBox()
            msg.setWindowTitle('Erro de login')
            msg.setText('Senha e login não coincidem ou não estão cadastradas')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
            self.janela_de_login.login_login.setText('')
            self.janela_de_login.login_password.setText('')
            

    def retorna_sessao(self):
        return (self.sessao_user)


    def register(self):

        self.nome = self.janela_de_login.register_name.text()
        self.login = self.janela_de_login.register_login.text()
        self.senha = self.janela_de_login.register_password.text()

        verificacao = ExceptionRegister(self.nome, self.login, self.senha)
        error = verificacao.verfifica_erros_registro()
        
        if(error[0] == False and error[1] == False):
            add_user(self.nome, self.login, self.senha)
            self.janela_de_login.register_login.setText('')
            self.janela_de_login.register_name.setText('')
            self.janela_de_login.register_password.setText('')

            msg = QMessageBox()
            msg.setWindowTitle('Sucesso')
            msg.setText('Você esta cadastrado')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()

        elif(error[0] == True):
            msg = QMessageBox()
            msg.setWindowTitle('Erro de login')
            msg.setText('Número de caracteres excedido')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()

        elif(error[0] == 'campo vazio'):
            msg = QMessageBox()
            msg.setWindowTitle('Erro de login')
            msg.setText('Alguns Campos estão vazios')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()

        elif(error[1] == True):
            msg = QMessageBox()
            msg.setWindowTitle('Erro de login')
            msg.setText('Esse Login ja esta cadastrado')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
          


