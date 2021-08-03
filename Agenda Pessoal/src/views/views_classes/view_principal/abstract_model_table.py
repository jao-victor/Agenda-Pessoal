from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor 

class ModeloTabela(QAbstractTableModel):
    def __init__(self, dados=None):
        QAbstractTableModel.__init__(self)
        
        self.dados_tabela = dados[0]
        self.nome_colunas = dados[1]

        self.load_data(self.dados_tabela)

    def load_data(self, dados):
        self.num_linhas = len(self.dados_tabela)
        self.num_colunas = len(self.nome_colunas)


    def rowCount(self, parent = QModelIndex()):
        # método obrigatório
        return self.num_linhas
        
    def columnCount(self, parent = QModelIndex()):
        # método obrigatório
        return self.num_colunas

    def data(self, index, role=Qt.DisplayRole):
        # index chama de montagem (ordem)
        # método obrigatório   
        
        coluna = index.column()
        linha = index.row()

        if (role == Qt.DisplayRole):
            return str(self.dados_tabela[linha][coluna])
        elif (role == Qt.TextAlignmentRole):
            Qt.AlignLeft
        

        return None   
        

    def headerData(self, section, orientation, role):
        #orientation = vertical(titulos da linha)-      horizontal(titulos das colunas)
        # section é a linhas de onde vamos pegar as informações
        # conveção
            
        if (role != Qt.DisplayRole): #Se o role não for do tipo, monta o cabeçalho no horizontal 
            return None

        if (orientation == Qt.Horizontal):
            return self.nome_colunas[section] # o nome das colunas - na 1º chamada id -  na 2º nome e sucessivamente
         

 




 