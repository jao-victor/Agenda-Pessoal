from PyQt5 import QtWidgets
from views.views_classes.view_login.janelaLogin import TelaLogin
from views.views_classes.view_principal.janelaPrincipal import JanelaPrincipal
import sys



app = QtWidgets.QApplication([])

login = TelaLogin()

if login.exec() == 1:
    sessao_user = login.retorna_sessao()
    janela_principal = JanelaPrincipal(sessao_user)
    janela_principal.show()

sys.exit(app.exec_())


