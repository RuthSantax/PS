from conf.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Subcategoria(Base):
    __tablename__ = "subcategoria"
    id = Column(String(10), primary_key=True)
    Subcategoria_id = Column(String(50), ForeignKey("categoria.id"))
    nombre = Column(String(50))
    descripcion = Column(String(80))
    
    productos = relationship("Producto", back_populates="subcategoria")
    categoria = relationship("Categoria", back_populates="subcategorias")