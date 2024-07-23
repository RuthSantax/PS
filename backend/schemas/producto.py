from pydantic import BaseModel, Field, EmailStr, field_validator, SecretStr
from fastapi import status
from typing import Optional, List
from fastapi.exceptions import HTTPException


class Producto(BaseModel):
    id: Optional[int] = None
    categoria_id: str = Field(min_length=5, max_length=30)
    subcateg_id: str = Field(min_length=5, max_length=30)
    nombre: str = Field(min_length=5, max_length=30)
    precio: int = Field(gt=0)
    descripcion: str = Field(min_length=5, max_length=100)
    foto: Optional[bytes] = None
    
    
    class Config:
        json_scheme_extra = {
            "example": {
                "id": 1,
                "nombre": "Aro stras",
                "precio": 2000,
                "categoria_id": "AR",
                "subcateg_id": "316L",
                "descripcion": "Aros con stras y prendedor de acero quirurgico",
                "foto": "iVBORw0KGgoAAAANSUhEUgAAAAUA"  # Ejemplo de cadena Base64
            }
        }
