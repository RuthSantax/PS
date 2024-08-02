from conf.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Subcategoria(Base):
    __tablename__ = "subcategoria"
    id = Column(String(10), unique= True)
    subcategoria = Column(String(50), primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String(80))
    
    productos = relationship("producto", back_populates="subcategoria")
    