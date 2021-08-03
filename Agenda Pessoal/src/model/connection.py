from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    engine =  create_engine('postgresql+psycopg2://postgres:joaovictor10@localhost/agenda_telefonica')
    Session = sessionmaker(engine)
    session = Session()
except Exception:
    print('FALHA AO CONECTAR COM O BANCO DE DADOS')    


