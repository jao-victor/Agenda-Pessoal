import sqlalchemy
from model.models import Usuario
from model import connection
from model.operation_in_Bd import busca_login_senha



def verification_login_user(login, senha):
    # ESSE MÉTODO VERIFICA SE O LOGIN E A SENHA DIGITADO EXISTE E COINCIDEM NO BANCO DE DADOS 

    # isso aqui é no model
    query = busca_login_senha(login, senha)
    
    try:
        if(login == query[0].usuario_login and senha == query[0].usuario_senha):
            print('LOGIN SUCESS')
            return False # pois erro é igual a falso
            
    except IndexError:
        print('Senha e login não coincidem ou não estão cadastradas !!!')
        return True # pois erro igual a verdadeiro
