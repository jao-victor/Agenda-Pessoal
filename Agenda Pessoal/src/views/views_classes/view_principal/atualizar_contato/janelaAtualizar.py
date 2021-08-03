from PyQt5.QtWidgets import QDialog
from views.views_classes.view_principal.atualizar_contato.classeTelaAtualizar import Ui_Dialog
from model.operation_in_Bd import update
from PyQt5.QtWidgets import QMessageBox



class TelaAtualizar(QDialog):

    def __init__(self, id_usuario):
        super().__init__()
        self.tela_atualizar = Ui_Dialog()
        self.tela_atualizar.setupUi(self)
        self.id_usuario = id_usuario
    

        self.tela_atualizar.b_atualizar_contato.clicked.connect(self.atualiza_contato)
        self.tela_atualizar.b_cancelar_atualizacao.clicked.connect(self.fechar_janela)

    def atualiza_contato(self):
       
        self.id = self.tela_atualizar.id.text()
        self.nome = self.tela_atualizar.nome_contato.text()
        self.nasc = self.tela_atualizar.data.text()
        self.email = self.tela_atualizar.email.text()
        self.rua = self.tela_atualizar.rua.text()
        self.numero_endereco = self.tela_atualizar.numero_endereco.text()
        self.condominio = self.tela_atualizar.condomio.text()
        self.bairro = self.tela_atualizar.bairro.text()
        self.cidade = self.tela_atualizar.cidade.text()
        self.numero = self.tela_atualizar.numero.text()
        self.tipo = self.tela_atualizar.tipo.text()
        
        self.validado = self.valida_campos()
        
        try:
            self.id = int(self.id)
            self.id_validado = True
        except:
            msg2 = QMessageBox()
            msg2.setWindowTitle('Id Inválido')
            msg2.setText('Digite um id válido')
            msg2.setIcon(QMessageBox.Warning)
            msg2.exec()
            self.fechar_janela()
            self.id_validado = False

        if (self.validado == True and self.id_validado == True):
            self.atualizou = update(self.id, self.id_usuario, self.nome, self.nasc, self.email, self.rua,\
                self.numero_endereco, self.condominio, self.bairro, self.cidade,\
               self.numero,self.tipo)

            if(self.atualizou == True):
                
                self.id = self.tela_atualizar.id.setText('')
                self.nome = self.tela_atualizar.nome_contato.setText('')
                self.email = self.tela_atualizar.email.setText('')
                self.rua = self.tela_atualizar.rua.setText('')
                self.numero_endereco = self.tela_atualizar.numero_endereco.setText('')
                self.condominio = self.tela_atualizar.condomio.setText('')
                self.bairro = self.tela_atualizar.bairro.setText('')
                self.cidade = self.tela_atualizar.cidade.setText('')
                self.numero = self.tela_atualizar.numero.setText('')
                self.tipo = self.tela_atualizar.tipo.setText('')

            
                msg3 = QMessageBox()
                msg3.setWindowTitle('Contato Atualizado')
                msg3.setText('Contato Atualizado')
                msg3.setIcon(QMessageBox.Warning)
                msg3.exec()

            elif (self.atualizou == 'nonexistent'):
                msg4 = QMessageBox()
                msg4.setWindowTitle('Id Inválido')
                msg4.setText('O Id do contato não existe')
                msg4.setIcon(QMessageBox.Warning)
                msg4.exec()
                self.reject()

            elif(self.atualizou == False):
                #from PyQt5.QtWidgets import QMessageBox
                msg5 = QMessageBox()
                msg5.setText('Erro ao atualizar contato')
                msg5.setWindowTitle('Erro de atualização')
                msg5.setIcon(QMessageBox.Warning)
                msg5.exec()
                self.reject()

            elif(self.atualizou == 'nao possui esse contato'):
                #from PyQt5.QtWidgets import QMessageBox
                msg6 = QMessageBox()
                msg6.setText('Você não possui esse contato')
                msg6.setWindowTitle('ERRO')
                msg6.setIcon(QMessageBox.Critical)
                msg6.exec()
                

    def valida_campos(self):

        if(self.id == ''):
            msg7 = QMessageBox()
            msg7.setIcon(QMessageBox.Warning)
            msg7.setWindowTitle('Insira o Id')
            msg7.setText('Inseria o id do contato que deseja modificar')
            msg7.exec()
            self.fechar_janela()
        elif(self.nome == ''):
            msg8 = QMessageBox()
            msg8.setIcon(QMessageBox.Warning)
            msg8.setText('O campo nome esta vazio')
            msg8.exec()
            self.fechar_janela()
        
        elif(self.numero == ''):
            msg9 = QMessageBox()
            msg9.setIcon(QMessageBox.Warning)
            msg9.setText('O campo número esta vazio')
            msg9.exec()
            self.fechar_janela()
        elif(self.tipo == ''):
            msg10 = QMessageBox()
            msg10.setIcon(QMessageBox.Warning)
            msg10.setText('O campo Fixo/Móvel esta vazio')
            msg10.exec()
            self.fechar_janela()       
        elif(self.email == ''):
            msg11 = QMessageBox()
            msg11.setIcon(QMessageBox.Warning)
            msg11.setText('O campo email esta vazio')
            msg11.exec()
            self.fechar_janela()
        elif(self.cidade == ''):
            msg12 = QMessageBox()
            msg12.setIcon(QMessageBox.Warning)
            msg12.setText('O campo cidade esta vazio')
            msg12.exec()
            self.fechar_janela()
        else:
            return True

    def fechar_janela(self):
        self.reject()

