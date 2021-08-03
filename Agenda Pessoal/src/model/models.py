from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import connection

Base = declarative_base()

#Tabela Usuario
class Usuario(Base): 
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key = True)
    usuario_nome =  Column (String(100), nullable = True)
    usuario_login = Column(String(50), unique = True, nullable = True)
    usuario_senha = Column(String(20), nullable = True)

    relacao_contato = relationship("Contato") # estabele a relação com a tabela contato

# Tabela Conatato
class Contato(Base):
    __tablename__ = 'contato'

    id = Column(Integer, primary_key = True)
    contato_nome = Column(String(100), nullable = True)
    contato_nasc = Column(String(10), nullable = True) # ano/mes/dia
    contato_email = Column(String(50), nullable = True)

    usuario_id = Column(Integer, ForeignKey('usuario.id')) # chave estrangeira - id da tabela usuario
    relacao_usuario = relationship("Usuario") # especifica a relação com a tabela usuario
    

#Tabela Endereço
class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key = True)
    cidade = Column(String(50), nullable = True)
    bairro = Column(String(50), nullable = False)
    rua = Column(String(50), nullable = False)
    condominio = Column(String(50), nullable = False)
    numero = Column(String(), nullable = False)
    contato_id = Column(Integer, ForeignKey('contato.id')) # Chave estrangeira - recebe o id da tabela contato
    relacao_contato = relationship('Contato') # define a relação com a tabela contato


#Tabela Telefone
class Telefone(Base):
    __tablename__ = 'telefone'

    id = Column(Integer, primary_key = True)
    telefone_tipo = Column(String(20), nullable = True)
    telefone_numero = Column(String(15), nullable = True)
    contato_id = Column(Integer, ForeignKey('contato.id')) # Chave estrangeira - recebe o id da tabela contato
    relacao_contato =  relationship('Contato') # define a relação com a tabela contato

Base.metadata.create_all(connection.engine)
