""" ESSE MÓDULO SERVE PARA TRATAR ALGUMAS POSSÍVEIS EXCEÇÕES QUE PODEM SER DISPARADAS COM A ENTRADA DE DADOS INCORRETA DO USUÁRIO, 
    POR EXEMPLO, NA FUNÇÃO DE CADASTRO O USUÁRIO PRECISA DIGITAR UM NOME COM MENOS OU IGUAL AO NÚMERO DE 100 CARACTERES, UM LOGIN
    COM MENOS OU IGUAL AO NÚMERO DE 50 CARACTERES E UMA SENHA COM MENOS OU IGUAL AO NUMERO DE 20 CARACTERES. 
    NA AÇÃO DE CADASTRAR, TAMBÉM É FEITA A VERIFICAÇÃO NO BANCO DE DADOS PARA VER SE JA NÃO EXISTE UM LOGIN JA CADASTRADO POIS SE
    O USUÁRIO TENTAR CADATRAR UM LOGIN EXISTENTE É DISPARADA UMA EXCESSÃO JA QUE A 'COLUNA' LOGIN É UNICA NO BAMCO DE DADOS"""

from model.models import Usuario
from model import connection
from model.operation_in_Bd import busca_login


class ExceptionRegister(Exception):

    """ EXCEÇÃO RESPONSÁVEL POR TRATAR OS ERROS DE ENTRADA DE DADOS
        VERIFICAÇÃO DE LOGINS JA EXISTENTES """

    def __init__(self,nome,login,senha):
        #CONSTRUTOR DA CLASSE   

        self.nome = nome
        self.login = login
        self.senha = senha

    
    def verificacao_register_user(self):
        #FAZ AS VERIFICAÇÕES DE ENTRADA DE DADOS E O TRATAMENTO SE 

        if(len(self.nome) > 100):
            print('Numero de caracteres em "nome" excedido (100) ou campo nulo !!!')
            print('-----------------------')    
            return True
        
        elif(len(self.login) > 50):
            print('Numero de caracteres em "login" excedido (50) !!!')
            print('-----------------------')    
            return True

        elif(len(self.senha) > 20):
            print('Numero de caracteres em "password" excedido (20) !!!')
            print('-----------------------')    
            return True
        elif(self.senha == '' or self.nome == '' or self.login == ''):
            return 'campo vazio'
        else:
            return False


    def verificacao_login_exist(self): 
        #FUNÇÃO QUE VERIFICA NO BANCO DE DADOS SE O LOGIN JA ESTA CADASTRADO         
      
        try:
            resultado = connection.session.query(Usuario.usuario_login).filter(Usuario.usuario_login == self.login).one_or_none()

            if(resultado == None):
                # SE SENHUM LOGIN FOR ENCONTRADO  RETORNA 'FALSE', POIS ERRO É IGUAL A FALSO SE O
                # LOGIN NÃO ESTA CADASTRADO NO BD
                return False 
            else:
                # SE ENCONTRAR ALGO NO BD É PQ JA EXISTE ESSE LOGIN E O ERRO É TRUE POIS NÃO PODE
                # CADASTRAR DOIS LOGINS
                print('Esse login ja esta cadastrado !!!')
                return True 
        except:
            
            # rerona erro pois o metodo one_or_none() retorna um erro se varias linhas  de resultado 
            #  forem encontradas
            return True


    def verfifica_erros_registro(self):
        # ESSE MÉTODO APENAS CHAMA OS OUTROS 2 PARA NÃO SER NECESSÁRIO
        # FAZER TODAS AS VERIFICAÇÕES EM UM MÉTODO SÓ

        verification1 = self.verificacao_register_user()
        verification2 = self.verificacao_login_exist()

        return (verification1,verification2)
            

