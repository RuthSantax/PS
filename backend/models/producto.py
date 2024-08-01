from conf.database import Base
from sqlalchemy import  Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    categoria_id = Column(String(20), ForeignKey('categoria.id'))
    nombre = Column(String(50))
    precio = Column(Integer)
    descripcion = Column(String(100))
    foto = Column(LargeBinary)
    
    
    categoria = relationship('Categoria', back_populates='productos')
    ventas = relationship('Venta', back_populates='producto')

    