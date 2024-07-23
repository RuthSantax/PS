from conf.database import Base
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey('producto.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    cantidad = Column(Integer)
    fecha_venta = Column(Date)
    
     # Relaciones con las tablas de vehículos y usuarios
    producto = relationship('Producto', back_populates='ventas')
    usuario = relationship('Usuario', back_populates='ventas')
