from conf.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Subcategoria(Base):
    __tablename__ = "subcategoria"
    id = Column(Integer, unique= True)
    subcategoria = Column(String(20), primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String(80))
    
    productos = relationship("Producto", back_populates="subcategoria_rel")
    