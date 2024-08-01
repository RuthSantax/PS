from conf.database import Base
from sqlalchemy import Column, String, ForeignKey
from models import subcategoria as s
from sqlalchemy.orm import relationship

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(String(10), unique=True)
    nombre = Column(String(50))
    categ = Column(String(10), primary_key=True)
    subc = s.Subcategoria.subcategoria, ForeignKey('subcategoria.id'),
    descripcion = Column(String(100), index=True)
    
    subcategorias = relationship("Subcategoria", back_populates="categoria")
    productos = relationship("Producto", back_populates="categoria")