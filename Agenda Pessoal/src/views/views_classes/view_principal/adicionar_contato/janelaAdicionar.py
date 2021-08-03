from PyQt5.QtWidgets import QDialog
from views.views_classes.view_principal.adicionar_contato.classeTelaAdicionar import Ui_Dialog
from model.operation_in_Bd import insert
from PyQt5.QtWidgets import QMessageBox


class TelaAdicionar(QDialog):
    def __init__(self, sessao_user):
        super().__init__()

        self.tela_adicionar = Ui_Dialog()
        self.tela_adicionar.setupUi(self)
        self.tela_adicionar.b_adicionar_contato.clicked.connect(self.adicionar_contato)
        self.sessao_user = sessao_user
        self.tela_adicionar.b_cancelar_contato.clicked.connect(self.fechar_janela)

    def adicionar_contato(self):

        self.nome = self.tela_adicionar.nome.text()
        self.nasc = self.tela_adicionar.data.text()
        self.email = self.tela_adicionar.email.text()
        self.rua = self.tela_adicionar.rua.text()
        self.numero_endereco = self.tela_adicionar.numero_endereco.text()
        self.condominio = self.tela_adicionar.condomio.text()
        self.bairro = self.tela_adicionar.bairro.text()
        self.cidade = self.tela_adicionar.cidade.text()
        self.numero = self.tela_adicionar.numero.text()
        self.tipo = self.tela_adicionar.tipo.text()

        self.validado = self.valida_campos()

        if (self.validado == True):
            
            self.adicionou = insert(self.sessao_user, self.nome, self.nasc, self.email, self.rua,\
                self.numero_endereco, self.condominio, self.bairro, self.cidade,\
               self.numero,self.tipo)
            
            if (self.adicionou == True):

                self.nome = self.tela_adicionar.nome.setText('')
                self.email = self.tela_adicionar.email.setText('')
                self.rua = self.tela_adicionar.rua.setText('')
                self.numero_endereco = self.tela_adicionar.numero_endereco.setText('')
                self.condominio = self.tela_adicionar.condomio.setText('')
                self.bairro = self.tela_adicionar.bairro.setText('')
                self.cidade = self.tela_adicionar.cidade.setText('')
                self.numero = self.tela_adicionar.numero.setText('')
                self.tipo = self.tela_adicionar.tipo.setText('')

                msg = QMessageBox()
                msg.setWindowTitle('Contato Adicionado')
                msg.setText('Contato Adicionado')
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
                

    def valida_campos(self):
        msg = QMessageBox()

        if(self.nome == ''):
            msg.setIcon(QMessageBox.Critical)
            msg.setText('O campo nome esta vazio')
            msg.exec()
            self.fechar_janela()
        elif(self.nasc == ''):
            msg.setIcon(QMessageBox.Critical)
            msg.setText('O campo nasc esta vazio')
            msg.exec()
            self.fechar_janela()
        elif(self.numero == ''):
            msg.setIcon(QMessageBox.Critical)
            msg.setText('O campo número esta vazio')
            msg.exec()
            self.fechar_janela()
        elif(self.tipo == ''):
            msg.setIcon(QMessageBox.Critical)
            msg.setText('O campo Fixo/Móvel esta vazio')
            msg.exec()
            self.fechar_janela()
        elif(self.email == ''):
            msg.setIcon(QMessageBox.Critical)
            msg.setText('O campo email esta vazio')
            msg.exec()
            self.fechar_janela()
        elif(self.cidade == ''):
            msg.setIcon(QMessageBox.Critical)
            msg.setText('O campo cidade esta vazio')
            msg.exec()
            self.fechar_janela()
        else:
            return True
            
    def fechar_janela(self):
        self.reject()
