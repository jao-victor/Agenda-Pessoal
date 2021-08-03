from views.views_classes.view_principal.deletar_contato.classeTelaDeletar import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox
from model.operation_in_Bd import delete

class TelaDeletar(QDialog):
    def __init__(self,id_usuario):
        super().__init__()

        self.tela_deletar = Ui_Dialog()
        self.tela_deletar.setupUi(self)
        self.id_usuario = id_usuario

        self.tela_deletar.b_excluir_contato.clicked.connect(self.excluir)

    def excluir(self):

        self.id = self.tela_deletar.id.text()

        try:
            self.id = int(self.id)
        except:
            msg = QMessageBox()
            msg.setWindowTitle('Id Inválido')
            msg.setText('Digite um id válido')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()


        if(self.id != '' and type(self.id) == int):
            self.deletado = delete(self.id, self.id_usuario)

            if(self.deletado == True):
                msg = QMessageBox()
                msg.setWindowTitle('Contato Deletado')
                msg.setText('Contato Deletado')
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
                self.id = self.tela_deletar.id.setText('')

            elif(self.deletado == 'nonexistent'):
                msg = QMessageBox()
                msg.setWindowTitle('Id Inválido')
                msg.setText('O Id do contato não existe')
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
            elif(self.deletado == 'nao possui esse contato'):
                msg = QMessageBox()
                msg.setText('Você não possui esse contato')
                msg.setWindowTitle('ERRO')
                msg.setIcon(QMessageBox.Warning)
                msg.exec()

        elif(self.id == ''):
            msg = QMessageBox()
            msg.setWindowTitle('Id Inválido')
            msg.setText('Digite um id válido')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        