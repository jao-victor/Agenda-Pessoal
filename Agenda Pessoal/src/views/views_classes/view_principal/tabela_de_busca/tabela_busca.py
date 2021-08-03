from PyQt5.QtWidgets import QDialog
from views.views_classes.view_principal.tabela_de_busca.classeTabelaBusca import Ui_Dialog
from views.views_classes.view_principal.abstract_model_table import ModeloTabela
from PyQt5.QtWidgets import QHeaderView
from model.operation_in_Bd import select
from PyQt5.QtWidgets import QMessageBox



class TabelaBusca(QDialog):
    def __init__(self,nome_busca, id):
        super().__init__()

        self.tabela_resultado = Ui_Dialog()
        self.tabela_resultado.setupUi(self)
        self.nome_busca = nome_busca
        self.id = id
        self.carrega_tabela()
      

    def carrega_tabela(self):

        if(self.nome_busca == ''):

            msg = QMessageBox()
            msg.setWindowTitle('Falta Argumentos')
            msg.setText('O campo esta vazio, digite um nome.')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()

        else:

            self.dados_tabela = select(self.nome_busca, self.id) 

            if(len(self.dados_tabela[0]) > 0):
            
                self.modelo = ModeloTabela(self.dados_tabela)
                self.tabela_resultado.tabela_resultado_busca.setModel(self.modelo)
                self.colunas = self.tabela_resultado.tabela_resultado_busca.horizontalHeader()
                self.colunas.setSectionResizeMode(QHeaderView.Stretch)
                self.exec()

            else:
                msg = QMessageBox()
                msg.setWindowTitle('Busca')
                msg.setText('Não foi encontrado contatos com esse nome.')
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
