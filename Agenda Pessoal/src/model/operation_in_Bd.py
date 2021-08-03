from model import connection
from model.models import *
import sqlalchemy




def add_user(name,login,password):
    #ADICIONA USUÁRIO NO BANCO DE DADOS

    user = Usuario(usuario_nome = name, usuario_login = login, usuario_senha = password)
    connection.session.add(user)
    connection.session.commit()
    connection.session.close()


def get_sessao_user(login, senha): # nome invertido pois não se pode mudar uma tupla exitente
    # retorna o id do usuário correspondente ao login e a senha

    consulta = connection.session.query(Usuario.id, Usuario.usuario_nome, Usuario.usuario_login)\
        .filter(Usuario.usuario_login == login).filter(Usuario.usuario_senha == senha)

    sessao_user = consulta[0]
    connection.session.close()
    return sessao_user
    


def consulta_BD(id):    

    """ Esse método retorna os nomes das colunas e dados necessários para
        montar a tabela de visualização na janela principal"""

    # Essa é a consulta em SQL que retorna do dados para a montagem da tabela
    """
        SELECT contato.id, contato_nome, contato_email, contato_nasc, endereco, telefone_tipo, telefone_numero FROM contato
        INNER JOIN endereco on endereco.contato_id = contato.id
        INNER JOIN telefone on telefone.contato_id = contato.id
        WHERE usuario_id = 2
    """

    # Essa é a mesma consulta, porém em sqlalchemy
    consulta = connection.session.query(Contato.contato_nome, \
    Contato.contato_email, Contato.contato_nasc,\
        Endereco.rua, Endereco.numero, Endereco.condominio, Endereco.bairro, Endereco.cidade, \
            Telefone.telefone_numero, Telefone.telefone_tipo,Contato.id)\
    .join(Endereco, Endereco.contato_id == Contato.id)\
    .join(Telefone, Telefone.contato_id == Contato.id)\
    .filter(Contato.usuario_id == id)


    resultados = connection.session.execute(consulta)
    nome_colunas = ['Nome','e-mail','Data Nascimento', 'Rua','Lt', 'Condomínio', 'Bairro',\
         'Cidade', 'Telefone','Tipo-Telefone','Id']
    tuplas = [] # lista das tuplas retornadas pela consulta

    for linha in resultados:
        tuplas.append(linha)
      

    dados = (tuplas, nome_colunas)

    connection.session.close()
    
    return dados


def busca_login_senha(login, senha):
    # Esse método busca o login e a senha correspondentes

    query = connection.session.query(Usuario.usuario_login, Usuario.usuario_senha)\
        .filter(Usuario.usuario_login == login, Usuario.usuario_senha == senha) 

    connection.session.close()
    return query


def busca_login(login):
    # Esse método verifica no BD se o login passado por parâmetro esta cadastrado
    resultado = connection.session.query(Usuario.usuario_login).filter(Usuario.usuario_login == self.login).one_or_none()
    connection.session.close()
    return resultado[0]
    

"""      OPERAÇÕES DE CRUD      """

def insert(sessao_user, nome, nasc, email, e_rua,\
                numero_endereco, e_condominio, e_bairro, e_cidade, numero, tipo):


    try:
        contato = Contato(contato_nome = nome, contato_nasc = nasc, contato_email = email, usuario_id = sessao_user[0])
        connection.session.add(contato)
        connection.session.commit()


        connection.session.add_all([Endereco(cidade = e_cidade, bairro = e_bairro, rua = e_rua, \
            condominio = e_condominio, numero = numero_endereco, contato_id = contato.id), Telefone(telefone_tipo = tipo,\
                telefone_numero = numero, contato_id = contato.id)])

        connection.session.commit()
        
        return True

    except:
        print("ERRO NA INSERÇÃO")
    finally:
        connection.session.close()


def update(id, id_usuario, nome, nasc, email, e_rua,\
                numero_endereco, e_condominio, e_bairro, e_cidade, numero, tipo):

    result = connection.session.query(Contato.id).filter((Contato.id == id ) \
        & (Contato.usuario_id == id_usuario)).one_or_none()

    if (result != None):

        try:
            resultado = connection.session.query(Contato).filter(Contato.id == id).one_or_none()

            if(resultado == None):
                return 'nonexistent'

            else:

                connection.session.query(Contato).filter((Contato.id == id)  & (Contato.usuario_id == id_usuario)).\
                    update({Contato.contato_nome: nome, Contato.contato_nasc: nasc, Contato.contato_email:email}\
                        , synchronize_session = False)

                connection.session.query(Endereco).filter((Endereco.contato_id == id) & (Contato.usuario_id == id_usuario)).\
                    update({Endereco.cidade: e_cidade, Endereco.bairro: e_bairro, Endereco.rua: e_rua, Endereco.condominio\
                        :e_condominio, Endereco.numero: numero_endereco}, synchronize_session = False)

                connection.session.query(Telefone).filter((Telefone.contato_id == id)  & (Contato.usuario_id == id_usuario)).\
                    update({Telefone.telefone_numero: numero, Telefone.telefone_tipo: tipo}\
                        , synchronize_session = False)

                connection.session.commit()
                return True

        except:
            print("ERRO NA ATUALIZAÇÃO")
            return False
        finally:
            connection.session.close()
    else:
        return 'nao possui esse contato'
        
  


def delete(id_contato, id_usuario):

    result = connection.session.query(Contato.id).filter((Contato.id == id_contato ) \
        & (Contato.usuario_id == id_usuario)).one_or_none()

    if (result != None):

        try:
            connection.session.query(Endereco).filter((Endereco.contato_id == id_contato) & (Contato.usuario_id == id_usuario))\
                .delete(synchronize_session = False)

            connection.session.query(Telefone).filter((Telefone.contato_id == id_contato) & (Contato.usuario_id == id_usuario))\
                .delete(synchronize_session = False)

            connection.session.query(Contato).filter((Contato.id == id_contato) & (Contato.usuario_id == id_usuario))\
                .delete(synchronize_session = False)

            connection.session.commit()
            return True
        except:
            print('ERRO NO DELETE')
            return False
        finally:
            connection.session.close()

    else:
        return 'nao possui esse contato'
  

def select(nome, id):

    try:
        consulta = connection.session.query(Contato.contato_nome, \
        Contato.contato_email, Contato.contato_nasc,\
            Endereco.rua, Endereco.numero, Endereco.condominio, Endereco.bairro, Endereco.cidade, \
                Telefone.telefone_numero, Telefone.telefone_tipo,Contato.id)\
        .join(Endereco, Endereco.contato_id == Contato.id)\
        .join(Telefone, Telefone.contato_id == Contato.id)\
        .filter((Contato.contato_nome == nome) & (Contato.usuario_id == id))

        resultados = connection.session.execute(consulta)

        nome_colunas = ['Nome','e-mail','Data Nascimento', 'Rua','Lote', 'Condomínio', 'Bairro',\
            'Cidade', 'Telefone','Tipo-Telefone','Id']
        tuplas = [] # lista das tuplas retornadas pela consulta

        for linha in resultados:
            tuplas.append(linha)


        dados = (tuplas, nome_colunas)

        return dados

    except:
        print('ERRO NA OBTENÇÃO DOS DADOS')

    finally:
        connection.session.close()

