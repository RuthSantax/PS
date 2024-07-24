from conf.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(128))
    rol = Column(String(50))
    
    ventas = relationship("Venta", back_populates="usuario")
    
