from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean

class Coordenadas(Base): #Estrutura para criar uma tabela
     __tablename__ = "coordenadas"
     id= Column(Integer, primary_key=True, autoincrement=True)
     x= Column(Integer)
     y= Column(Integer)
     z= Column(Integer)
     j1= Column(Integer)
     j2= Column(Integer)
     j3= Column(Integer)
     j4= Column(Integer)

     def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
        return f"Coordenada(id={self.id},x={self.x},y={self.y},z={self.z}, j1={self.j1},j2={self.j2},j3={self.j3},j4={self.j4})"
     
     def lista_dados(self):
        lista = [self.x, self.y, self.z, self.j1, self.j2, self.j3, self.j4]
        return lista