from conf.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from models import subcategoria as s
from sqlalchemy.orm import relationship

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(String(10), unique=True)
    nombre = Column(String(50))
    categoria = Column(String(10), primary_key=True)
    descripcion = Column(String(100), index=True)

    productos = relationship("Producto", back_populates="categoria")