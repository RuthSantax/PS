from pydantic import BaseModel, Field, EmailStr, field_validator, SecretStr
from fastapi import status
from typing import Optional, List
from fastapi.exceptions import HTTPException
from datetime import date

class Venta(BaseModel):
    id: Optional[int] = None
    producto_id: int = Field(gt=0)
    usuario_id: int = Field(gt=0)
    cantidad: int = Field(gt=0)
    fecha_venta: date
    
    
