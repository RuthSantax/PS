from conf.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Subcategoria(Base):
    __tablename__ = "subcategoria"
    id = Column(Integer(10), unique= True)
    subcategoria = Column(String(50), primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String(80))
    
    productos = relationship("Producto", back_populates="subcategoria")
    