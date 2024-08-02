from conf.database import Base
from sqlalchemy import Column, String, Integer
from models import subcategoria as s
from sqlalchemy.orm import relationship

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, unique=True)
    nombre = Column(String(50))
    categoria_ = Column(String(20), primary_key=True)
    descripcion = Column(String(100), index=True)

    productos = relationship("Producto", back_populates="categoria_rel")