from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.coordenadas import Coordenadas

# engine = create_engine('sqlite:///:memory:', echo=True) #Cria o banco em memória
engine = create_engine('sqlite+pysqlite:///banco.db', echo=True) #Cria o banco com caminho relativo


#Cria uma sessão para conversar com banco de dados (SQLite no caso)
Session = sessionmaker(bind=engine)
session = Session()

#Cria as tabelas se elas não existirem
Base.metadata.create_all(engine) 
