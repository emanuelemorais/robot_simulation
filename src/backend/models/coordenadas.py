from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Coordenadas(Base): #Estrutura para criar uma tabela
     __tablename__ = "coordenadas"
     id= Column(Integer, primary_key=True, autoincrement=True)
     x= Column(Float)
     y= Column(FLoat)
     z= Column(Float)
     r=Column(Float)

     def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
        return f"Coordenada(id={self.id},x={self.x},y={self.y},z={self.z}, r={self.r})"
     
     def lista_dados(self):
        lista = [self.x, self.y, self.z, self.j1, self.j2, self.j3, self.j4]
        return lista