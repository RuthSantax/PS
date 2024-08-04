from conf.database import Base
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    categoria = Column(String(20), ForeignKey('categoria.categoria_'))
    subcategoria = Column(String(20), ForeignKey('subcategoria.subcategoria'))
    nombre = Column(String(50))
    descripcion = Column(String(100))
    precio = Column(Integer)
    

    
    
    categoria_rel = relationship('Categoria', back_populates='productos')
    subcategoria_rel = relationship('Subcategoria', back_populates='productos')
    ventas = relationship('Venta', back_populates='producto')

    