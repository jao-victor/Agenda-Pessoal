from views.views_classes.view_principal.classeTelaPrincipal import Ui_MainWindow # importa a tela de login
from views.views_classes.imagens.janela_principal import imagens
from PyQt5.QtWidgets import QMainWindow
from model.operation_in_Bd import consulta_BD
from views.views_classes.view_principal.abstract_model_table import ModeloTabela
from PyQt5.QtWidgets import QHeaderView
from views.views_classes.view_principal.adicionar_contato.janelaAdicionar import TelaAdicionar 
from views.views_classes.view_principal.atualizar_contato.janelaAtualizar import TelaAtualizar 
from views.views_classes.view_principal.deletar_contato.janelaDeletar import TelaDeletar 
from views.views_classes.view_principal.tabela_de_busca.tabela_busca import TabelaBusca 



class JanelaPrincipal(QMainWindow):
    def __init__(self, sessao_user):
        super().__init__()
        self.sessao_user = sessao_user
        self.janela_principal = Ui_MainWindow()
        self.janela_principal.setupUi(self)
        self.id = self.sessao_user[0]

        self.carrega_tabela()
        self.janela_principal.label_2.setText(sessao_user[1])

        self.janela_principal.b_adicionar.clicked.connect(self.abre_janela_adicionar)
        self.janela_principal.refresh.clicked.connect(self.carrega_tabela)
        self.janela_principal.b_atualizar.clicked.connect(self.abre_janela_atualizar)
        self.janela_principal.b_deletar.clicked.connect(self.abre_janela_deletar)
        self.janela_principal.b_procurar.clicked.connect(self.abre_tabela_busca)
        self.janela_principal.b_sair.clicked.connect(self.fechar_janela)

    def carrega_tabela(self):

         # retorna a mesma sessão mais com o id do ususario
        self.dados_tabela = consulta_BD(self.id) # carrega os dados referente ao usuario da sessão pelo id do usuario
        self.modelo = ModeloTabela(self.dados_tabela)
        self.janela_principal.tabela_de_contatos.setModel(self.modelo)
        self.colunas = self.janela_principal.tabela_de_contatos.horizontalHeader()
        self.colunas.setSectionResizeMode(QHeaderView.Stretch)

    def abre_janela_adicionar(self):
        tela_adicionar = TelaAdicionar(self.sessao_user)
        tela_adicionar.exec()

    def abre_janela_atualizar(self):
        tela_atualizar = TelaAtualizar(self.id)
        tela_atualizar.exec()

    def abre_janela_deletar(self):
        tela_deletar = TelaDeletar(self.id)
        tela_deletar.exec()

    def abre_tabela_busca(self):
        self.nome_busca = self.janela_principal.pesquisar_contato.text()
        tabela_resultados = TabelaBusca(self.nome_busca, self.id)

    def fechar_janela(self):
        import sys
        self.close()
        sys.exit(1)
        
